---
id: 19c__DBMS_INMEMORY.POPULATE
name: DBMS_INMEMORY.POPULATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_INMEMORY
tags: [dbms_inmemory]
source_file: DBMS_INMEMORY.html
---

# DBMS_INMEMORY.POPULATE

This procedure forces population of the specified table, partition, or subpartition into the IM column store.

## Syntax

```sql
DBMS_INMEMORY.POPULATE(
   schema_name      IN    VARCHAR2,
   table_name       IN    VARCHAR2,
   subobject_name   IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of schema |
| table_name | VARCHAR2 | IN | Name of table |
| subobject_name | VARCHAR2 | IN | Partition or subpartition |

## Usage Notes

Syntax DBMS_INMEMORY.POPULATE( schema_name IN VARCHAR2, table_name IN VARCHAR2, subobject_name IN VARCHAR2 DEFAULT NULL); Parameters Table 89-3 POPULATE Procedure Parameters Parameter Description schema_name Name of schema table_name Name of table subobject_name Partition or subpartition