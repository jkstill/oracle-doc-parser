---
id: 19c__ALL_REPL_DBNAME_MAPPING
name: ALL_REPL_DBNAME_MAPPING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_REPL_DBNAME_MAPPING.html
---

# ALL_REPL_DBNAME_MAPPING

ALL_REPL_DBNAME_MAPPING provides details about the database name mapping in replication for the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_ROOT_NAME | VARCHAR2(128) | The fully qualified global name of the root in a multitenant container database (CDB) where the changes originated |
| SOURCE_DATABASE_NAME | VARCHAR2(128) | The fully qualified global name of the pluggable database (PDB) where the changes originated |
| SOURCE_CONTAINER_NAME | VARCHAR2(128) | The container name of the database where the changes originated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_REPL_DBNAME_MAPPING provides details about the database name mapping in replication. See Also: " DBA_REPL_DBNAME_MAPPING " See Also: " DBA_REPL_DBNAME_MAPPING "