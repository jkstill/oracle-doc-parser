---
id: 19c__DBMS_REPAIR.REBUILD_FREELISTS
name: DBMS_REPAIR.REBUILD_FREELISTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR.REBUILD_FREELISTS

This procedure rebuilds the freelists for the specified object.

## Syntax

```sql
DBMS_REPAIR.REBUILD_FREELISTS (
   schema_name    IN VARCHAR2,   
   object_name    IN  VARCHAR2,
   partition_name IN VARCHAR2 DEFAULT NULL,
   object_type    IN BINARY_INTEGER DEFAULT TABLE_OBJECT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema name. |
| object_name | VARCHAR2 | IN | Name of the object whose freelists are to be rebuilt. |
| partition_name | VARCHAR2 | IN | Partition or subpartition name whose freelists are to be rebuilt. If this is a partitioned object, and partition_name is not specified, then all partitions and subpartitions are processed. If this is a partitioned object, and the specified partition contains subpartitions, then all subpartitions are processed. |
| object_type | BINARY_INTEGER | IN | Type of the object to be processed. This must be either TABLE_OBJECT (default) or INDEX_OBJECT . See " Constants " . |

## Usage Notes

All free blocks are placed on the master freelist. All other freelists are zeroed. If the object has multiple freelist groups, then the free blocks are distributed among all freelists, allocating to the different groups in round-robin fashion. Syntax DBMS_REPAIR.REBUILD_FREELISTS ( schema_name IN VARCHAR2, object_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL, object_type IN BINARY_INTEGER DEFAULT TABLE_OBJECT); Parameters Table 140-9 REBUILD_FREELISTS Procedure Parameters Parameter Description schema_name Schema name. object_name Name of the object whose freelists are to be rebuilt. partition_name Partition or subpartition name whose freelists are to be rebuilt. If this is a partitioned object, and partition_name is not specified, then all partitions and subpartitions are processed. If this is a partitioned object, and the specified partition contains subpartitions, then all subpartitions are processed. object_type Type of the object to be processed. This must be either TABLE_OBJECT (default) or INDEX_OBJECT . See " Constants " .