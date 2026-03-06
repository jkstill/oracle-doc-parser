---
id: 19c__V$DIAG_APP_TRACE_FILE
name: V$DIAG_APP_TRACE_FILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DIAG_APP_TRACE_FILE.html
---

# V$DIAG_APP_TRACE_FILE

V$DIAG_APP_TRACE_FILE contains information about all trace files present in the Automatic Diagnostic Repository (ADR) for the current container (PDB) which contain application trace data (SQL_TRACE or OPTIMIZER_TRACE event data). This view also supports GV$ global views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADR_HOME | VARCHAR2(444) |  |
| TRACE_FILENAME | VARCHAR2(68) |  |
| CHANGE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| MODIFY_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| SQL_TRACE | VARCHAR2(1) |  |
| OPTIMIZER_TRACE | VARCHAR2(1) |  |
| CON_ID | NUMBER |  |