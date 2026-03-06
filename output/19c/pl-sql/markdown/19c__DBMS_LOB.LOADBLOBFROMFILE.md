---
id: 19c__DBMS_LOB.LOADBLOBFROMFILE
name: DBMS_LOB.LOADBLOBFROMFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.LOADBLOBFROMFILE

This procedure loads data from BFILE to internal BLOB . This achieves the same outcome as LOADFROMFILE , and returns the new offsets.

## Syntax

```sql
DBMS_LOB.LOADBLOBFROMFILE (
   dest_lob    IN OUT NOCOPY BLOB, 
   src_bfile   IN            BFILE, 
   amount      IN            INTEGER, 
   dest_offset IN OUT        INTEGER, 
   src_offset  IN OUT        INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dest_lob | NOCOPY | IN OUT | BLOB locator of the target for the load. |
| src_bfile | BFILE | IN | BFILE locator of the source for the load. |
| amount | INTEGER | IN | Number of bytes to load from the BFILE . You can also use DBMS_LOB.LOBMAXSIZE to load until the end of the BFILE . |
| dest_offset | INTEGER | IN OUT | ( IN ) Offset in bytes in the destination BLOB (origin: 1) for the start of the write. (OUT) New offset in bytes in the destination BLOB right after the end of this write, which is also where the next write should begin. |
| src_offset | INTEGER) | IN OUT | (IN) Offset in bytes in the source BFILE (origin: 1) for the start of the read .(OUT) Offset in bytes in the source BFILE right after the end of this read, which is also where the next read should begin. |

## Usage Notes

Syntax DBMS_LOB.LOADBLOBFROMFILE ( dest_lob IN OUT NOCOPY BLOB, src_bfile IN BFILE, amount IN INTEGER, dest_offset IN OUT INTEGER, src_offset IN OUT INTEGER); Parameters Table 99-74 LOADBLOBFROMFILE Procedure Parameters Parameter Description dest_lob BLOB locator of the target for the load. src_bfile BFILE locator of the source for the load. amount Number of bytes to load from the BFILE . You can also use DBMS_LOB.LOBMAXSIZE to load until the end of the BFILE . dest_offset ( IN ) Offset in bytes in the destination BLOB (origin: 1) for the start of the write. (OUT) New offset in bytes in the destination BLOB right after the end of this write, which is also where the next write should begin. src_offset (IN) Offset in bytes in the source BFILE (origin: 1) for the start of the read .(OUT) Offset in bytes in the source BFILE right after the end of this read, which is also where the next read should begin. Usage Notes You can specify the offsets for both the source and destination LOBs, and the number of bytes to copy from the source BFILE . The amount and src_offset , because they refer to the BFILE , are in terms of bytes, and the dest_offset is in bytes for BLOBs . If the offset you specify in the destination LOB is beyond the end of the data currently in this LOB, then zero-byte fillers or spaces are inserted in the destination BLOB . If the offset is less than the current length of the destination LOB, then existing data is overwritten. There is an error if the input amount plus offset exceeds the length of the data in the BFILE (unless the amount specified is LOBMAXSIZE which you can specify to continue loading until the end of the BFILE is reached). It is not mandatory that you wrap the LOB operation inside the OPEN/CLOSE operations. If you did not open the LOB before performing the operation, the functional and domain indexes on the LOB column are updated during the call. However, if you opened the LOB before performing the operation, you must close it before you commit the transaction. When an internal LOB is closed, it updates the functional and domain indexes on the LOB column. If you do not wrap the LOB operation inside the OPEN/CLOSE , the functional and domain indexes are updated each time you write to the LOB. This can adversely affect performance. Therefore, it is recommended that you enclose write operations to the LOB within the OPEN or CLOSE statement. LOADFROMFILE gets the destination LOB prior to the load unless the load covers the entire LOB. Constants and Defaults There is no easy way to omit parameters. You must either declare a variable for IN/OUT parameter or provide a default value for the IN parameter. Here is a summary of the constants and the defaults that can be used. Constants defined in DBMSLOB.SQL lobmaxsize CONSTANT INTEGER := DBMS_LOB.LOBMAXSIZE; Exceptions Table 99-76 LOADBLOBFROMFILE Procedure Exceptions Exception Description VALUE_ERROR Any of the input parameters are NULL or INVALID . INVALID_ARGVAL Either: - src_offset or dest_offset < 1. - src_offset or dest_offset > LOBMAXSIZE . - amount < 1. - amount > LOBMAXSIZE . BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled if buffering is enabled on the BLOB See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure