---
id: 19c__DBMS_LOB.INSTR
name: DBMS_LOB.INSTR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.INSTR

This function returns the matching position of the nth occurrence of the pattern in the LOB, starting from the offset you specify.

## Syntax

```sql
DBMS_LOB.INSTR (
   lob_loc    IN   BLOB,
   pattern    IN   RAW,
   offset     IN   INTEGER := 1,
   nth        IN   INTEGER := 1)
  RETURN INTEGER;

DBMS_LOB.INSTR (
   lob_loc    IN   CLOB      CHARACTER SET ANY_CS,
   pattern    IN   VARCHAR2  CHARACTER SET lob_loc%CHARSET,
   offset     IN   INTEGER := 1,
   nth        IN   INTEGER := 1)
  RETURN INTEGER;

DBMS_LOB.INSTR (
   file_loc   IN   BFILE,
   pattern    IN   RAW,
   offset     IN   INTEGER := 1,
   nth        IN   INTEGER := 1)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | Locator for the LOB to be examined. For more information, see Operational Notes . |
| file_loc | BFILE | IN | The file locator for the LOB to be examined. |
| pattern | RAW | IN | Pattern to be tested for. The pattern is a group of RAW bytes for BLOBs , and a character string ( VARCHAR2 ) for CLOBs .The maximum size of the pattern is 16383 bytes. |
| offset | INTEGER | IN | Absolute offset in bytes ( BLOBs ) or characters ( CLOBs ) at which the pattern matching is to start. (origin: 1) |
| nth | INTEGER | IN | Occurrence number, starting at 1. |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.INSTR ( lob_loc IN BLOB, pattern IN RAW, offset IN INTEGER := 1, nth IN INTEGER := 1) RETURN INTEGER; DBMS_LOB.INSTR ( lob_loc IN CLOB CHARACTER SET ANY_CS, pattern IN VARCHAR2 CHARACTER SET lob_loc%CHARSET, offset IN INTEGER := 1, nth IN INTEGER := 1) RETURN INTEGER; DBMS_LOB.INSTR ( file_loc IN BFILE, pattern IN RAW, offset IN INTEGER := 1, nth IN INTEGER := 1) RETURN INTEGER; Pragmas pragma restrict_references(INSTR, WNDS, WNPS, RNDS, RNPS); Parameters Table 99-67 INSTR Function Parameters Parameter Description lob_loc Locator for the LOB to be examined. For more information, see Operational Notes . file_loc The file locator for the LOB to be examined. pattern Pattern to be tested for. The pattern is a group of RAW bytes for BLOBs , and a character string ( VARCHAR2 ) for CLOBs .The maximum size of the pattern is 16383 bytes. offset Absolute offset in bytes ( BLOBs ) or characters ( CLOBs ) at which the pattern matching is to start. (origin: 1) nth Occurrence number, starting at 1. Return Values Table 99-68 INSTR Function Return Values Return Description INTEGER Offset of the start of the matched pattern, in bytes or characters. It returns 0 if the pattern is not found. NULL Either: -any one or more of the IN parameters was NULL or INVALID . - offset < 1 or offset > LOBMAXSIZE . - nth < 1. - nth > LOBMAXSIZE. Usage Notes The form of the VARCHAR2 buffer (the pattern parameter) must match the form of the CLOB parameter. In other words, if the input LOB parameter is of type NCLOB , then the buffer must contain NCHAR data. Conversely, if the input LOB parameter is of type CLOB , then the buffer must contain CHAR data. For BFILEs , the file must be already opened using a successful FILEOPEN operation for this operation to succeed. Operations that accept RAW or VARCHAR2 parameters for pattern matching, such as INSTR , do not support regular expressions or special matching characters (as in the case of SQL LIKE ) in the pattern parameter or substrings.