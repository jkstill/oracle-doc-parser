---
id: 19c__DBMS_XMLINDEX.PROCESS_PENDING
name: DBMS_XMLINDEX.PROCESS_PENDING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLINDEX
tags: [dbms_xmlindex]
source_file: DBMS_XMLINDEX.html
---

# DBMS_XMLINDEX.PROCESS_PENDING

This procedure processes executes DMLs required to complete a NONBLOCKING ALTER INDEX ADD_GROUP/ADD_COLUMN operation on an XMLIndex .

## Syntax

```sql
DBMS_XMLINDEX.PROCESS_PENDING (
   xml_index_schema    IN     VARCHAR2,
   xml_index_name      IN     VARCHAR2,
   pending_row_count   OUT    BINARY_INTEGER,
   error_row_count     OUT    BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xml_index_schema | VARCHAR2 | IN | Name of the owner of the XMLIndex |
| xml_index_name | VARCHAR2 | IN | Name of the XMLIndex to be altered using NONBLOCKING ALTER INDEX OPERATION |
| pending_row_count | BINARY_INTEGER | OUT | Number of pending rows to be processed |
| error_row_count | BINARY_INTEGER) | OUT | Number of rows for which indexing may have failed because of an error |

## Usage Notes

Syntax DBMS_XMLINDEX.PROCESS_PENDING ( xml_index_schema IN VARCHAR2, xml_index_name IN VARCHAR2, pending_row_count OUT BINARY_INTEGER, error_row_count OUT BINARY_INTEGER); Parameters Table 206-6 PROCESS_PENDING Procedure Parameters Parameter Description xml_index_schema Name of the owner of the XMLIndex xml_index_name Name of the XMLIndex to be altered using NONBLOCKING ALTER INDEX OPERATION pending_row_count Number of pending rows to be processed error_row_count Number of rows for which indexing may have failed because of an error Usage Notes This procedure will iteratively attempt to index all necessary rows in small batches while skipping rows that are locked and rows for which index maintenance fails with an error. Therefore, it may have to be executed multiple times for an XMLIndex until all pending rows are processed. Once all pending rows are processed, user can complete the NONBLOCKING ALTER INDEX OPERATION . If it is not possible process all the pending rows after multiple trials, the user will have to manually triage the locking or error issues by examining unprocessed rows in SYS_AIXSXI_######_PENDINGTAB and errors in SYS_AIXSXI_#####_ERRORTAB .. Keeping track of rows and the errors is useful in triaging issues. Examples EXEC DBMS_XMLINDEX.PROCESS_PENDING( 'SCOTT', 'PO_XMLINDEX_IX', out_param1, out_param2);