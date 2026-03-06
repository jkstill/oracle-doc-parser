---
id: 19c__DBA_SR_PARTN_OPS
name: DBA_SR_PARTN_OPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_SR_PARTN_OPS.html
---

# DBA_SR_PARTN_OPS

DBA_SR_PARTN_OPS provides information on the partition operations registered on the base tables of the materialized views registered for synchronous refresh.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the base table registered for synchronous refresh |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PARTITION_OP | VARCHAR2(128) | Type of partition operation: DROP EXCHANGE TRUNCATE |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition to be changed |
| OUTSIDE_TABLE_SCHEMA | VARCHAR2(128) | Schema in which the outside table (for EXCHANGE PARTITION ) was created |
| OUTSIDE_TABLE_NAME | VARCHAR2(128) | Name of the outside table (for EXCHANGE PARTITION ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content These rows last only as long as the registrations are active; that is, they disappear after EXECUTE_REFRESH or ABORT_REFRESH of the base table by the DBMS_SYNC_REFRESH package. Related View USER_SR_PARTN_OPS provides information on the partition operations registered on the base tables of the materialized views registered for synchronous refresh belonging to the current user. Its columns are the same as those in DBA_SR_PARTN_OPS . See Also: " USER_SR_PARTN_OPS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SYNC_REFRESH package