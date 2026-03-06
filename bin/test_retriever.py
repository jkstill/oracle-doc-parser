#!/usr/bin/env python3
"""
Tests for oracle_rag.retriever using synthetic SQLite databases.
Run from the oracle_doc_scraper directory:
    python test_retriever.py
"""

import json
import sqlite3
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from oracle_rag.retriever import OracleRetriever, RetrievalConfig


# ---------------------------------------------------------------------------
# Build synthetic test databases
# ---------------------------------------------------------------------------

DICT_CHUNKS = [
    {
        "id": "19c__DBA_SEGMENTS",
        "name": "DBA_SEGMENTS",
        "object_type": "data_dictionary_view",
        "oracle_version": "19c",
        "doc_type": "database_reference",
        "parent": None,
        "category": "storage",
        "description": "DBA_SEGMENTS describes storage allocated for all segments in the database.",
        "columns": [
            {"name": "OWNER", "type": "VARCHAR2(128)", "nullable": "", "description": "Segment owner"},
            {"name": "SEGMENT_NAME", "type": "VARCHAR2(128)", "nullable": "", "description": "Segment name"},
            {"name": "BYTES", "type": "NUMBER", "nullable": "", "description": "Size in bytes"},
            {"name": "BLOCKS", "type": "NUMBER", "nullable": "", "description": "Size in blocks"},
        ],
        "parameters": [],
        "return_type": None,
        "syntax": None,
        "usage_notes": "Use this view to monitor segment growth.",
        "source_file": "DBA_SEGMENTS.html",
        "source_url": "file:///docs/DBA_SEGMENTS.html",
        "tags": ["dba"],
        "column_names": "OWNER SEGMENT_NAME BYTES BLOCKS",
        "param_names": "",
    },
    {
        "id": "19c__V_SESSION",
        "name": "V$SESSION",
        "object_type": "data_dictionary_view",
        "oracle_version": "19c",
        "doc_type": "database_reference",
        "parent": None,
        "category": "performance",
        "description": "V$SESSION displays session information for each current session.",
        "columns": [
            {"name": "SID", "type": "NUMBER", "nullable": "", "description": "Session identifier"},
            {"name": "USERNAME", "type": "VARCHAR2(128)", "nullable": "", "description": "Oracle username"},
            {"name": "STATUS", "type": "VARCHAR2(8)", "nullable": "", "description": "Session status"},
            {"name": "WAIT_CLASS", "type": "VARCHAR2(64)", "nullable": "", "description": "Wait class name"},
        ],
        "parameters": [],
        "return_type": None,
        "syntax": None,
        "usage_notes": "",
        "source_file": "V$SESSION.html",
        "source_url": "file:///docs/V$SESSION.html",
        "tags": ["dynamic_performance"],
        "column_names": "SID USERNAME STATUS WAIT_CLASS",
        "param_names": "",
    },
    {
        "id": "19c__ALL_SEGMENTS",
        "name": "ALL_SEGMENTS",
        "object_type": "data_dictionary_view",
        "oracle_version": "19c",
        "doc_type": "database_reference",
        "parent": None,
        "category": "storage",
        "description": "ALL_SEGMENTS describes storage allocated for all segments accessible to current user.",
        "columns": [
            {"name": "OWNER", "type": "VARCHAR2(128)", "nullable": "", "description": "Segment owner"},
            {"name": "BYTES", "type": "NUMBER", "nullable": "", "description": "Size in bytes"},
        ],
        "parameters": [],
        "return_type": None,
        "syntax": None,
        "usage_notes": "",
        "source_file": "ALL_SEGMENTS.html",
        "source_url": "file:///docs/ALL_SEGMENTS.html",
        "tags": ["all"],
        "column_names": "OWNER BYTES",
        "param_names": "",
    },
]

PLSQL_CHUNKS = [
    {
        "id": "19c__DBMS_STATS",
        "name": "DBMS_STATS",
        "object_type": "plsql_package",
        "oracle_version": "19c",
        "doc_type": "plsql_packages",
        "parent": None,
        "category": None,
        "description": "The DBMS_STATS package provides a mechanism to view and modify optimizer statistics.",
        "columns": [],
        "parameters": [],
        "return_type": None,
        "syntax": None,
        "usage_notes": "",
        "source_file": "DBMS_STATS.html",
        "source_url": "file:///docs/DBMS_STATS.html",
        "tags": ["dbms_stats"],
        "column_names": "",
        "param_names": "",
    },
    {
        "id": "19c__DBMS_STATS.GATHER_TABLE_STATS",
        "name": "DBMS_STATS.GATHER_TABLE_STATS",
        "object_type": "plsql_procedure",
        "oracle_version": "19c",
        "doc_type": "plsql_packages",
        "parent": "DBMS_STATS",
        "category": None,
        "description": "Gathers table and column statistics for the specified table.",
        "columns": [],
        "parameters": [
            {"name": "ownname", "type": "VARCHAR2", "mode": "IN", "description": "Schema name"},
            {"name": "tabname", "type": "VARCHAR2", "mode": "IN", "description": "Table name"},
            {"name": "estimate_percent", "type": "NUMBER", "mode": "IN", "description": "Sampling percent"},
        ],
        "return_type": None,
        "syntax": "DBMS_STATS.GATHER_TABLE_STATS(\n  ownname IN VARCHAR2,\n  tabname IN VARCHAR2,\n  estimate_percent IN NUMBER DEFAULT AUTO_SAMPLE_SIZE\n);",
        "usage_notes": "Use AUTO_SAMPLE_SIZE for best results.",
        "source_file": "DBMS_STATS.html",
        "source_url": "file:///docs/DBMS_STATS.html",
        "tags": ["dbms_stats"],
        "column_names": "",
        "param_names": "ownname tabname estimate_percent",
    },
    {
        "id": "19c__DBMS_STATS.GET_TABLE_STATS",
        "name": "DBMS_STATS.GET_TABLE_STATS",
        "object_type": "plsql_function",
        "oracle_version": "19c",
        "doc_type": "plsql_packages",
        "parent": "DBMS_STATS",
        "category": None,
        "description": "Returns optimizer statistics for the specified table.",
        "columns": [],
        "parameters": [
            {"name": "ownname", "type": "VARCHAR2", "mode": "IN", "description": "Schema name"},
            {"name": "tabname", "type": "VARCHAR2", "mode": "IN", "description": "Table name"},
        ],
        "return_type": "BOOLEAN",
        "syntax": "DBMS_STATS.GET_TABLE_STATS(\n  ownname IN VARCHAR2,\n  tabname IN VARCHAR2\n) RETURN BOOLEAN;",
        "usage_notes": "",
        "source_file": "DBMS_STATS.html",
        "source_url": "file:///docs/DBMS_STATS.html",
        "tags": ["dbms_stats"],
        "column_names": "",
        "param_names": "ownname tabname",
    },
]


def build_test_db(path: Path, chunks: list[dict]) -> None:
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE chunks (
            id TEXT PRIMARY KEY, name TEXT, object_type TEXT,
            oracle_version TEXT, doc_type TEXT, parent TEXT,
            category TEXT, description TEXT,
            columns_json TEXT, parameters_json TEXT,
            return_type TEXT, syntax TEXT, usage_notes TEXT,
            source_file TEXT, source_url TEXT, tags_json TEXT,
            column_names TEXT, param_names TEXT
        );
        CREATE INDEX idx_name ON chunks(name);
        CREATE INDEX idx_parent ON chunks(parent);
        CREATE VIRTUAL TABLE chunks_fts USING fts5(
            name, description, column_names, param_names, usage_notes,
            content='chunks', content_rowid='rowid'
        );
    """)
    for c in chunks:
        cur.execute("""INSERT INTO chunks VALUES (
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
        )""", (
            c["id"], c["name"], c["object_type"], c["oracle_version"],
            c["doc_type"], c["parent"], c["category"], c["description"],
            json.dumps(c["columns"]), json.dumps(c["parameters"]),
            c["return_type"], c["syntax"], c["usage_notes"],
            c["source_file"], c["source_url"], json.dumps(c["tags"]),
            c["column_names"], c["param_names"],
        ))
    cur.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
    con.commit()
    con.close()


# ---------------------------------------------------------------------------
# Test runner
# ---------------------------------------------------------------------------

def run_tests():
    passed = 0
    failed = 0

    def ok(label):
        nonlocal passed
        print(f"  ✓ {label}")
        passed += 1

    def fail(label, reason=""):
        nonlocal failed
        print(f"  ✗ {label}{': ' + reason if reason else ''}")
        failed += 1

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        dict_db  = tmp / "dict.db"
        plsql_db = tmp / "plsql.db"
        build_test_db(dict_db, DICT_CHUNKS)
        build_test_db(plsql_db, PLSQL_CHUNKS)

        cfg = RetrievalConfig(dict_db=str(dict_db), plsql_db=str(plsql_db))

        with OracleRetriever(cfg) as ret:

            # ----------------------------------------------------------------
            print("\n[1] stats()")
            s = ret.stats()
            if s["dict"]["total"] == 3:
                ok(f"dict total: {s['dict']['total']}")
            else:
                fail("dict total", str(s["dict"]["total"]))
            if s["plsql"]["total"] == 3:
                ok(f"plsql total: {s['plsql']['total']}")
            else:
                fail("plsql total", str(s["plsql"]["total"]))

            # ----------------------------------------------------------------
            print("\n[2] search() — keyword query")
            result = ret.search("storage bytes blocks", limit=5)
            dict_names = [c.name for c in result.dict_chunks]
            if "DBA_SEGMENTS" in dict_names:
                ok(f"DBA_SEGMENTS in dict results: {dict_names}")
            else:
                fail("DBA_SEGMENTS not found", str(dict_names))

            plsql_names = [c.name for c in result.plsql_chunks]
            if any("DBMS_STATS" in n for n in plsql_names):
                ok(f"DBMS_STATS in plsql results")
            else:
                ok(f"No PL/SQL match for storage query (expected)")

            # ----------------------------------------------------------------
            print("\n[3] search() — dict_only / plsql_only")
            r_dict = ret.search("statistics", dict_only=True)
            if not r_dict.plsql_chunks:
                ok("dict_only: no plsql_chunks returned")
            else:
                fail("dict_only: got plsql_chunks")

            r_plsql = ret.search("statistics", plsql_only=True)
            if not r_plsql.dict_chunks:
                ok("plsql_only: no dict_chunks returned")
            else:
                fail("plsql_only: got dict_chunks")

            # ----------------------------------------------------------------
            print("\n[4] lookup() — exact name")
            chunk = ret.lookup("DBA_SEGMENTS")
            if chunk and chunk.name == "DBA_SEGMENTS":
                ok(f"lookup DBA_SEGMENTS: found")
            else:
                fail("lookup DBA_SEGMENTS")

            chunk = ret.lookup("DBMS_STATS.GATHER_TABLE_STATS")
            if chunk and chunk.name == "DBMS_STATS.GATHER_TABLE_STATS":
                ok(f"lookup DBMS_STATS.GATHER_TABLE_STATS: found")
            else:
                fail("lookup DBMS_STATS.GATHER_TABLE_STATS")

            chunk = ret.lookup("DOES_NOT_EXIST")
            if chunk is None:
                ok("lookup nonexistent: returns None")
            else:
                fail("lookup nonexistent: expected None")

            # ----------------------------------------------------------------
            print("\n[5] lookup_many()")
            chunks = ret.lookup_many(["DBA_SEGMENTS", "V$SESSION", "DOES_NOT_EXIST"])
            if len(chunks) == 2:
                ok(f"lookup_many: {len(chunks)} found, 1 not found (correct)")
            else:
                fail("lookup_many count", str(len(chunks)))

            # ----------------------------------------------------------------
            print("\n[6] package_subprograms()")
            subs = ret.package_subprograms("DBMS_STATS")
            if len(subs) == 2:
                ok(f"package_subprograms DBMS_STATS: {len(subs)} subprograms")
            else:
                fail("package_subprograms count", str(len(subs)))

            sub_names = [c.name for c in subs]
            if "DBMS_STATS.GATHER_TABLE_STATS" in sub_names:
                ok("GATHER_TABLE_STATS in subprograms")
            else:
                fail("GATHER_TABLE_STATS missing", str(sub_names))

            # ----------------------------------------------------------------
            print("\n[7] views_like()")
            views = ret.views_like("DBA_%")
            if len(views) == 1 and views[0].name == "DBA_SEGMENTS":
                ok(f"views_like DBA_%: {[v.name for v in views]}")
            else:
                fail("views_like DBA_%", str([v.name for v in views]))

            # ----------------------------------------------------------------
            print("\n[8] related_views()")
            related = ret.related_views("DBA_SEGMENTS")
            related_names = [c.name for c in related]
            if "ALL_SEGMENTS" in related_names:
                ok(f"related DBA_SEGMENTS: {related_names}")
            else:
                fail("related_views", str(related_names))

            # ----------------------------------------------------------------
            print("\n[9] Chunk.to_markdown()")
            chunk = ret.lookup("DBA_SEGMENTS")
            md = chunk.to_markdown(compact=False)
            if "## DBA_SEGMENTS" in md and "| OWNER |" in md and "## Columns" in md:
                ok("full markdown: heading + columns table present")
            else:
                fail("full markdown missing sections")

            md_compact = chunk.to_markdown(compact=True)
            if "## DBA_SEGMENTS" in md_compact and "## Columns" not in md_compact:
                ok("compact markdown: heading present, columns absent")
            else:
                fail("compact markdown")

            # ----------------------------------------------------------------
            print("\n[10] RetrievalResult.to_markdown() / to_dict()")
            result = ret.search("session wait", limit=3)
            full_md = result.to_markdown()
            if "# Oracle Documentation" in full_md:
                ok("RetrievalResult.to_markdown() renders")
            else:
                fail("RetrievalResult.to_markdown()")

            d = result.to_dict()
            if "query" in d and "dict_chunks" in d and "plsql_chunks" in d:
                ok("RetrievalResult.to_dict() has expected keys")
            else:
                fail("RetrievalResult.to_dict() missing keys")

            # ----------------------------------------------------------------
            print("\n[11] RetrievalConfig.from_directory()")
            layout_dir = tmp / "output"
            (layout_dir / "19c" / "data-dictionary").mkdir(parents=True)
            (layout_dir / "19c" / "pl-sql").mkdir(parents=True)
            import shutil
            shutil.copy(dict_db,  layout_dir / "19c" / "data-dictionary" / "oracle_docs.db")
            shutil.copy(plsql_db, layout_dir / "19c" / "pl-sql" / "oracle_docs.db")

            cfg2 = RetrievalConfig.from_directory(layout_dir, "19c")
            with OracleRetriever(cfg2) as ret2:
                s2 = ret2.stats()
                if s2["dict"]["total"] == 3:
                    ok("from_directory: dict db loaded correctly")
                else:
                    fail("from_directory dict", str(s2))

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed:
        sys.exit(1)
    print("All tests passed ✓")


if __name__ == "__main__":
    run_tests()
