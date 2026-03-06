---
id: 19c__DBA_DML_LOCKS
name: DBA_DML_LOCKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DML_LOCKS.html
---

# DBA_DML_LOCKS

DBA_DML_LOCKS lists all DML locks held in the database and all outstanding requests for a DML lock.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER | Session holding or acquiring the lock |
| OWNER | VARCHAR2(128) | Owner of the lock |
| NAME | VARCHAR2(128) | Name of the lock |
| MODE_HELD | VARCHAR2(13) | The type of lock held. The values are: ROWS_S ( SS ): row share lock ROW-X ( SX ): row exclusive lock SHARE ( S ): share lock S/ROW-X ( SSX ): exclusive lock NONE : lock requested but not yet obtained |
| MODE_REQUESTED | VARCHAR2(13) | Lock request type. The values are: ROWS_S ( SS ): row share lock ROW-X ( SX ): row exclusive lock SHARE ( S ): share lock S/ROW-X ( SSX ): exclusive lock NONE : Lock identifier obtained; lock not held or requested |
| LAST_CONVERT | NUMBER | Time since current mode was granted |
| BLOCKING_OTHERS | VARCHAR2(40) | Blocking others |

## Usage Notes

See Also: Oracle Database Concepts for more information about lock modes for table locks See Also: Oracle Database Concepts for more information about lock modes for table locks