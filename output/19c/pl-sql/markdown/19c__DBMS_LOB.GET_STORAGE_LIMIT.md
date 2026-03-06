---
id: 19c__DBMS_LOB.GET_STORAGE_LIMIT
name: DBMS_LOB.GET_STORAGE_LIMIT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.GET_STORAGE_LIMIT

This function returns the LOB storage limit for the specified LOB.

## Syntax

```sql
DBMS_LOB.GET_STORAGE_LIMIT (
   lob_loc  IN CLOB CHARACTER SET ANY_CS)
 RETURN INTEGER; 

DBMS_LOB.GET_STORAGE_LIMIT (
   lob_loc  IN BLOB)
 RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | CLOB | IN | LOB locator. For more information, see Operational Notes . |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.GET_STORAGE_LIMIT ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN INTEGER; DBMS_LOB.GET_STORAGE_LIMIT ( lob_loc IN BLOB) RETURN INTEGER; Pragmas PRAGMA RESTRICT_REFERENCES(get_storage_limit, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-60 GET_STORAGE_LIMIT Function Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . Return Value The value returned from this function is the maximum allowable size for specified LOB locator. For BLOB s, the return value depends on the block size of the tablespace the LOB resides in and is calculated as (2 32 )-1 (4294967295) times the block size of the tablespace. For CLOB s/ NCLOB s, the value returned is the(2 32 )-1 (4294967295) times the block size of the tablespace divided by the character width of the CLOB / NCLOB . Usage See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for details on LOB storage limits