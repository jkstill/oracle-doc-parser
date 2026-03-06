---
id: 19c__DBMS_PART.CLEANUP_GIDX
name: DBMS_PART.CLEANUP_GIDX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PART
tags: [dbms_part]
source_file: DBMS_PART.html
---

# DBMS_PART.CLEANUP_GIDX

As a consequence of prior partition maintenance operations with asynchronous global index maintenance, global indexes can contain entries pointing to data segments that no longer exist. These stale index rows will not cause any correctness issues or corruptions during any operation on the table or index, whether these are queries, DMLs, DDLs or analyze. This procedure will identify and cleanup these global indexes to ensure efficiency in terms of storage and performance.

## Syntax

```sql
DBMS_PART.CLEANUP_GIDX (
   schema_name_in    IN   VARCHAR2 DEFAULT NULL,
   table_name_in     IN   VARCHAR2 DEFAULT NULL,
   parallel          IN   VARCHAR2 DEFAULT NULL,
   options           IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name_in | VARCHAR2 | IN | Non- NULL processes only indexes on tables in the given schema |
| table_name_in | VARCHAR2 | IN | Non- NULL processes only indexes on the given table in the given schema ( schema_name_in must be non- NULL if table_name_in is non- NULL ) |
| parallel | VARCHAR2 | IN | The parallel degree to use for the ALTER INDEX DDLs. |
| options | VARCHAR2 | IN | The following options are supported: CLEANUP_ORPHANS : implies that 'cleanup only' mechanism is used. COALESCE : implies that 'coalesce cleanup' mechanism is used. |

## Usage Notes

Syntax DBMS_PART.CLEANUP_GIDX ( schema_name_in IN VARCHAR2 DEFAULT NULL, table_name_in IN VARCHAR2 DEFAULT NULL, parallel IN VARCHAR2 DEFAULT NULL, options IN VARCHAR2 DEFAULT NULL); Parameters Table 122-2 CLEANUP_GIDX Function Parameters Parameter Description schema_name_in Non- NULL processes only indexes on tables in the given schema table_name_in Non- NULL processes only indexes on the given table in the given schema ( schema_name_in must be non- NULL if table_name_in is non- NULL ) parallel The parallel degree to use for the ALTER INDEX DDLs. options The following options are supported: CLEANUP_ORPHANS : implies that 'cleanup only' mechanism is used. COALESCE : implies that 'coalesce cleanup' mechanism is used.