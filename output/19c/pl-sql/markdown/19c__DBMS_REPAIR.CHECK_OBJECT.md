---
id: 19c__DBMS_REPAIR.CHECK_OBJECT
name: DBMS_REPAIR.CHECK_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR.CHECK_OBJECT

This procedure checks the specified objects and populates the repair table with information about corruptions and repair directives.

## Syntax

```sql
DBMS_REPAIR.CHECK_OBJECT (
   schema_name       IN  VARCHAR2,
   object_name       IN  VARCHAR2,
   partition_name    IN  VARCHAR2       DEFAULT NULL,
   object_type       IN  BINARY_INTEGER DEFAULT TABLE_OBJECT,
   repair_table_name IN  VARCHAR2       DEFAULT 'REPAIR_TABLE',
   flags             IN  BINARY_INTEGER DEFAULT NULL,
   relative_fno      IN  BINARY_INTEGER DEFAULT NULL,
   block_start       IN  BINARY_INTEGER DEFAULT NULL,
   block_end         IN  BINARY_INTEGER DEFAULT NULL,
   corrupt_count     OUT BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema name of the object to be checked. |
| object_name | VARCHAR2 | IN | Name of the table or index to be checked. |
| partition_name | VARCHAR2 | IN | Partition or subpartition name to be checked. If this is a partitioned object, and if partition_name is not specified, then all partitions and subpartitions are checked. If this is a partitioned object, and if the specified partition contains subpartitions, then all subpartitions are checked. |
| object_type | BINARY_INTEGER | IN | Type of the object to be processed. This must be either TABLE_OBJECT (default) or INDEX_OBJECT . See " Constants " . |
| repair_table_name | VARCHAR2 | IN | Name of the repair table to be populated. The table must exist in the SYS schema. Use the ADMIN_TABLES Procedure to create a repair table. The default name is REPAIR_TABLE . |
| flags | BINARY_INTEGER | IN | Reserved for future use. |
| relative_fno | BINARY_INTEGER | IN | Relative file number: Used when specifying a block range. |
| block_start | BINARY_INTEGER | IN | First block to process if specifying a block range. May be specified only if the object is a single table, partition, or subpartition. |
| block_end | BINARY_INTEGER | IN | Last block to process if specifying a block range. May be specified only if the object is a single table, partition, or subpartition. If only one of block_start or block_end is specified, then the other defaults to the first or last block in the file respectively. |
| corrupt_count | BINARY_INTEGER) | OUT | Number of corruptions reported. |

## Usage Notes

Validation consists of block checking all blocks in the object. Syntax DBMS_REPAIR.CHECK_OBJECT ( schema_name IN VARCHAR2, object_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL, object_type IN BINARY_INTEGER DEFAULT TABLE_OBJECT, repair_table_name IN VARCHAR2 DEFAULT 'REPAIR_TABLE', flags IN BINARY_INTEGER DEFAULT NULL, relative_fno IN BINARY_INTEGER DEFAULT NULL, block_start IN BINARY_INTEGER DEFAULT NULL, block_end IN BINARY_INTEGER DEFAULT NULL, corrupt_count OUT BINARY_INTEGER); Parameters Table 140-5 CHECK_OBJECT Procedure Parameters Parameter Description schema_name Schema name of the object to be checked. object_name Name of the table or index to be checked. partition_name Partition or subpartition name to be checked. If this is a partitioned object, and if partition_name is not specified, then all partitions and subpartitions are checked. If this is a partitioned object, and if the specified partition contains subpartitions, then all subpartitions are checked. object_type Type of the object to be processed. This must be either TABLE_OBJECT (default) or INDEX_OBJECT . See " Constants " . repair_table_name Name of the repair table to be populated. The table must exist in the SYS schema. Use the ADMIN_TABLES Procedure to create a repair table. The default name is REPAIR_TABLE . flags Reserved for future use. relative_fno Relative file number: Used when specifying a block range. block_start First block to process if specifying a block range. May be specified only if the object is a single table, partition, or subpartition. block_end Last block to process if specifying a block range. May be specified only if the object is a single table, partition, or subpartition. If only one of block_start or block_end is specified, then the other defaults to the first or last block in the file respectively. corrupt_count Number of corruptions reported. Usage Notes You may optionally specify a DBA range, partition name, or subpartition name when you want to check a portion of an object.