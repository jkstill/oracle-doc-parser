---
id: 19c__DBA_DDL_LOCKS
name: DBA_DDL_LOCKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DDL_LOCKS.html
---

# DBA_DDL_LOCKS

DBA_DDL_LOCKS lists all DDL locks held in the database and all outstanding requests for a DDL lock.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER | Session identifier |
| OWNER | VARCHAR2(128) | Owner of the lock |
| NAME | VARCHAR2(1000) | Name of the lock |
| TYPE | VARCHAR2(40) | Lock type: Cursor Table/Procedure/Type Body Trigger Index Cluster Java Source Java Resource Java Data |
| MODE_HELD | VARCHAR2(9) | Lock mode: None Null Share Exclusive |
| MODE_REQUESTED | VARCHAR2(9) | Lock request type: None Null Share Exclusive |

## Usage Notes

See Also: Oracle Database Concepts for more information about DDL locks See Also: Oracle Database Concepts for more information about DDL locks