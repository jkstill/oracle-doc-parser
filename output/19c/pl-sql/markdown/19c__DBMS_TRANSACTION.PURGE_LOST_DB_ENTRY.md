---
id: 19c__DBMS_TRANSACTION.PURGE_LOST_DB_ENTRY
name: DBMS_TRANSACTION.PURGE_LOST_DB_ENTRY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.PURGE_LOST_DB_ENTRY

Procedure PURGE_LOST_DB_ENTRY purges entries that control database recovery from a local site.

## Syntax

```sql
DBMS_TRANSACTION.PURGE_LOST_DB_ENTRY (
   xid VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | VARCHAR2) | IN | Must be set to the value of the LOCAL_TRAN_ID column in the DBA_2PC_PENDING table. |

## Usage Notes

When a failure occurs during commit processing, automatic recovery consistently resolves the results at all sites involved in the transaction. However, if the remote database is destroyed or re-created before recovery completes, then the entries used to control recovery in DBA_2PC_PENDING and associated tables are never removed, and recovery will periodically retry. Procedure PURGE_LOST_DB_ENTRY enables removal of such transactions from the local site. Syntax DBMS_TRANSACTION.PURGE_LOST_DB_ENTRY ( xid VARCHAR2); Parameters Table 179-5 PURGE_LOST_DB_ENTRY Procedure Parameters Parameter Description xid Must be set to the value of the LOCAL_TRAN_ID column in the DBA_2PC_PENDING table. Usage Notes WARNING: PURGE_LOST_DB_ENTRY should only be used when the other database is lost or has been re-created. Any other use may leave the other database in an unrecoverable or inconsistent state. WARNING: PURGE_LOST_DB_ENTRY should only be used when the other database is lost or has been re-created. Any other use may leave the other database in an unrecoverable or inconsistent state.