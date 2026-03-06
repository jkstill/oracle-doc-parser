---
id: 19c__DBMS_LOB.WRITE
name: DBMS_LOB.WRITE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.WRITE

This procedure writes a specified amount of data into an internal LOB, starting from an absolute offset from the beginning of the LOB. The data is written from the buffer parameter.

## Syntax

```sql
DBMS_LOB.WRITE (
   lob_loc  IN OUT NOCOPY  BLOB,
   amount   IN             INTEGER,
   offset   IN             INTEGER,
   buffer   IN             RAW);

DBMS_LOB.WRITE (
   lob_loc  IN OUT  NOCOPY CLOB   CHARACTER SET ANY_CS,
   amount   IN             INTEGER,
   offset   IN             INTEGER,
   buffer   IN             VARCHAR2 CHARACTER SET lob_loc%CHARSET);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | Locator for the internal LOB to be written to. For more information, see Operational Notes |
| amount | INTEGER | IN | Number of bytes (for BLOBs ) or characters (for CLOBs ) to write |
| offset | INTEGER | IN | Offset in bytes (for BLOBs ) or characters (for CLOBs ) from the start of the LOB (origin: 1) for the write operation. |
| buffer | RAW) | IN | Input buffer for the write |

## Usage Notes

WRITE replaces (overwrites) any data that already exists in the LOB at the offset, for the length you specify. Syntax DBMS_LOB.WRITE ( lob_loc IN OUT NOCOPY BLOB, amount IN INTEGER, offset IN INTEGER, buffer IN RAW); DBMS_LOB.WRITE ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, amount IN INTEGER, offset IN INTEGER, buffer IN VARCHAR2 CHARACTER SET lob_loc%CHARSET); Parameters Table 99-100 WRITE Procedure Parameters Parameter Description lob_loc Locator for the internal LOB to be written to. For more information, see Operational Notes amount Number of bytes (for BLOBs ) or characters (for CLOBs ) to write offset Offset in bytes (for BLOBs ) or characters (for CLOBs ) from the start of the LOB (origin: 1) for the write operation. buffer Input buffer for the write Exceptions Table 99-101 WRITE Procedure Exceptions Exception Description VALUE_ERROR Any of lob_loc , amount , or offset parameters are NULL , out of range, or INVALID . INVALID_ARGVAL Either: - amount < 1 - amount > 32767 bytes (or the character equivalent) - offset < 1 - offset > LOBMAXSIZE QUERY_WRITE Cannot perform a LOB write inside a query or PDML parallel execution server BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled if buffering is enabled on the LOB SECUREFILE_OUTOFBOUNDS Attempted to perform a write operation past the end of a LOB having FRAGMENT_* on it Usage Notes There is an error if the input amount is more than the data in the buffer. If the input amount is less than the data in the buffer, then only amount bytes or characters from the buffer is written to the LOB. If the offset you specify is beyond the end of the data currently in the LOB, then zero-byte fillers or spaces are inserted in the BLOB or CLOB respectively. The form of the VARCHAR2 buffer must match the form of the CLOB parameter. In other words, if the input LOB parameter is of type NCLOB , then the buffer must contain NCHAR data. Conversely, if the input LOB parameter is of type CLOB , then the buffer must contain CHAR data. When calling DBMS_LOB . WRITE from the client (for example, in a BEGIN / END block from within SQL*Plus), the buffer must contain data in the client's character set. The database converts the client-side buffer to the server's character set before it writes the buffer data to the LOB. It is not mandatory that you wrap the LOB operation inside the Open/Close interfaces. If you did not open the LOB before performing the operation, the functional and domain indexes on the LOB column are updated during the call. However, if you opened the LOB before performing the operation, you must close it before you commit the transaction. When an internal LOB is closed, it updates the functional and domain indexes on the LOB column. If you do not wrap the LOB operation inside the Open/Close API, the functional and domain indexes are updated each time you write to the LOB. This can adversely affect performance. Therefore, it is recommended that you enclose write operations to the LOB within the OPEN or CLOSE statement. WRITE gets the LOB, if necessary, before writing the LOB, unless the write is specified to overwrite the entire LOB. See Also: " APPEND Procedures " " COPY Procedures " Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure