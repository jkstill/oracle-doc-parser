---
id: 19c__DBMS_LOB.LOADFROMFILE
name: DBMS_LOB.LOADFROMFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.LOADFROMFILE

This deprecated procedure copies all, or a part of, a source external LOB ( BFILE ) to a destination internal LOB.

## Syntax

```sql
DBMS_LOB.LOADFROMFILE (
   dest_lob    IN OUT NOCOPY BLOB, 
   src_file    IN            BFILE, 
   amount      IN            INTEGER, 
   dest_offset IN            INTEGER  := 1, 
   src_offset  IN            INTEGER  := 1);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dest_lob | NOCOPY | IN OUT | LOB locator of the target for the load. |
| src_file | BFILE | IN | BFILE locator of the source for the load. |
| amount | INTEGER | IN | Number of bytes to load from the BFILE . |
| dest_offset | INTEGER | IN | Offset in bytes or characters in the destination LOB (origin: 1) for the start of the load. |
| src_offset | INTEGER | IN | Offset in bytes in the source BFILE (origin: 1) for the start of the load. |

## Usage Notes

Note: This procedure has been deprecated starting in Oracle Database 12c release 12.2. Note: This procedure has been deprecated starting in Oracle Database 12c release 12.2. Syntax DBMS_LOB.LOADFROMFILE ( dest_lob IN OUT NOCOPY BLOB, src_file IN BFILE, amount IN INTEGER, dest_offset IN INTEGER := 1, src_offset IN INTEGER := 1); Parameters Table 99-81 LOADFROMFILE Procedure Parameters Parameter Description dest_lob LOB locator of the target for the load. src_file BFILE locator of the source for the load. amount Number of bytes to load from the BFILE . dest_offset Offset in bytes or characters in the destination LOB (origin: 1) for the start of the load. src_offset Offset in bytes in the source BFILE (origin: 1) for the start of the load. Usage Notes You can specify the offsets for both the source and destination LOBs, and the number of bytes to copy from the source BFILE . The amount and src_offset , because they refer to the BFILE , are in terms of bytes, and the dest_offset is either in bytes or characters for BLOBs and CLOBs respectively. Note: The input BFILE must have been opened prior to using this procedure. No character set conversions are performed implicitly when binary BFILE data is loaded into a CLOB . The BFILE data must already be in the same character set as the CLOB in the database. No error checking is performed to verify this.