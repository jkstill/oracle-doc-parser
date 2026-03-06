---
id: 19c__DBMS_LOB.GETLENGTH
name: DBMS_LOB.GETLENGTH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.GETLENGTH

This function gets the length of the specified LOB. The length in bytes or characters is returned.

## Syntax

```sql
DBMS_LOB.GETLENGTH (
   lob_loc    IN  BLOB) 
  RETURN INTEGER;
 
DBMS_LOB.GETLENGTH (
   lob_loc    IN  CLOB   CHARACTER SET ANY_CS) 
  RETURN INTEGER; 

DBMS_LOB.GETLENGTH (
   file_loc    IN  BFILE) 
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_loc | BFILE) | IN | The file locator for the LOB whose length is to be returned. |

**Returns:** `INTEGER`

## Usage Notes

The length returned for a BFILE includes the EOF , if it exists. Any 0-byte or space filler in the LOB caused by previous ERASE or WRITE operations is also included in the length count. The length of an empty internal LOB is 0. Syntax DBMS_LOB.GETLENGTH ( lob_loc IN BLOB) RETURN INTEGER; DBMS_LOB.GETLENGTH ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN INTEGER; DBMS_LOB.GETLENGTH ( file_loc IN BFILE) RETURN INTEGER; Pragmas pragma restrict_references(GETLENGTH, WNDS, WNPS, RNDS, RNPS); Parameters Table 99-63 GETLENGTH Function Parameter Parameter Description file_loc The file locator for the LOB whose length is to be returned. Return Values The length of the LOB in bytes or characters as an INTEGER . NULL is returned if the input LOB is NULL or if the input lob_loc is NULL . An error is returned in the following cases for BFILEs : lob_loc does not have the necessary directory and operating system privileges lob_loc cannot be read because of an operating system read error See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure