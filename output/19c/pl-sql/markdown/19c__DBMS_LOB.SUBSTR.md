---
id: 19c__DBMS_LOB.SUBSTR
name: DBMS_LOB.SUBSTR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.SUBSTR

This function returns amount bytes or characters of a LOB, starting from an absolute offset from the beginning of the LOB.

## Syntax

```sql
DBMS_LOB.SUBSTR (
   lob_loc     IN    BLOB,
   amount      IN    INTEGER := 32767,
   offset      IN    INTEGER := 1)
  RETURN RAW;

DBMS_LOB.SUBSTR (
   lob_loc     IN    CLOB   CHARACTER SET ANY_CS,
   amount      IN    INTEGER := 32767,
   offset      IN    INTEGER := 1)
  RETURN VARCHAR2 CHARACTER SET lob_loc%CHARSET;

DBMS_LOB.SUBSTR (
   file_loc     IN    BFILE,
   amount      IN    INTEGER := 32767,
   offset      IN    INTEGER := 1)
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | Locator for the LOB to be read. For more information, see Operational Notes . |
| file_loc | BFILE | IN | The file locator for the LOB to be examined. |
| amount | INTEGER | IN | Number of bytes (for BLOBs ) or characters (for CLOBs ) to be read. |
| offset | INTEGER | IN | Offset in bytes (for BLOBs ) or characters (for CLOBs ) from the start of the LOB (origin: 1). |

**Returns:** `RAW`

## Usage Notes

For fixed-width n -byte CLOBs , if the input amount for SUBSTR is greater than (32767/ n ), then SUBSTR returns a character buffer of length (32767/ n ), or the length of the CLOB , whichever is lesser. For CLOBs in a varying-width character set, n is the maximum byte-width used for characters in the CLOB. Syntax DBMS_LOB.SUBSTR ( lob_loc IN BLOB, amount IN INTEGER := 32767, offset IN INTEGER := 1) RETURN RAW; DBMS_LOB.SUBSTR ( lob_loc IN CLOB CHARACTER SET ANY_CS, amount IN INTEGER := 32767, offset IN INTEGER := 1) RETURN VARCHAR2 CHARACTER SET lob_loc%CHARSET; DBMS_LOB.SUBSTR ( file_loc IN BFILE, amount IN INTEGER := 32767, offset IN INTEGER := 1) RETURN RAW; Pragmas pragma restrict_references(SUBSTR, WNDS, WNPS, RNDS, RNPS); Parameters Table 99-95 SUBSTR Function Parameters Parameter Description lob_loc Locator for the LOB to be read. For more information, see Operational Notes . file_loc The file locator for the LOB to be examined. amount Number of bytes (for BLOBs ) or characters (for CLOBs ) to be read. offset Offset in bytes (for BLOBs ) or characters (for CLOBs ) from the start of the LOB (origin: 1). Return Values Table 99-96 SUBSTR Function Return Values Return Description RAW Function overloading that has a BLOB or BFILE in parameter. VARCHAR2 CLOB version. NULL Either: - any input parameter is NULL - amount < 1 - amount > 32767 - offset < 1 - offset > LOBMAXSIZE