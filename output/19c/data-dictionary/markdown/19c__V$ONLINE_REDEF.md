---
id: 19c__V$ONLINE_REDEF
name: V$ONLINE_REDEF
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ONLINE_REDEF.html
---

# V$ONLINE_REDEF

V$ONLINE_REDEF provides information about the status of currently running online redefinitions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| REDEFINITION_ID | NUMBER |  |
| TABLE_OWNER | VARCHAR2(129) |  |
| ORIGINAL_TABLE_NAME | VARCHAR2(129) |  |
| INTERIM_TABLE_NAME | VARCHAR2(1024) |  |
| PARTITION_NAME | VARCHAR2(1024) |  |
| OPERATION | VARCHAR2(128) |  |
| SUBOPERATION | VARCHAR2(128) |  |
| DETAILED_MESSAGE | VARCHAR2(1024) |  |
| PROGRESS | VARCHAR2(128) |  |
| REFRESH_STATEMENT_SQL_ID | VARCHAR2(128) |  |
| REFRESH_STATEMENT | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content