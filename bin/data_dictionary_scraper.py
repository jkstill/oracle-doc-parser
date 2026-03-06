#!/usr/bin/env python3
"""
Oracle Documentation RAG Scraper
Parses local Oracle HTML docs (file:// paths) and outputs structured chunks
suitable for RAG pipelines: JSONL, Markdown files, and SQLite.

Usage:
    python scraper.py --path /path/to/oracle/docs --version 19c --doctype database_reference
    python scraper.py --path /path/to/oracle/docs --version 19c --doctype plsql_packages
    python scraper.py --path /path/to/oracle/docs --version 23ai --doctype all
"""

import argparse
import json
import logging
import re
import sqlite3
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class DocChunk:
    """One RAG chunk — one view, one package subprogram, etc."""
    id: str                          # Unique: version__type__name
    name: str                        # E.g. DBA_SEGMENTS, DBMS_STATS.GATHER_TABLE_STATS
    object_type: str                 # data_dictionary_view | plsql_package | plsql_subprogram
    oracle_version: str              # 19c, 21c, 23ai …
    doc_type: str                    # database_reference | plsql_packages
    parent: Optional[str]            # Package name for subprograms
    category: Optional[str]          # E.g. storage, security, performance
    description: str                 # Plain text description
    columns: list[dict]              # [{name, type, description}, …]  (views)
    parameters: list[dict]           # [{name, type, mode, description}, …] (subprograms)
    return_type: Optional[str]       # For functions
    syntax: Optional[str]            # Raw syntax block if present
    usage_notes: str                 # Any additional notes
    source_file: str                 # Relative path of source HTML
    source_url: str                  # file:// URL
    tags: list[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        """Render chunk as Markdown with YAML front-matter."""
        lines = [
            "---",
            f"id: {self.id}",
            f"name: {self.name}",
            f"object_type: {self.object_type}",
            f"oracle_version: {self.oracle_version}",
            f"doc_type: {self.doc_type}",
        ]
        if self.parent:
            lines.append(f"parent: {self.parent}")
        if self.category:
            lines.append(f"category: {self.category}")
        if self.tags:
            lines.append(f"tags: [{', '.join(self.tags)}]")
        lines += [
            f"source_file: {self.source_file}",
            "---",
            "",
            f"# {self.name}",
            "",
            self.description,
        ]

        if self.syntax:
            lines += ["", "## Syntax", "", "```sql", self.syntax.strip(), "```"]

        if self.columns:
            lines += ["", "## Columns", "", "| Column | Type | Description |",
                      "|--------|------|-------------|"]
            for col in self.columns:
                name = col.get("name", "")
                ctype = col.get("type", "")
                desc = col.get("description", "").replace("\n", " ")
                lines.append(f"| {name} | {ctype} | {desc} |")

        if self.parameters:
            lines += ["", "## Parameters", "", "| Parameter | Type | Mode | Description |",
                      "|-----------|------|------|-------------|"]
            for p in self.parameters:
                pname = p.get("name", "")
                ptype = p.get("type", "")
                pmode = p.get("mode", "")
                pdesc = p.get("description", "").replace("\n", " ")
                lines.append(f"| {pname} | {ptype} | {pmode} | {pdesc} |")

        if self.return_type:
            lines += ["", f"**Returns:** `{self.return_type}`"]

        if self.usage_notes:
            lines += ["", "## Usage Notes", "", self.usage_notes]

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# HTML parsing helpers
# ---------------------------------------------------------------------------

def load_html(path: Path) -> BeautifulSoup:
    for enc in ("utf-8", "iso-8859-1", "windows-1252"):
        try:
            return BeautifulSoup(path.read_text(encoding=enc), "lxml")
        except (UnicodeDecodeError, LookupError):
            continue
    raise ValueError(f"Cannot decode {path}")


def clean_text(element) -> str:
    """Extract clean text from a BS4 element."""
    if element is None:
        return ""
    return re.sub(r"\s+", " ", element.get_text(separator=" ")).strip()


def parse_table_to_dicts(table, col_names: list[str]) -> list[dict]:
    """
    Parse an HTML table into a list of dicts using the provided column keys.
    Skips header rows. Tolerates ragged rows.
    """
    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all(["td", "th"])
        if not cells:
            continue
        # Skip rows that are all <th> (header rows)
        if all(c.name == "th" for c in cells):
            continue
        texts = [clean_text(c) for c in cells]
        row = {col_names[i]: texts[i] for i in range(min(len(col_names), len(texts)))}
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Database Reference parser
# ---------------------------------------------------------------------------

def detect_view_category(name: str) -> str:
    """Heuristic category from view name."""
    n = name.upper()
    cats = {
        "SEGMENT": "storage", "EXTENT": "storage", "TABLESPACE": "storage",
        "INDEX": "index", "TABLE": "tables", "COLUMN": "tables",
        "USER": "security", "ROLE": "security", "PRIV": "security", "GRANT": "security",
        "SESSION": "performance", "STAT": "performance", "WAIT": "performance",
        "SQL": "sql", "CURSOR": "sql",
        "LOG": "logging", "REDO": "logging", "ARCHIVE": "logging",
        "OBJECT": "objects", "PROCEDURE": "objects", "FUNCTION": "objects",
        "TRIGGER": "objects", "VIEW": "objects", "SEQUENCE": "objects",
        "PARAM": "configuration", "INIT": "configuration",
        "AUDIT": "auditing",
        "CONSTRAINT": "integrity",
        "PARTITION": "partitioning",
        "SYS": "internal",
    }
    for keyword, cat in cats.items():
        if keyword in n:
            return cat
    return "general"


def parse_view_tags(name: str) -> list[str]:
    tags = []
    n = name.upper()
    if n.startswith("DBA_"):
        tags.append("dba")
    elif n.startswith("ALL_"):
        tags.append("all")
    elif n.startswith("USER_"):
        tags.append("user")
    elif n.startswith("V$") or n.startswith("GV$"):
        tags.append("dynamic_performance")
    return tags


def parse_database_reference_page(html_path: Path, version: str) -> list[DocChunk]:
    """
    Parse a single Oracle Database Reference HTML page.

    Actual structure (Oracle 19c/21c/23ai Bootstrap-based docs):
      <h2 class="sect2"><span class="enumeration_section">4.191 </span>DBA_CHANGE_NOTIFICATION_REGS</h2>
      <div class="ind">
        <p>Description text...</p>
        <div class="tblformalwide">
          <table class="FormalWide">
            <thead><tr><th>Column</th><th>Datatype</th><th>NULL</th><th>Description</th></tr></thead>
            <tbody>...</tbody>
          </table>
        </div>
      </div>
    """
    soup = load_html(html_path)

    # Remove noscript boilerplate — it appears in the body and pollutes text extraction
    for tag in soup.find_all("div", class_="noscript"):
        tag.decompose()

    # --- View name: h2.sect2, stripping the "4.191 " enumeration prefix ---
    h2 = soup.find("h2", class_="sect2")
    if h2 is None:
        return []

    # Remove the enumeration_section span so we get just the view name
    enum_span = h2.find("span", class_="enumeration_section")
    if enum_span:
        enum_span.decompose()
    name = clean_text(h2)

    # Must look like a data dictionary object
    if not re.match(
        r"^(DBA_|ALL_|USER_|V\$|GV\$|CDB_|DICT|GLOBAL_NAME|SESSION_|NLS_|"
        r"INDEX_|ROLE_|TABLE_|COLUMN_|AUDIT_|RESOURCE_|DATABASE_|PROXY_)",
        name.upper(),
    ):
        return []

    # --- Description: first <p> inside <div class="ind"> ---
    ind_div = soup.find("div", class_="ind")
    description = ""
    if ind_div:
        for p in ind_div.find_all("p"):
            txt = clean_text(p)
            # Skip navigation noise and very short fragments
            if txt and len(txt) > 20 and "navigation purposes only" not in txt:
                description = txt
                break

    # --- Columns: <table class="FormalWide"> ---
    # Headers are: Column, Datatype, NULL, Description
    columns = []
    formal_table = soup.find("table", class_="FormalWide")
    if formal_table:
        for tr in formal_table.find_all("tr"):
            cells = tr.find_all("td")
            if len(cells) < 2:
                continue  # skip header row (uses <th>)
            col_name = clean_text(cells[0])
            col_type = clean_text(cells[1])
            nullable = clean_text(cells[2]) if len(cells) > 2 else ""
            col_desc = clean_text(cells[3]) if len(cells) > 3 else ""
            if not col_name:
                continue
            columns.append({
                "name": col_name,
                "type": col_type,
                "nullable": nullable,
                "description": col_desc,
            })

    # --- Usage notes: infoboxnotealso divs and section divs ---
    notes_parts = []
    for tag in soup.find_all("div", class_=re.compile(r"infobox|section|alert")):
        txt = clean_text(tag)
        if txt and txt != description and len(txt) > 10 and "navigation purposes only" not in txt:
            notes_parts.append(txt)
    usage_notes = " ".join(notes_parts[:5])

    safe_name = re.sub(r"[^A-Za-z0-9_$]", "_", name)
    return [DocChunk(
        id=f"{version}__{safe_name}",
        name=name,
        object_type="data_dictionary_view",
        oracle_version=version,
        doc_type="database_reference",
        parent=None,
        category=detect_view_category(name),
        description=description,
        columns=columns,
        parameters=[],
        return_type=None,
        syntax=None,
        usage_notes=usage_notes,
        source_file=str(html_path.name),
        source_url=f"file://{html_path}",
        tags=parse_view_tags(name),
    )]


# ---------------------------------------------------------------------------
# PL/SQL Packages parser
# ---------------------------------------------------------------------------

SUBPROGRAM_TYPES = re.compile(
    r"\b(PROCEDURE|FUNCTION|PRAGMA|TYPE|CONSTANT|EXCEPTION)\b", re.IGNORECASE
)


def extract_package_name(soup: BeautifulSoup, html_path: Path) -> str:
    """
    Extract package name from the page h2.sect2 heading.
    Strips leading enumeration like '280 ' or '42.1 '.
    Falls back to filename stem.
    """
    h2 = soup.find("h2", class_="sect2")
    if h2:
        span = h2.find("span", class_=re.compile(r"enumeration"))
        if span:
            span.decompose()
        raw = clean_text(h2)
        # Take first token — e.g. "DBMS_STATS" from "DBMS_STATS Package"
        name = raw.split()[0].upper().rstrip(".")
        return name
    return html_path.stem.upper()


def parse_plsql_packages_page(html_path: Path, version: str) -> list[DocChunk]:
    """
    Parse a single Oracle PL/SQL Packages Reference HTML page.

    Actual structure (Oracle 19c Bootstrap-based docs):
      <h2 class="sect2"><span class="enumeration_chapter">280 </span>ANYDATA TYPE</h2>
      <div class="ind">
        <p>Package description...</p>
        <!-- Summary table -->
        <div class="tblformal">
          <table class="Formal">
            <thead><tr><th>Subprogram</th><th>Description</th></tr></thead>
          </table>
        </div>
        <!-- One props_rev_3 div per subprogram -->
        <div class="props_rev_3">
          <h4 class="sect4"><span class="enumeration_section">280.3.1 </span>BEGINCREATE Static Procedure</h4>
          <p>Subprogram description...</p>
          <pre class="oac_no_warn">PROCEDURE BEGINCREATE(...);</pre>
          <table class="Formal">
            <thead><tr><th>Parameter</th><th>Description</th></tr></thead>
          </table>
        </div>
      </div>
    """
    soup = load_html(html_path)
    chunks = []

    package_name = extract_package_name(soup, html_path)

    # Package-level description: first <p> in <div class="ind">
    ind_div = soup.find("div", class_="ind")
    pkg_desc = ""
    if ind_div:
        first_p = ind_div.find("p")
        pkg_desc = clean_text(first_p) if first_p else ""

    # Each subprogram lives in a <div class="props_rev_3">
    subprogram_divs = soup.find_all("div", class_="props_rev_3")

    for div in subprogram_divs:
        # Heading: h3.sect3 or h4.sect4
        h = div.find(re.compile(r"h[3-5]"), class_=re.compile(r"sect[3-5]"))
        if h is None:
            continue

        # Strip enumeration span
        enum_span = h.find("span", class_=re.compile(r"enumeration"))
        if enum_span:
            enum_span.decompose()
        raw_heading = clean_text(h)

        # Skip non-subprogram sections: Restrictions, Operational Notes,
        # Summary, Constants, Types, Exceptions, etc.
        skip_patterns = re.compile(
            r"\b(restriction|note|summary|overview|constant|exception|"
            r"type\b|return|deprecat|desupport|introduc|example|usage|"
            r"privilege|security|property|compatib)\b",
            re.IGNORECASE,
        )
        if skip_patterns.search(raw_heading):
            continue

        # Must contain a recognisable subprogram keyword or look like an identifier
        is_subprogram = bool(re.search(
            r"\b(procedure|function|member|static|constructor)\b",
            raw_heading, re.IGNORECASE,
        ))
        looks_like_identifier = bool(re.match(r"^[A-Z][A-Z0-9_$*]+\b", raw_heading.upper()))
        if not is_subprogram and not looks_like_identifier:
            continue

        # Derive clean subprogram name — first word, strip trailing keywords
        subprog_name = raw_heading.split()[0].upper().rstrip(".")
        # Remove trailing type qualifiers like "Procedure", "Function" if fused
        subprog_name = re.sub(r"(PROCEDURE|FUNCTION|MEMBER|STATIC)$", "", subprog_name)

        full_name = (
            f"{package_name}.{subprog_name}"
            if subprog_name != package_name
            else subprog_name
        )

        # Description: first <p> in this div
        desc_p = div.find("p")
        description = clean_text(desc_p) if desc_p else pkg_desc

        # Syntax: <pre class="oac_no_warn"> — take the first one
        syntax = ""
        pre = div.find("pre", class_=re.compile(r"oac_no_warn|code"))
        if pre is None:
            pre = div.find("pre")
        if pre:
            syntax = pre.get_text().strip()

        # Detect function vs procedure from syntax or heading
        is_function = bool(re.search(r"\bRETURN\b", syntax, re.IGNORECASE)) or \
                      bool(re.search(r"\bfunction\b", raw_heading, re.IGNORECASE))
        return_type = None
        if is_function and syntax:
            ret_match = re.search(r"RETURN\s+([A-Z][A-Z0-9_.$%()]*)", syntax, re.IGNORECASE)
            return_type = ret_match.group(1).rstrip(";") if ret_match else "UNKNOWN"

        # Parameters: <table class="Formal"> with Parameter/Description headers
        parameters = []
        for tbl in div.find_all("table", class_="Formal"):
            headers = [clean_text(th) for th in tbl.find_all("th")]
            if not headers or not any(
                h.lower() in ("parameter", "param", "argument") for h in headers
            ):
                continue
            for tr in tbl.find_all("tr"):
                cells = tr.find_all("td")
                if len(cells) < 2:
                    continue
                param_name = clean_text(cells[0])
                param_desc = clean_text(cells[1])
                if not param_name:
                    continue
                # Mode and type often embedded in description or syntax --
                # extract from syntax if possible
                mode = ""
                ptype = ""
                if syntax:
                    # Look for: param_name [IN|OUT|IN OUT] type
                    pm = re.search(
                        rf"\b{re.escape(param_name)}\s+(IN\s+OUT|IN|OUT)?\s*([A-Z][A-Z0-9_.$%()]*)",
                        syntax, re.IGNORECASE,
                    )
                    if pm:
                        mode = pm.group(1).strip() if pm.group(1) else "IN"
                        ptype = pm.group(2).strip()
                parameters.append({
                    "name": param_name,
                    "type": ptype,
                    "mode": mode,
                    "description": param_desc,
                })
            break  # only the first matching parameter table per subprogram

        # Usage notes
        notes_parts = []
        for tag in div.find_all("div", class_=re.compile(r"infobox|section|note|caution|warning")):
            txt = clean_text(tag)
            if txt and txt != description and len(txt) > 20:
                notes_parts.append(txt)
        usage_notes = " ".join(notes_parts[:5])

        if is_function:
            obj_type = "plsql_function"
        elif re.search(r"\bprocedure\b", raw_heading + " " + syntax, re.IGNORECASE):
            obj_type = "plsql_procedure"
        else:
            obj_type = "plsql_subprogram"

        safe_name = re.sub(r"[^A-Za-z0-9_$.]", "_", full_name)
        chunk = DocChunk(
            id=f"{version}__{safe_name}",
            name=full_name,
            object_type=obj_type,
            oracle_version=version,
            doc_type="plsql_packages",
            parent=package_name,
            category=None,
            description=description,
            columns=[],
            parameters=parameters,
            return_type=return_type,
            syntax=syntax,
            usage_notes=usage_notes,
            source_file=str(html_path.name),
            source_url=f"file://{html_path}",
            tags=[package_name.lower()],
        )
        chunks.append(chunk)

    # Always emit a package-level chunk too — useful for "what does DBMS_STATS do?"
    if pkg_desc:
        safe_pkg = re.sub(r"[^A-Za-z0-9_$.]", "_", package_name)
        pkg_chunk = DocChunk(
            id=f"{version}__{safe_pkg}__pkg",
            name=package_name,
            object_type="plsql_package",
            oracle_version=version,
            doc_type="plsql_packages",
            parent=None,
            category=None,
            description=pkg_desc,
            columns=[],
            parameters=[],
            return_type=None,
            syntax=None,
            usage_notes="",
            source_file=str(html_path.name),
            source_url=f"file://{html_path}",
            tags=[package_name.lower()],
        )
        chunks.insert(0, pkg_chunk)

    return chunks


# ---------------------------------------------------------------------------
# Crawler: walk a directory tree of HTML files
# ---------------------------------------------------------------------------

def detect_doctype(path: Path) -> Optional[str]:
    """
    Heuristic: guess doc type from directory name or filename patterns.
    Returns 'database_reference', 'plsql_packages', or None.
    """
    parts = path.parts
    p = " ".join(parts).lower()
    if any(x in p for x in ("refrn", "database_reference", "dbref", "data_dict")):
        return "database_reference"
    if any(x in p for x in ("arpls", "plsql_packages", "plsql-packages", "packages_reference")):
        return "plsql_packages"
    # Fall back to content sniff
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")[:2000]
        if re.search(r"DBA_|ALL_|USER_|V\$", text):
            return "database_reference"
        if re.search(r"DBMS_|UTL_|procedure|function", text, re.IGNORECASE):
            return "plsql_packages"
    except Exception:
        pass
    return None


def crawl(
    start_path: Path,
    version: str,
    doctype: str,
    max_files: Optional[int] = None,
) -> list[DocChunk]:
    """
    Recursively find HTML files under start_path and parse them.
    doctype: 'database_reference' | 'plsql_packages' | 'all'
    """
    all_chunks: list[DocChunk] = []
    html_files = sorted(start_path.rglob("*.htm")) + sorted(start_path.rglob("*.html"))

    if max_files:
        html_files = html_files[:max_files]

    log.info(f"Found {len(html_files)} HTML files under {start_path}")

    for i, html_file in enumerate(html_files, 1):
        detected = detect_doctype(html_file)
        effective_type = doctype if doctype != "all" else detected

        if effective_type is None:
            log.debug(f"[{i}/{len(html_files)}] Skipping (unknown doctype): {html_file.name}")
            continue

        log.info(f"[{i}/{len(html_files)}] Parsing [{effective_type}]: {html_file.name}")
        try:
            if effective_type == "database_reference":
                chunks = parse_database_reference_page(html_file, version)
            elif effective_type == "plsql_packages":
                chunks = parse_plsql_packages_page(html_file, version)
            else:
                continue

            log.info(f"  → {len(chunks)} chunk(s)")
            all_chunks.extend(chunks)
        except Exception as e:
            log.warning(f"  ✗ Error parsing {html_file.name}: {e}")

    return all_chunks


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_jsonl(chunks: list[DocChunk], out_dir: Path) -> Path:
    out_file = out_dir / "oracle_docs.jsonl"
    with out_file.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(asdict(chunk), ensure_ascii=False) + "\n")
    log.info(f"Wrote {len(chunks)} records to {out_file}")
    return out_file


def write_markdown_files(chunks: list[DocChunk], out_dir: Path) -> None:
    md_dir = out_dir / "markdown"
    md_dir.mkdir(parents=True, exist_ok=True)
    for chunk in chunks:
        safe = re.sub(r"[^A-Za-z0-9_.$-]", "_", chunk.id)
        path = md_dir / f"{safe}.md"
        path.write_text(chunk.to_markdown(), encoding="utf-8")
    log.info(f"Wrote {len(chunks)} Markdown files to {md_dir}")


def write_sqlite(chunks: list[DocChunk], out_dir: Path) -> Path:
    db_path = out_dir / "oracle_docs.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS chunks (
            id              TEXT PRIMARY KEY,
            name            TEXT NOT NULL,
            object_type     TEXT,
            oracle_version  TEXT,
            doc_type        TEXT,
            parent          TEXT,
            category        TEXT,
            description     TEXT,
            columns_json    TEXT,
            parameters_json TEXT,
            return_type     TEXT,
            syntax          TEXT,
            usage_notes     TEXT,
            source_file     TEXT,
            source_url      TEXT,
            tags_json       TEXT,
            column_names    TEXT,
            param_names     TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_name    ON chunks(name);
        CREATE INDEX IF NOT EXISTS idx_version ON chunks(oracle_version);
        CREATE INDEX IF NOT EXISTS idx_type    ON chunks(object_type);
        CREATE INDEX IF NOT EXISTS idx_parent  ON chunks(parent);

        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
            name,
            description,
            column_names,
            param_names,
            usage_notes,
            content='chunks',
            content_rowid='rowid'
        );
    """)

    for chunk in chunks:
        # Flat space-separated column/param names for FTS — makes
        # "num_rows blocks" match DBA_TABLES even if not in description
        column_names = " ".join(c["name"] for c in chunk.columns)
        param_names  = " ".join(p["name"] for p in chunk.parameters)

        cur.execute("""
            INSERT OR REPLACE INTO chunks VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, (
            chunk.id, chunk.name, chunk.object_type, chunk.oracle_version,
            chunk.doc_type, chunk.parent, chunk.category, chunk.description,
            json.dumps(chunk.columns), json.dumps(chunk.parameters),
            chunk.return_type, chunk.syntax, chunk.usage_notes,
            chunk.source_file, chunk.source_url, json.dumps(chunk.tags),
            column_names, param_names,
        ))

    # Rebuild FTS index
    cur.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
    con.commit()
    con.close()
    log.info(f"Wrote {len(chunks)} rows to SQLite: {db_path}")
    return db_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Parse local Oracle HTML docs into RAG-ready chunks.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--path", required=True,
        help="Root directory of local Oracle docs (file:// base path)",
    )
    parser.add_argument(
        "--version", required=True,
        help="Oracle version tag, e.g. 19c, 21c, 23ai",
    )
    parser.add_argument(
        "--doctype", default="all",
        choices=["database_reference", "plsql_packages", "all"],
        help="Which doc type to parse (default: all)",
    )
    parser.add_argument(
        "--output", default="./output",
        help="Output directory (default: ./output)",
    )
    parser.add_argument(
        "--max-files", type=int, default=None,
        help="Limit number of HTML files (useful for testing)",
    )
    parser.add_argument(
        "--no-jsonl", action="store_true", help="Skip JSONL output",
    )
    parser.add_argument(
        "--no-markdown", action="store_true", help="Skip Markdown output",
    )
    parser.add_argument(
        "--no-sqlite", action="store_true", help="Skip SQLite output",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    start_path = Path(args.path).expanduser().resolve()
    if not start_path.exists():
        log.error(f"Path does not exist: {start_path}")
        sys.exit(1)

    out_dir = Path(args.output).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    log.info(f"Starting crawl: {start_path}  version={args.version}  doctype={args.doctype}")
    chunks = crawl(start_path, args.version, args.doctype, args.max_files)

    if not chunks:
        log.warning("No chunks extracted. Check --path and --doctype.")
        sys.exit(0)

    log.info(f"Total chunks extracted: {len(chunks)}")

    if not args.no_jsonl:
        write_jsonl(chunks, out_dir)
    if not args.no_markdown:
        write_markdown_files(chunks, out_dir)
    if not args.no_sqlite:
        write_sqlite(chunks, out_dir)

    log.info("Done.")


if __name__ == "__main__":
    main()
