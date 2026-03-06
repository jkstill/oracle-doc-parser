---
id: 19c__DBMS_CQ_NOTIFICATION.ENABLE_REG
name: DBMS_CQ_NOTIFICATION.ENABLE_REG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CQ_NOTIFICATION
tags: [dbms_cq_notification]
source_file: DBMS_CQ_NOTIFICATION.html
---

# DBMS_CQ_NOTIFICATION.ENABLE_REG

This procedure adds objects to an existing registration identifier (ID).

## Syntax

```sql
DBMS_CQ_NOTIFICATION.ENABLE_REG (  
  regid IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| regid | NUMBER) | IN | Client registration ID |

## Usage Notes

It is similar to the interface for creating a new registration, except that it takes an existing regid to which to add objects.Subsequent execution of queries causes the objects referenced in the queries to be added to the specified regid , and the registration is completed on invoking the REG_END Procedure . Syntax DBMS_CQ_NOTIFICATION.ENABLE_REG ( regid IN NUMBER); Parameters Table 40-9 ENABLE_REG Procedure Parameters Parameter Description regid Client registration ID Usage Notes Only the user that created the registration will be able to add further objects to the registration.