---
id: 19c__DBMS_LOB.ISOPEN
name: DBMS_LOB.ISOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.ISOPEN

This function checks to see if the LOB was already opened using the input locator. This subprogram is for internal and external LOBs.

## Syntax

```sql
DBMS_LOB.ISOPEN (
   lob_loc IN BLOB) 
  RETURN INTEGER; 

DBMS_LOB.ISOPEN (
   lob_loc IN CLOB CHARACTER SET ANY_CS) 
  RETURN INTEGER; 

DBMS_LOB.ISOPEN (
   file_loc IN BFILE) 
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB) | IN | LOB locator. For more information, see Operational Notes . |
| file_loc | BFILE) | IN | File locator. |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.ISOPEN ( lob_loc IN BLOB) RETURN INTEGER; DBMS_LOB.ISOPEN ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN INTEGER; DBMS_LOB.ISOPEN ( file_loc IN BFILE) RETURN INTEGER; Pragmas PRAGMA RESTRICT_REFERENCES(isopen, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-70 ISOPEN Function Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . file_loc File locator. Return Values The return value is 1 if the LOB is open, 0 otherwise. Usage Notes For BFILES , openness is associated with the locator. If the input locator was never passed to OPEN, the BFILE is not considered to be opened by this locator. However, a different locator may have opened the BFILE . More than one OPEN can be performed on the same BFILE using different locators. For internal LOBs, openness is associated with the LOB, not with the locator. If locator1 opened the LOB, then locator2 also sees the LOB as open. For internal LOBs, ISOPEN requires a round-trip, because it checks the state on the server to see if the LOB is indeed open. For external LOBs ( BFILEs ), ISOPEN also requires a round-trip, because that's where the state is kept. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure