---
id: 19c__DBA_TS_QUOTAS
name: DBA_TS_QUOTAS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TS_QUOTAS.html
---

# DBA_TS_QUOTAS

DBA_TS_QUOTAS describes tablespace quotas for all users.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) | Tablespace name |
| USERNAME | VARCHAR2(128) | User with resource rights on the tablespace |
| BYTES | NUMBER | Number of bytes charged to the user |
| MAX_BYTES | NUMBER | User's quota in bytes, or -1 if no limit |
| BLOCKS | NUMBER | Number of Oracle blocks charged to the user |
| MAX_BLOCKS | NUMBER | User's quota in Oracle blocks, or -1 if no limit |
| DROPPED | VARCHAR2(3) | Whether the tablespace has been dropped |

## Usage Notes

Related View USER_TS_QUOTAS describes tablespace quotas for the current user. This view does not display the USERNAME column. See Also: " USER_TS_QUOTAS " See Also: " USER_TS_QUOTAS "