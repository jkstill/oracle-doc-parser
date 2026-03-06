---
id: 19c__DBMS_REPAIR.SEGMENT_FIX_STATUS
name: DBMS_REPAIR.SEGMENT_FIX_STATUS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR.SEGMENT_FIX_STATUS

With this procedure you can fix the corrupted state of a bitmap entry. The procedure either recalculates the state based on the current contents of the corresponding block or sets the state to a specific value.

## Syntax

```sql
DBMS_REPAIR.SEGMENT_FIX_STATUS (
   segment_owner   IN VARCHAR2,
   segment_name    IN VARCHAR2,
   segment_type    IN BINARY_INTEGER DEFAULT TABLE_OBJECT,
   file_number     IN BINARY_INTEGER DEFAULT NULL,
   block_number    IN BINARY_INTEGER DEFAULT NULL,
   status_value    IN BINARY_INTEGER DEFAULT NULL,
   partition_name  IN VARCHAR2 DEFAULT NULL,);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_owner |  |  | Schema name of the segment. |
| segment_name | VARCHAR2 | IN | Segment name. |
| partition_name | VARCHAR2 | IN | Optional. Name of an individual partition. NULL for nonpartitioned objects. Default is NULL . |
| segment_type | BINARY_INTEGER | IN | Optional Type of the segment (for example, TABLE_OBJECT or INDEX_OBJECT ). Default is NULL . |
| file_number | BINARY_INTEGER | IN | (optional) The tablespace-relative file number of the data block whose status has to be fixed. If omitted, all the blocks in the segment will be checked for state correctness and fixed. |
| block_number | BINARY_INTEGER | IN | (optional) The file-relative block number of the data block whose status has to be fixed. If omitted, all the blocks in the segment will be checked for state correctness and fixed. |
| status_value | BINARY_INTEGER | IN | (optional) The value to which the block status described by the file_number and block_number will be set. If omitted, the status will be set based on the current state of the block. This is almost always the case, but if there is a bug in the calculation algorithm, the value can be set manually. Status values: 1 = block is full 2 = block is 0-25% free 3 = block is 25-50% free 4 = block is 50-75% free 5 = block is 75-100% free The status for bitmap blocks, segment headers, and extent map blocks cannot be altered. The status for blocks in a fixed hash area cannot be altered. For index blocks, there are only two possible states: 1 = block is full and 3 = block has free space. |

## Usage Notes

Syntax DBMS_REPAIR.SEGMENT_FIX_STATUS ( segment_owner IN VARCHAR2, segment_name IN VARCHAR2, segment_type IN BINARY_INTEGER DEFAULT TABLE_OBJECT, file_number IN BINARY_INTEGER DEFAULT NULL, block_number IN BINARY_INTEGER DEFAULT NULL, status_value IN BINARY_INTEGER DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL,); Parameters Table 140-10 SEGMENT_FIX_STATUS Procedure Parameters Parameter Description schema_owner Schema name of the segment. segment_name Segment name. partition_name Optional. Name of an individual partition. NULL for nonpartitioned objects. Default is NULL . segment_type Optional Type of the segment (for example, TABLE_OBJECT or INDEX_OBJECT ). Default is NULL . file_number (optional) The tablespace-relative file number of the data block whose status has to be fixed. If omitted, all the blocks in the segment will be checked for state correctness and fixed. block_number (optional) The file-relative block number of the data block whose status has to be fixed. If omitted, all the blocks in the segment will be checked for state correctness and fixed. status_value (optional) The value to which the block status described by the file_number and block_number will be set. If omitted, the status will be set based on the current state of the block. This is almost always the case, but if there is a bug in the calculation algorithm, the value can be set manually. Status values: 1 = block is full 2 = block is 0-25% free 3 = block is 25-50% free 4 = block is 50-75% free 5 = block is 75-100% free The status for bitmap blocks, segment headers, and extent map blocks cannot be altered. The status for blocks in a fixed hash area cannot be altered. For index blocks, there are only two possible states: 1 = block is full and 3 = block has free space.