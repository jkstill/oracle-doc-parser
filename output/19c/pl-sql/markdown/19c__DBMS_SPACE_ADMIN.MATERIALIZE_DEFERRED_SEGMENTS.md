---
id: 19c__DBMS_SPACE_ADMIN.MATERIALIZE_DEFERRED_SEGMENTS
name: DBMS_SPACE_ADMIN.MATERIALIZE_DEFERRED_SEGMENTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.MATERIALIZE_DEFERRED_SEGMENTS

This procedure materializes segments for tables and table fragments with deferred segment creation and their dependent objects.

## Syntax

```sql
DBMS_SPACE_ADMIN.MATERIALIZE_DEFERRED_SEGMENTS (
   schema_name       IN     VARCHAR2   DEFAULT NULL,
   table_name        IN     VARCHAR2   DEFAULT NULL,
   partition_name    IN     VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of schema |
| table_name | VARCHAR2 | IN | Name of table |
| partition_name | VARCHAR2 | IN | Name of partition |

## Usage Notes

Syntax DBMS_SPACE_ADMIN.MATERIALIZE_DEFERRED_SEGMENTS ( schema_name IN VARCHAR2 DEFAULT NULL, table_name IN VARCHAR2 DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 159-7 MATERIALIZE_DEFERRED_SEGMENTS Procedure Parameters Parameter Description schema_name Name of schema table_name Name of table partition_name Name of partition Usage Notes Given a schema name, this procedure scans all tables in the schema. For each table, if the deferred or delayed segment property is set for the table or any of its fragments, then a new segment is created for those fragments and their dependent objects. Optionally: No schema_name is specified, in which case tables belonging to all schemas are scanned Both schema_name and table_name are specified to perform the operation on a specified table All three arguments are supplied, restricting the operation to the partition and its dependent objects