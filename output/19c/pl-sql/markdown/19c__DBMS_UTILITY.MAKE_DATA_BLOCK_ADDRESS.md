---
id: 19c__DBMS_UTILITY.MAKE_DATA_BLOCK_ADDRESS
name: DBMS_UTILITY.MAKE_DATA_BLOCK_ADDRESS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.MAKE_DATA_BLOCK_ADDRESS

This function creates a data block address given a file number and a block number.

## Syntax

```sql
DBMS_UTILITY.MAKE_DATA_BLOCK_ADDRESS (
   file  NUMBER, 
   block NUMBER) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file | NUMBER | IN | File that contains the block |
| block | NUMBER) | IN | Offset of the block within the file in terms of block increments |

**Returns:** `NUMBER`

## Usage Notes

A data block address is the internal structure used to identify a block in the database. This function is useful when accessing certain fixed tables that contain data block addresses. Syntax DBMS_UTILITY.MAKE_DATA_BLOCK_ADDRESS ( file NUMBER, block NUMBER) RETURN NUMBER; Parameters Table 187-29 MAKE_DATA_BLOCK_ADDRESS Function Parameters Parameter Description file File that contains the block block Offset of the block within the file in terms of block increments Pragmas pragma restrict_references (make_data_block_address, WNDS, RNDS, WNPS, RNPS); Return Values Data block address.