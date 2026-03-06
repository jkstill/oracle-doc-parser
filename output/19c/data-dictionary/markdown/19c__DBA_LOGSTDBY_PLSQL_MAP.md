---
id: 19c__DBA_LOGSTDBY_PLSQL_MAP
name: DBA_LOGSTDBY_PLSQL_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_LOGSTDBY_PLSQL_MAP.html
---

# DBA_LOGSTDBY_PLSQL_MAP

DBA_LOGSTDBY_PLSQL_MAP shows the mapping between a supported user invokable (/external) PL/SQL procedure to the corresponding replicated internal PL/SQL procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner name of the procedure |
| PKG_NAME | VARCHAR2(128) | Package name of the user invokable procedure |
| PROC_NAME | VARCHAR2(128) | Procedure name of the user invokable procedure |
| INTERNAL_PKG_NAME | VARCHAR2(128) | Package name of the internal procedure |
| INTERNAL_PROC_NAME | VARCHAR2(128) | Procedure name of the internal procedure |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: In a CDB, this view shows data when queried in the root or a PDB. Note: In a CDB, this view shows data when queried in the root or a PDB.