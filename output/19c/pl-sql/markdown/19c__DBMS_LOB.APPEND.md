---
id: 19c__DBMS_LOB.APPEND
name: DBMS_LOB.APPEND
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.APPEND

This procedure appends the contents of a source internal LOB to a destination LOB. It appends the complete source LOB.

## Syntax

```sql
DBMS_LOB.APPEND (
   dest_lob IN OUT  NOCOPY BLOB, 
   src_lob  IN             BLOB); 

DBMS_LOB.APPEND (
   dest_lob IN OUT  NOCOPY CLOB  CHARACTER SET ANY_CS, 
   src_lob  IN             CLOB  CHARACTER SET dest_lob%CHARSET);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dest_lob | NOCOPY | IN OUT | Locator for the internal LOB to which the data is to be appended. |
| src_lob | BLOB) | IN | Locator for the internal LOB from which the data is to be read. |

## Usage Notes

Syntax DBMS_LOB.APPEND ( dest_lob IN OUT NOCOPY BLOB, src_lob IN BLOB); DBMS_LOB.APPEND ( dest_lob IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, src_lob IN CLOB CHARACTER SET dest_lob%CHARSET); Parameters Table 99-10 APPEND Procedure Parameters Parameter Description dest_lob Locator for the internal LOB to which the data is to be appended. src_lob Locator for the internal LOB from which the data is to be read. Exceptions Table 99-11 APPEND Procedure Exceptions Exception Description VALUE_ERROR Either the source or the destination LOB is NULL . QUERY_WRITE Cannot perform a LOB write inside a query or PDML parallel execution server BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled if buffering is enabled on either LOB Usage Notes It is not mandatory that you wrap the LOB operation inside the Open/Close interfaces. If you did not open the LOB before performing the operation, the functional and domain indexes on the LOB column are updated during the call. However, if you opened the LOB before performing the operation, you must close it before you commit the transaction. When an internal LOB is closed, it updates the functional and domain indexes on the LOB column. If you do not wrap the LOB operation inside the Open/Close API, the functional and domain indexes are updated each time you write to the LOB. This can adversely affect performance. Therefore, it is recommended that you enclose write operations to the LOB within the OPEN or CLOSE statement. If APPEND is called on a LOB that has been archived, it implicitly gets the LOB before the first byte is written If APPEND is called on a SecureFiles LOB that is a DBFS Link, an exception is thrown. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure