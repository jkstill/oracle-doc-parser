---
id: 19c__DBMS_REPAIR.DUMP_ORPHAN_KEYS
name: DBMS_REPAIR.DUMP_ORPHAN_KEYS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR.DUMP_ORPHAN_KEYS

This procedure reports on index entries that point to rows in corrupt data blocks. For each such index entry encountered, a row is inserted into the specified orphan table.

## Syntax

```sql
DBMS_REPAIR.DUMP_ORPHAN_KEYS (
   schema_name       IN  VARCHAR2,
   object_name       IN  VARCHAR2,
   partition_name    IN  VARCHAR2       DEFAULT NULL,
   object_type       IN  BINARY_INTEGER DEFAULT INDEX_OBJECT,
   repair_table_name IN  VARCHAR2       DEFAULT 'REPAIR_TABLE',
   orphan_table_name IN  VARCHAR2       DEFAULT 'ORPHAN_KEYS_TABLE',
   flags             IN  BINARY_INTEGER DEFAULT NULL,
   key_count         OUT BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema name. |
| object_name | VARCHAR2 | IN | Object name. |
| partition_name | VARCHAR2 | IN | Partition or subpartition name to be processed. If this is a partitioned object, and if partition_name is not specified, then all partitions and subpartitions are processed. If this is a partitioned object, and if the specified partition contains subpartitions, then all subpartitions are processed. |
| object_type | BINARY_INTEGER | IN | Type of the object to be processed. The default is INDEX_OBJECT See " Constants " . |
| repair_table_name | VARCHAR2 | IN | Name of the repair table that has information regarding corrupt blocks in the base table. The specified table must exist in the SYS schema. The ADMIN_TABLES Procedure is used to create the table. |
| orphan_table_name | VARCHAR2 | IN | Name of the orphan key table to populate with information regarding each index entry that refers to a row in a corrupt data block. The specified table must exist in the SYS schema. The ADMIN_TABLES Procedure is used to create the table. |
| flags | BINARY_INTEGER | IN | Reserved for future use. |
| key_count | BINARY_INTEGER) | OUT | Number of index entries processed. |

## Usage Notes

If the repair table is specified, then any corrupt blocks associated with the base table are handled in addition to all data blocks that are marked software corrupt. Otherwise, only blocks that are marked corrupt are handled. This information may be useful for rebuilding lost rows in the table and for diagnostic purposes. Syntax DBMS_REPAIR.DUMP_ORPHAN_KEYS ( schema_name IN VARCHAR2, object_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL, object_type IN BINARY_INTEGER DEFAULT INDEX_OBJECT, repair_table_name IN VARCHAR2 DEFAULT 'REPAIR_TABLE', orphan_table_name IN VARCHAR2 DEFAULT 'ORPHAN_KEYS_TABLE', flags IN BINARY_INTEGER DEFAULT NULL, key_count OUT BINARY_INTEGER); Parameters Table 140-6 DUMP_ORPHAN_KEYS Procedure Parameters Parameter Description schema_name Schema name. object_name Object name. partition_name Partition or subpartition name to be processed. If this is a partitioned object, and if partition_name is not specified, then all partitions and subpartitions are processed. If this is a partitioned object, and if the specified partition contains subpartitions, then all subpartitions are processed. object_type Type of the object to be processed. The default is INDEX_OBJECT See " Constants " . repair_table_name Name of the repair table that has information regarding corrupt blocks in the base table. The specified table must exist in the SYS schema. The ADMIN_TABLES Procedure is used to create the table. orphan_table_name Name of the orphan key table to populate with information regarding each index entry that refers to a row in a corrupt data block. The specified table must exist in the SYS schema. The ADMIN_TABLES Procedure is used to create the table. flags Reserved for future use. key_count Number of index entries processed.