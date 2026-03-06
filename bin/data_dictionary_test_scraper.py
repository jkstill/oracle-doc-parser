#!/usr/bin/env python3
"""
Quick test for the Oracle doc scraper using minimal synthetic HTML fixtures.
Run from the same directory as scraper.py:
    python test_scraper.py
"""

import json
import sqlite3
import sys
import tempfile
from pathlib import Path

# --- Synthetic HTML fixtures ---------------------------------------------------

DB_REF_HTML = """\
<!DOCTYPE html>
<html>
<head><title>DBA_SEGMENTS</title></head>
<body>
<article>
<header>
<h2 class="sect2" id="REFRN-GUID-xxx">
  <span class="enumeration_section">4.250 </span>DBA_SEGMENTS
</h2>
</header>
<div class="ind">
<p><code class="codeph">DBA_SEGMENTS</code> describes storage allocated for all segments in the database.</p>
<div class="tblformalwide">
<table class="FormalWide" border="1" width="100%">
<thead>
<tr>
  <th>Column</th><th>Datatype</th><th>NULL</th><th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><p><code class="codeph">OWNER</code></p></td>
  <td><p><code class="codeph">VARCHAR2(128)</code></p></td>
  <td><p></p></td>
  <td><p>Username of the segment owner</p></td>
</tr>
<tr>
  <td><p><code class="codeph">SEGMENT_NAME</code></p></td>
  <td><p><code class="codeph">VARCHAR2(128)</code></p></td>
  <td><p></p></td>
  <td><p>Name of the segment, if applicable</p></td>
</tr>
<tr>
  <td><p><code class="codeph">SEGMENT_TYPE</code></p></td>
  <td><p><code class="codeph">VARCHAR2(18)</code></p></td>
  <td><p></p></td>
  <td><p>Type of segment: TABLE, CLUSTER, INDEX, etc.</p></td>
</tr>
<tr>
  <td><p><code class="codeph">TABLESPACE_NAME</code></p></td>
  <td><p><code class="codeph">VARCHAR2(30)</code></p></td>
  <td><p></p></td>
  <td><p>Name of the tablespace containing the segment</p></td>
</tr>
<tr>
  <td><p><code class="codeph">BYTES</code></p></td>
  <td><p><code class="codeph">NUMBER</code></p></td>
  <td><p></p></td>
  <td><p>Size in bytes of the segment</p></td>
</tr>
<tr>
  <td><p><code class="codeph">BLOCKS</code></p></td>
  <td><p><code class="codeph">NUMBER</code></p></td>
  <td><p></p></td>
  <td><p>Size in Oracle blocks of the segment</p></td>
</tr>
</tbody>
</table>
</div>
<div class="infoboxnotealso">Note: On partitioned objects, this view shows statistics for individual partitions.</div>
</div>
</article>
</body>
</html>
"""

PLSQL_HTML = """\
<!DOCTYPE html>
<html>
<head><title>DBMS_STATS</title></head>
<body>
<article>
<header>
<h2 class="sect2" id="ARPLS-GUID-xxx">
  <span class="enumeration_chapter">42 </span>DBMS_STATS
</h2>
</header>
<div class="ind">
<p>The DBMS_STATS package provides a mechanism to view and modify optimizer statistics.</p>

<div class="props_rev_3">
  <h4 class="sect4"><span class="enumeration_section">42.1 </span>GATHER_TABLE_STATS Procedure</h4>
  <div>
    <p>Gathers table and column (and index) statistics for the specified table.</p>
    <pre class="oac_no_warn">DBMS_STATS.GATHER_TABLE_STATS (
   ownname          IN VARCHAR2,
   tabname          IN VARCHAR2,
   partname         IN VARCHAR2 DEFAULT NULL,
   estimate_percent IN NUMBER   DEFAULT DBMS_STATS.AUTO_SAMPLE_SIZE,
   cascade          IN BOOLEAN  DEFAULT DBMS_STATS.AUTO_CASCADE
);</pre>
    <table class="Formal" border="1" width="100%">
      <thead><tr><th>Parameter</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td><p>ownname</p></td><td><p>Name of the schema user</p></td></tr>
        <tr><td><p>tabname</p></td><td><p>Name of the table</p></td></tr>
        <tr><td><p>partname</p></td><td><p>Name of the partition (optional)</p></td></tr>
        <tr><td><p>estimate_percent</p></td><td><p>Percentage of rows to estimate</p></td></tr>
        <tr><td><p>cascade</p></td><td><p>Gather index statistics as well</p></td></tr>
      </tbody>
    </table>
    <div class="infoboxnotealso">Note: Setting estimate_percent to AUTO_SAMPLE_SIZE is recommended.</div>
  </div>
</div>

<div class="props_rev_3">
  <h4 class="sect4"><span class="enumeration_section">42.2 </span>GET_TABLE_STATS Function</h4>
  <div>
    <p>Returns table statistics for the specified table.</p>
    <pre class="oac_no_warn">DBMS_STATS.GET_TABLE_STATS (
   ownname     IN  VARCHAR2,
   tabname     IN  VARCHAR2,
   numrows     OUT NUMBER,
   numblks     OUT NUMBER
) RETURN BOOLEAN;</pre>
    <table class="Formal" border="1" width="100%">
      <thead><tr><th>Parameter</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td><p>ownname</p></td><td><p>Schema owner name</p></td></tr>
        <tr><td><p>tabname</p></td><td><p>Table name</p></td></tr>
        <tr><td><p>numrows</p></td><td><p>Number of rows in table</p></td></tr>
        <tr><td><p>numblks</p></td><td><p>Number of blocks</p></td></tr>
      </tbody>
    </table>
  </div>
</div>

</div>
</article>
</body>
</html>
"""

# -------------------------------------------------------------------------------

def run_tests():
    sys.path.insert(0, str(Path(__file__).parent))
    from data_dictionary_scraper import (
        parse_database_reference_page,
        parse_plsql_packages_page,
        write_jsonl, write_markdown_files, write_sqlite,
    )

    passed = 0
    failed = 0

    def ok(label):
        nonlocal passed
        print(f"  ✓ {label}")
        passed += 1

    def fail(label, reason):
        nonlocal failed
        print(f"  ✗ {label}: {reason}")
        failed += 1

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # Write fixtures
        db_ref_file = tmp / "refrn_dba_segments.htm"
        db_ref_file.write_text(DB_REF_HTML, encoding="utf-8")

        plsql_file = tmp / "arpls_dbms_stats.htm"
        plsql_file.write_text(PLSQL_HTML, encoding="utf-8")

        # -----------------------------------------------------------------------
        print("\n[1] Database Reference parsing")
        chunks = parse_database_reference_page(db_ref_file, "19c")

        if chunks:
            ok(f"Got {len(chunks)} chunk(s)")
        else:
            fail("chunk count", "expected ≥1 chunk")

        if chunks:
            c = chunks[0]
            if c.name == "DBA_SEGMENTS":
                ok(f"Name: {c.name}")
            else:
                fail("name", f"got {c.name!r}")

            if c.object_type == "data_dictionary_view":
                ok(f"object_type: {c.object_type}")
            else:
                fail("object_type", f"got {c.object_type!r}")

            if c.oracle_version == "19c":
                ok(f"oracle_version: {c.oracle_version}")
            else:
                fail("oracle_version", f"got {c.oracle_version!r}")

            if c.category == "storage":
                ok(f"category: {c.category}")
            else:
                fail("category", f"got {c.category!r}")

            if len(c.columns) >= 4:
                ok(f"columns: {len(c.columns)} extracted")
            else:
                fail("columns", f"got {len(c.columns)}, expected ≥4")

            col_names = [col["name"] for col in c.columns]
            if "OWNER" in col_names:
                ok("OWNER column present")
            else:
                fail("OWNER column", f"col_names={col_names}")

            if "dba" in c.tags:
                ok("tag 'dba' present")
            else:
                fail("tags", f"got {c.tags}")

            md = c.to_markdown()
            if "## Columns" in md and "| OWNER |" in md:
                ok("Markdown renders column table")
            else:
                fail("Markdown", "missing column table")

        # -----------------------------------------------------------------------
        print("\n[2] PL/SQL Packages parsing")
        chunks = parse_plsql_packages_page(plsql_file, "19c")

        # First chunk is the package-level chunk, then subprograms
        if len(chunks) >= 3:
            ok(f"Got {len(chunks)} chunk(s) (1 package + subprograms)")
        else:
            fail("chunk count", f"got {len(chunks)}, expected ≥3 (1 package + 2 subprograms)")

        pkg_chunk = next((c for c in chunks if c.object_type == "plsql_package"), None)
        if pkg_chunk:
            ok(f"Package-level chunk: {pkg_chunk.name}")
            if pkg_chunk.parent is None:
                ok("Package chunk has no parent")
            else:
                fail("package parent", f"expected None, got {pkg_chunk.parent!r}")
        else:
            fail("plsql_package chunk", "not found")

        gather = next((c for c in chunks if "GATHER_TABLE_STATS" in c.name), None)
        if gather:
            ok(f"GATHER_TABLE_STATS chunk found: {gather.name}")

            if gather.parent == "DBMS_STATS":
                ok(f"parent: {gather.parent}")
            else:
                fail("parent", f"got {gather.parent!r}")

            if len(gather.parameters) >= 3:
                ok(f"parameters: {len(gather.parameters)} extracted")
            else:
                fail("parameters", f"got {len(gather.parameters)}")

            if gather.syntax and "GATHER_TABLE_STATS" in gather.syntax:
                ok("syntax block captured")
            else:
                syntax_preview = repr(gather.syntax)[:80]
                fail("syntax", f"got {syntax_preview}")

            if gather.object_type == "plsql_procedure":
                ok(f"object_type: {gather.object_type}")
            else:
                fail("object_type", f"got {gather.object_type!r}")
        else:
            fail("GATHER_TABLE_STATS", "chunk not found")

        get_stats = next((c for c in chunks if "GET_TABLE_STATS" in c.name), None)
        if get_stats:
            if get_stats.object_type in ("plsql_function", "plsql_subprogram"):
                ok(f"GET_TABLE_STATS type: {get_stats.object_type}")
            else:
                fail("GET_TABLE_STATS type", f"got {get_stats.object_type!r}")
            if get_stats.return_type:
                ok(f"return_type captured: {get_stats.return_type}")
            else:
                fail("return_type", "expected a value, got None")
        else:
            fail("GET_TABLE_STATS", "chunk not found")

        # -----------------------------------------------------------------------
        print("\n[3] Output writers")
        all_chunks = []
        all_chunks += parse_database_reference_page(db_ref_file, "19c")
        all_chunks += parse_plsql_packages_page(plsql_file, "19c")

        out_dir = tmp / "output"
        out_dir.mkdir()

        # JSONL
        jsonl_path = write_jsonl(all_chunks, out_dir)
        lines = jsonl_path.read_text().strip().splitlines()
        if len(lines) == len(all_chunks):
            ok(f"JSONL: {len(lines)} lines")
        else:
            fail("JSONL line count", f"expected {len(all_chunks)}, got {len(lines)}")
        try:
            obj = json.loads(lines[0])
            if "id" in obj and "columns" in obj:
                ok("JSONL schema valid (id + columns present)")
            else:
                fail("JSONL schema", f"keys={list(obj.keys())}")
        except Exception as e:
            fail("JSONL parse", str(e))

        # Markdown
        write_markdown_files(all_chunks, out_dir)
        md_files = list((out_dir / "markdown").glob("*.md"))
        if len(md_files) == len(all_chunks):
            ok(f"Markdown: {len(md_files)} files")
        else:
            fail("Markdown file count", f"expected {len(all_chunks)}, got {len(md_files)}")

        # SQLite
        db_path = write_sqlite(all_chunks, out_dir)
        con = sqlite3.connect(db_path)
        row_count = con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        if row_count == len(all_chunks):
            ok(f"SQLite: {row_count} rows")
        else:
            fail("SQLite row count", f"expected {len(all_chunks)}, got {row_count}")

        fts_results = con.execute(
            "SELECT name FROM chunks_fts WHERE chunks_fts MATCH 'storage'"
        ).fetchall()
        if fts_results:
            ok(f"FTS5 search works: found {len(fts_results)} result(s) for 'storage'")
        else:
            fail("FTS5 search", "no results for 'storage'")

        con.close()

    # Summary
    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed:
        sys.exit(1)
    else:
        print("All tests passed ✓")


if __name__ == "__main__":
    run_tests()
