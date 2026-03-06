---
id: 19c__DBMS_LOB.CLOSE
name: DBMS_LOB.CLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.CLOSE

This procedure closes a previously opened internal or external LOB.

## Syntax

```sql
DBMS_LOB.CLOSE (
   lob_loc    IN OUT NOCOPY BLOB); 

DBMS_LOB.CLOSE (
   lob_loc    IN OUT NOCOPY CLOB CHARACTER SET ANY_CS); 

DBMS_LOB.CLOSE (
   file_loc   IN OUT NOCOPY BFILE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator. For more information, see Operational Notes . |

## Usage Notes

Syntax DBMS_LOB.CLOSE ( lob_loc IN OUT NOCOPY BLOB); DBMS_LOB.CLOSE ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS); DBMS_LOB.CLOSE ( file_loc IN OUT NOCOPY BFILE); Parameters Table 99-13 CLOSE Procedure Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . Exceptions No error is returned if the BFILE exists but is not opened. An error is returned if the LOB is not open. Usage Notes CLOSE requires a round-trip to the server for both internal and external LOBs. For internal LOBs, CLOSE triggers other code that relies on the close call, and for external LOBs ( BFILEs ), CLOSE actually closes the server-side operating system file. It is not mandatory that you wrap all LOB operations inside the Open/Close interfaces. However, if you open a LOB, you must close it before you commit the transaction; an error is produced if you do not. When an internal LOB is closed, it updates the functional and domain indexes on the LOB column. It is an error to commit the transaction before closing all opened LOBs that were opened by the transaction. When the error is returned, the openness of the open LOBs is discarded, but the transaction is successfully committed. Hence, all the changes made to the LOB and non-LOB data in the transaction are committed, but the domain and function-based indexes are not updated. If this happens, you should rebuild the functional and domain indexes on the LOB column. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure