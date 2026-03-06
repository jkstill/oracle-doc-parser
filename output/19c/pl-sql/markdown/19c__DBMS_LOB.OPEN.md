---
id: 19c__DBMS_LOB.OPEN
name: DBMS_LOB.OPEN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.OPEN

This procedure opens a LOB, internal or external, in the indicated mode. Valid modes include read-only, and read/write.

## Syntax

```sql
DBMS_LOB.OPEN (
   lob_loc   IN OUT NOCOPY BLOB,
   open_mode IN            BINARY_INTEGER);
 
DBMS_LOB.OPEN (
   lob_loc   IN OUT NOCOPY CLOB CHARACTER SET ANY_CS,
   open_mode IN            BINARY_INTEGER);
 
DBMS_LOB.OPEN (
   file_loc  IN OUT NOCOPY BFILE,
   open_mode IN            BINARY_INTEGER := file_readonly);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator. For more information, see Operational Notes . |
| open_mode | BINARY_INTEGER) | IN | Mode in which to open. For BLOB and CLOB types, the mode can be either: LOB_READONLY or LOB_READWRITE . For BFILE types, the mode must be FILE_READONLY . |

## Usage Notes

Syntax DBMS_LOB.OPEN ( lob_loc IN OUT NOCOPY BLOB, open_mode IN BINARY_INTEGER); DBMS_LOB.OPEN ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, open_mode IN BINARY_INTEGER); DBMS_LOB.OPEN ( file_loc IN OUT NOCOPY BFILE, open_mode IN BINARY_INTEGER := file_readonly); Parameters Table 99-85 OPEN Procedure Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . open_mode Mode in which to open. For BLOB and CLOB types, the mode can be either: LOB_READONLY or LOB_READWRITE . For BFILE types, the mode must be FILE_READONLY . Usage Notes Note: If the LOB was opened in read-only mode, and if you try to write to the LOB, then an error is returned. BFILE can only be opened with read-only mode. OPEN requires a round-trip to the server for both internal and external LOBs. For internal LOBs, OPEN triggers other code that relies on the OPEN call. For external LOBs ( BFILEs ), OPEN requires a round-trip because the actual operating system file on the server side is being opened. It is not mandatory that you wrap all LOB operations inside the Open/Close interfaces. However, if you open a LOB, you must close it before you commit the transaction; an error is produced if you do not. When an internal LOB is closed, it updates the functional and domain indexes on the LOB column. It is an error to commit the transaction before closing all opened LOBs that were opened by the transaction. When the error is returned, the openness of the open LOBs is discarded, but the transaction is successfully committed. Hence, all the changes made to the LOB and non-LOB data in the transaction are committed, but the domain and function-based indexes are not updated. If this happens, you should rebuild the functional and domain indexes on the LOB column. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure Note: If the LOB was opened in read-only mode, and if you try to write to the LOB, then an error is returned. BFILE can only be opened with read-only mode. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure