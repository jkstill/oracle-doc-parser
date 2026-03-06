---
id: 19c__DBMS_UTILITY.DATA_BLOCK_ADDRESS_FILE
name: DBMS_UTILITY.DATA_BLOCK_ADDRESS_FILE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.DATA_BLOCK_ADDRESS_FILE

This function gets the file number part of a data block address.

## Syntax

```sql
DBMS_UTILITY.DATA_BLOCK_ADDRESS_FILE (
   dba NUMBER) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dba | NUMBER) | IN | Data block address |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.DATA_BLOCK_ADDRESS_FILE ( dba NUMBER) RETURN NUMBER; Parameters Table 187-15 DATA_BLOCK_ADDRESS_FILE Function Parameters Parameter Description dba Data block address Pragmas pragma restrict_references (data_block_address_file, WNDS, RNDS, WNPS, RNPS); Return Values File that contains the block. Usage Notes This function should not be used with datablocks which belong to bigfile tablespaces.