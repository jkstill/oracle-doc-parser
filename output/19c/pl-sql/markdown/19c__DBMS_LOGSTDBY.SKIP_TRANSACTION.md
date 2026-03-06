---
id: 19c__DBMS_LOGSTDBY.SKIP_TRANSACTION
name: DBMS_LOGSTDBY.SKIP_TRANSACTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.SKIP_TRANSACTION

This procedure provides a way to skip (ignore) applying transactions to the logical standby database. You can skip specific transactions by specifying transaction identification information.

## Syntax

```sql
DBMS_LOGSTDBY.SKIP_TRANSACTION (
     xidusn_p          IN NUMBER,
     xidslt_p          IN NUMBER,
     xidsqn_p          IN NUMBER,
     con_name_p      VARCHAR2     IN     DEFAULT  NULL
);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xidusn_p NUMBER |  |  | Transaction ID undo segment number of the transaction being skipped |
| xidslt_p NUMBER |  |  | Transaction ID slot number of the transaction being skipped |
| xidsqn_p NUMBER |  |  | Transaction ID sequence number of the transaction being skipped |
| con_name_p | VARCHAR2 | IN | The transaction name. |

## Usage Notes

Syntax DBMS_LOGSTDBY.SKIP_TRANSACTION ( xidusn_p IN NUMBER, xidslt_p IN NUMBER, xidsqn_p IN NUMBER, con_name_p VARCHAR2 IN DEFAULT NULL ); Parameters Table 102-19 SKIP_TRANSACTION Procedure Parameters Parameter Description xidusn_p NUMBER Transaction ID undo segment number of the transaction being skipped xidslt_p NUMBER Transaction ID slot number of the transaction being skipped xidsqn_p NUMBER Transaction ID sequence number of the transaction being skipped con_name_p The transaction name. Usage Notes If SQL Apply stops due to a particular transaction (for example, a DDL transaction), you can specify that transaction ID and then continue to apply. You can call this procedure multiple times for as many transactions as you want SQL Apply to ignore. WARNING: SKIP_TRANSACTION is an inherently dangerous operation. Do not invoke this procedure unless you have examined the transaction in question through the V$LOGMNR_CONTENTS view and have taken compensating actions at the logical standby database. SKIP_TRANSACTION is not the appropriate procedure to invoke to skip DML changes to a table. To skip a DML failure, use a SKIP procedure, such as SKIP('DML','MySchema','MyFailed Table'). Using the SKIP_TRANSACTION procedure for DML transactions may skip changes for other tables, thus logically corrupting them. WARNING: SKIP_TRANSACTION is an inherently dangerous operation. Do not invoke this procedure unless you have examined the transaction in question through the V$LOGMNR_CONTENTS view and have taken compensating actions at the logical standby database. SKIP_TRANSACTION is not the appropriate procedure to invoke to skip DML changes to a table. To skip a DML failure, use a SKIP procedure, such as SKIP('DML','MySchema','MyFailed Table'). Using the SKIP_TRANSACTION procedure for DML transactions may skip changes for other tables, thus logically corrupting them. This procedure requires DBA privileges to execute. Use the DBA_LOGSTDBY_SKIP_TRANSACTION view to list the transactions that are going to be skipped by SQL Apply.