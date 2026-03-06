---
id: 19c__DBMS_CQ_NOTIFICATION.DEREGISTER
name: DBMS_CQ_NOTIFICATION.DEREGISTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CQ_NOTIFICATION
tags: [dbms_cq_notification]
source_file: DBMS_CQ_NOTIFICATION.html
---

# DBMS_CQ_NOTIFICATION.DEREGISTER

This procedure describes the client with the specified registration identifier (ID).

## Syntax

```sql
DBMS_CQ_NOTIFICATION.DEREGISTER (
  regid IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| regid | NUMBER) | IN | Client registration ID |

## Usage Notes

Syntax DBMS_CQ_NOTIFICATION.DEREGISTER ( regid IN NUMBER); Parameters Table 40-8 DEREGISTER Procedure Parameters Parameter Description regid Client registration ID Usage Notes Only the user that created the registration (or the SYS user) will be able to desubscribe the registration.