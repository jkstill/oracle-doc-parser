---
id: 19c__DBMS_SPACE_ADMIN.DROP_EMPTY_SEGMENTS
name: DBMS_SPACE_ADMIN.DROP_EMPTY_SEGMENTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.DROP_EMPTY_SEGMENTS

This procedures drops segments from empty tables or table fragments and dependent objects.

## Syntax

```sql
DBMS_SPACE_ADMIN.DROP_EMPTY_SEGMENTS (
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

Syntax DBMS_SPACE_ADMIN.DROP_EMPTY_SEGMENTS ( schema_name IN VARCHAR2 DEFAULT NULL, table_name IN VARCHAR2 DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 159-5 DROP_EMPTY_SEGMENTS Procedure Parameters Parameter Description schema_name Name of schema table_name Name of table partition_name Name of partition Usage Notes Given a schema name, this procedure scans all tables in the schema. For each table, if the table or any of its fragments are found to be empty, and the table satisfies certain criteria (restrictions being the same as those described in "Restrictions on Deferred Segment Creation" ), then the empty table fragment and associated index segments are dropped along with the corresponding LOB data and index segments. A subsequent insert creates segments with the same properties. Optionally: No schema_name is specified, in which case tables belonging to all schemas are scanned Both schema_name and table_name are specified to perform the operation on a specified table All three arguments are supplied, restricting the operation to the partition and its dependent objects