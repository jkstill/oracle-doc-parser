---
id: 19c__DBA_WORKLOAD_SQL_MAP
name: DBA_WORKLOAD_SQL_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_WORKLOAD_SQL_MAP.html
---

# DBA_WORKLOAD_SQL_MAP

DBA_WORKLOAD_SQL_MAP contains the mapping information for skipping or replacing a SQL statement based on its sql_id during workload replay.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPLAY_ID | NUMBER(38) | A foreign key to the ID column in the DBA_WORKLOAD_REPLAYs view |
| SCHEDULE_CAP_ID | NUMBER(38) | The ID of a capture in the schedule |
| SQL_ID | VARCHAR2(13) | SQL identifier of the SQL statement at the time of capture |
| OPERATION | VARCHAR2(7) | SKIP or REPLACE |
| SQL_ID_NUMBER | NUMBER | Internal representation of SQL_ID |
| REPLACEMENT_SQL_TEXT | VARCHAR2(4000) | When the value in the OPERATION column is SKIP , this column is NULL. When the value in the OPERATION column is REPLACE , this column shows the SQL statement to be used. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content