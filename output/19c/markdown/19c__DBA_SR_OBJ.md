---
id: 19c__DBA_SR_OBJ
name: DBA_SR_OBJ
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_SR_OBJ.html
---

# DBA_SR_OBJ

DBA_SR_OBJ provides information on the objects registered for synchronous refresh for current groups.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the synchronous refresh object |
| NAME | VARCHAR2(128) | Name of the synchronous refresh object |
| TYPE | VARCHAR2(5) | Type of synchronous refresh object: MVIEW TABLE |
| GROUP_ID | NUMBER | Group ID of the synchronous refresh group to which this object belongs |
| STAGING_LOG_NAME | VARCHAR2(128) | Name of the staging log for tables. This column has a value of NULL for materialized views. |

## Usage Notes

Related View USER_SR_OBJ provides information on the objects registered for synchronous refresh for current groups for the current user. Its columns are the same as those in DBA_SR_OBJ . See Also: " USER_SR_OBJ " See Also: " USER_SR_OBJ "