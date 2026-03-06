---
id: 19c__DBMS_LOB.COMPARE
name: DBMS_LOB.COMPARE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.COMPARE

This function compares two entire LOBs or parts of two LOBs.

## Syntax

```sql
DBMS_LOB.COMPARE (
   lob_1            IN BLOB,
   lob_2            IN BLOB,
   amount           IN INTEGER := DBMS_LOB.LOBMAXSIZE,
   offset_1         IN INTEGER := 1,
   offset_2         IN INTEGER := 1)
  RETURN INTEGER;

DBMS_LOB.COMPARE (
   lob_1            IN CLOB  CHARACTER SET ANY_CS,
   lob_2            IN CLOB  CHARACTER SET lob_1%CHARSET,
   amount           IN INTEGER := DBMS_LOB.LOBMAXSIZE,
   offset_1         IN INTEGER := 1,
   offset_2         IN INTEGER := 1)
  RETURN INTEGER; 

DBMS_LOB.COMPARE (
   lob_1            IN BFILE,
   lob_2            IN BFILE,
   amount           IN INTEGER,
   offset_1         IN INTEGER := 1,
   offset_2         IN INTEGER := 1)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_1 | BLOB | IN | LOB locator of first target for comparison. |
| lob_2 | BLOB | IN | LOB locator of second target for comparison. |
| amount | INTEGER | IN | Number of bytes (for BLOBs ) or characters (for CLOB s/ NCLOBS s) to compare. |
| offset_1 | INTEGER | IN | Offset in bytes or characters on the first LOB (origin: 1) for the comparison. |
| offset_2 | INTEGER | IN | Offset in bytes or characters on the second LOB (origin: 1) for the comparison. |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.COMPARE ( lob_1 IN BLOB, lob_2 IN BLOB, amount IN INTEGER := DBMS_LOB.LOBMAXSIZE, offset_1 IN INTEGER := 1, offset_2 IN INTEGER := 1) RETURN INTEGER; DBMS_LOB.COMPARE ( lob_1 IN CLOB CHARACTER SET ANY_CS, lob_2 IN CLOB CHARACTER SET lob_1%CHARSET, amount IN INTEGER := DBMS_LOB.LOBMAXSIZE, offset_1 IN INTEGER := 1, offset_2 IN INTEGER := 1) RETURN INTEGER; DBMS_LOB.COMPARE ( lob_1 IN BFILE, lob_2 IN BFILE, amount IN INTEGER, offset_1 IN INTEGER := 1, offset_2 IN INTEGER := 1) RETURN INTEGER; Pragmas pragma restrict_references(COMPARE, WNDS, WNPS, RNDS, RNPS); Parameters Table 99-14 COMPARE Function Parameters Parameter Description lob_1 LOB locator of first target for comparison. lob_2 LOB locator of second target for comparison. amount Number of bytes (for BLOBs ) or characters (for CLOB s/ NCLOBS s) to compare. offset_1 Offset in bytes or characters on the first LOB (origin: 1) for the comparison. offset_2 Offset in bytes or characters on the second LOB (origin: 1) for the comparison. Return Values INTEGER : 0 if the comparison succeeds, nonzero if not. NULL , if any of amount, offset_1 or offset_2 is not a valid LOB offset value. A valid offset is within the range of 1 to LOBMAXSIZE inclusive. Usage Notes You can only compare LOBs of the same datatype ( LOBs of BLOB type with other BLOBs , and CLOBs with CLOBs , and BFILEs with BFILEs ). For BFILEs , the file must be already opened using a successful FILEOPEN operation for this operation to succeed. COMPARE returns 0 if the data exactly matches over the range specified by the offset and amount parameters. COMPARE returns -1 if the first CLOB is less than the second, and 1 if it is greater. For fixed-width n -byte CLOBs , if the input amount for COMPARE is specified to be greater than ( DBMS_LOB . LOBMAXSIZE / n ), then COMPARE matches characters in a range of size ( DBMS_LOB . LOBMAXSIZE / n ), or Max(length(clob1), length(clob2)), whichever is lesser. If COMPARE is called on any LOB that has been archived, it implicitly gets the LOB before the compare begins. If COMPARE() is called on a SecureFiles LOB that is a DBFS Link, the linked LOB is streamed from DBFS, if possible, otherwise an exception is thrown.