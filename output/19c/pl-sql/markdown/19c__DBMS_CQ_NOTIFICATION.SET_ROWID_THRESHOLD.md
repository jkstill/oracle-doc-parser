---
id: 19c__DBMS_CQ_NOTIFICATION.SET_ROWID_THRESHOLD
name: DBMS_CQ_NOTIFICATION.SET_ROWID_THRESHOLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CQ_NOTIFICATION
tags: [dbms_cq_notification]
source_file: DBMS_CQ_NOTIFICATION.html
---

# DBMS_CQ_NOTIFICATION.SET_ROWID_THRESHOLD

This procedure configures the maximum number of rows of a table published in a change notification if the rows of the table are modified in a transaction.

## Syntax

```sql
DBMS_CQ_NOTIFICATION.SET_ROWID_THRESHOLD (  
  tbname     IN  VARCHAR2,
  threshold  IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tbname | VARCHAR2 | IN | Table name qualified by the schema name in the form schemaname.tablename |
| threshold | NUMBER) | IN | Maximum number of modified rows of the table to be published in the change notification |

## Usage Notes

Syntax DBMS_CQ_NOTIFICATION.SET_ROWID_THRESHOLD ( tbname IN VARCHAR2, threshold IN NUMBER); Parameters Table 40-11 SET_ROWID_THRESHOLD Procedure Parameters Parameter Description tbname Table name qualified by the schema name in the form schemaname.tablename threshold Maximum number of modified rows of the table to be published in the change notification Usage Notes The table needs to be registered for change notification either at object change granularity or at query result set granularity. The threshold set by means of this subprogram applies to that instance only and does not persist across instance startup/shutdown.