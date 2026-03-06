---
id: 19c__DBMS_LOGSTDBY.UNSKIP_TRANSACTION
name: DBMS_LOGSTDBY.UNSKIP_TRANSACTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.UNSKIP_TRANSACTION

Use the UNSKIP_TRANSACTION procedure to delete rules specified earlier with the SKIP_TRANSACTION procedure.

## Syntax

```sql
DBMS_LOGSTDBY.UNSKIP_TRANSACTION (
     xidusn_p         IN NUMBER,
     xidslt_p         IN NUMBER,
     xidsqn_p         IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| XIDUSN |  |  | Transaction ID undo segment number of the transaction being skipped |
| XIDSLT |  |  | Transaction ID slot number of the transaction being skipped |
| XIDSQN |  |  | Transaction ID sequence number of the transaction being skipped |

## Usage Notes

The parameters specified in the UNSKIP_TRANSACTION procedure must match exactly for the procedure to delete an already-specified rule. Syntax DBMS_LOGSTDBY.UNSKIP_TRANSACTION ( xidusn_p IN NUMBER, xidslt_p IN NUMBER, xidsqn_p IN NUMBER); Parameters Table 102-23 UNSKIP_TRANSACTION Procedure Parameters Parameter Description XIDUSN Transaction ID undo segment number of the transaction being skipped XIDSLT Transaction ID slot number of the transaction being skipped XIDSQN Transaction ID sequence number of the transaction being skipped Exceptions Table 102-24 UNSKIP_TRANSACTION Procedure Exceptions Exception Description ORA-01031 need DBA privileges to execute this procedure ORA-16103 Logical Standby apply must be stopped to allow this operation ORA-16104 invalid Logical Standby option requested Usage Notes This procedure requires DBA privileges to execute. Query the DBA_LOGSTDBY_SKIP_TRANSACTION view to list the transactions that are going to be skipped by SQL Apply.