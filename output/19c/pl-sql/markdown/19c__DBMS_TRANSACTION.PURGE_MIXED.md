---
id: 19c__DBMS_TRANSACTION.PURGE_MIXED
name: DBMS_TRANSACTION.PURGE_MIXED
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.PURGE_MIXED

This procedure deletes information about a given mixed outcome transaction

## Syntax

```sql
DBMS_TRANSACTION.PURGE_MIXED (
   xid VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | VARCHAR2) | IN | Must be set to the value of the LOCAL_TRAN_ID column in the DBA_2PC_PENDING table. |

## Usage Notes

When in-doubt transactions are forced to commit or rollback (instead of letting automatic recovery resolve their outcomes), there is a possibility that a transaction can have a mixed outcome; some sites commit, and others rollback. Such inconsistency cannot be resolved automatically by Oracle. However, Oracle flags entries in DBA_2PC_PENDING by setting the MIXED column to a value of 'yes'. Oracle never automatically deletes information about a mixed outcome transaction. When the application or DBA is certain that all inconsistencies that might have arisen as a result of the mixed transaction have been resolved, this procedure can be used to delete the information about a given mixed outcome transaction. Syntax DBMS_TRANSACTION.PURGE_MIXED ( xid VARCHAR2); Parameters Table 179-7 PURGE_MIXED Procedure Parameters Parameter Description xid Must be set to the value of the LOCAL_TRAN_ID column in the DBA_2PC_PENDING table.