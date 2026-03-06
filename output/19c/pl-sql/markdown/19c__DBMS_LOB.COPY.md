---
id: 19c__DBMS_LOB.COPY
name: DBMS_LOB.COPY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.COPY

This procedure copies all, or a part of, a source internal LOB to a destination internal LOB. You can specify the offsets for both the source and destination LOBs, and the number of bytes or characters to copy.

## Syntax

```sql
DBMS_LOB.COPY (
  dest_lob    IN OUT NOCOPY BLOB,
  src_lob     IN            BLOB,
  amount      IN            INTEGER,
  dest_offset IN            INTEGER := 1,
  src_offset  IN            INTEGER := 1);

DBMS_LOB.COPY ( 
  dest_lob    IN OUT NOCOPY CLOB  CHARACTER SET ANY_CS,
  src_lob     IN            CLOB  CHARACTER SET dest_lob%CHARSET,
  amount      IN            INTEGER,
  dest_offset IN            INTEGER := 1,
  src_offset  IN            INTEGER := 1);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dest_lob | NOCOPY | IN OUT | LOB locator of the copy target. |
| src_lob | BLOB | IN | LOB locator of source for the copy. |
| amount | INTEGER | IN | Number of bytes (for BLOBs ) or characters (for CLOBs ) to copy. |
| dest_offset | INTEGER | IN | Offset in bytes or characters in the destination LOB (origin: 1) for the start of the copy. |
| src_offset | INTEGER | IN | Offset in bytes or characters in the source LOB (origin: 1) for the start of the copy. |

## Usage Notes

Syntax DBMS_LOB.COPY ( dest_lob IN OUT NOCOPY BLOB, src_lob IN BLOB, amount IN INTEGER, dest_offset IN INTEGER := 1, src_offset IN INTEGER := 1); DBMS_LOB.COPY ( dest_lob IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, src_lob IN CLOB CHARACTER SET dest_lob%CHARSET, amount IN INTEGER, dest_offset IN INTEGER := 1, src_offset IN INTEGER := 1); Parameters Table 99-22 COPY Procedure Parameters Parameter Description dest_lob LOB locator of the copy target. src_lob LOB locator of source for the copy. amount Number of bytes (for BLOBs ) or characters (for CLOBs ) to copy. dest_offset Offset in bytes or characters in the destination LOB (origin: 1) for the start of the copy. src_offset Offset in bytes or characters in the source LOB (origin: 1) for the start of the copy. Exceptions Table 99-23 COPY Procedure Exceptions Exception Description VALUE_ERROR Any of the input parameters are NULL or invalid. INVALID_ARGVAL Either: - src_offset or dest_offset < 1 - src_offset or dest_offset > LOBMAXSIZE - amount < 1 - amount > LOBMAXSIZE QUERY_WRITE Cannot perform a LOB write inside a query or PDML parallel execution server BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled if buffering is enabled on either LOB Usage Notes If the offset you specify in the destination LOB is beyond the end of the data currently in this LOB, then zero-byte fillers or spaces are inserted in the destination BLOB or CLOB respectively. If the offset is less than the current length of the destination LOB, then existing data is overwritten. It is not an error to specify an amount that exceeds the length of the data in the source LOB. Thus, you can specify a large amount to copy from the source LOB, which copies data from the src_offset to the end of the source LOB. It is not mandatory that you wrap the LOB operation inside the Open/Close interfaces. If you did not open the LOB before performing the operation, the functional and domain indexes on the LOB column are updated during the call. However, if you opened the LOB before performing the operation, you must close it before you commit the transaction. When an internal LOB is closed, it updates the functional and domain indexes on the LOB column. If you do not wrap the LOB operation inside the Open/Close API, the functional and domain indexes are updated each time you write to the LOB. This can adversely affect performance. Therefore, it is recommended that you enclose write operations to the LOB within the OPEN or CLOSE statement. Prior to copy, the source and destination LOBs are retrieved, if they are currently archived. For a complete over-write, the destination LOB is not retrieved. If the source LOB is a DBFS Link, the data is streamed from DBFS, if possible, otherwise an exception is thrown. If the destination LOB is a DBFS Link, an exception is thrown. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure