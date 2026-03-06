---
id: 19c__DBMS_AQ.UNREGISTER
name: DBMS_AQ.UNREGISTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.UNREGISTER

This procedure unregisters a subscription which turns off notifications.

## Syntax

```sql
DBMS_AQ.UNREGISTER (
   reg_list     IN  SYS.AQ$_REG_INFO_LIST,
   reg_count    IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| reg_list | SYS.AQ$_REG_INFO_LIST | IN | Specifies the list of subscriptions to which you want to register for message notifications. It is a list of AQ$_REG_INFO Type . |
| reg_count | NUMBER) | IN | Specifies the number of entries in the reg_list . |

## Usage Notes

Syntax DBMS_AQ.UNREGISTER ( reg_list IN SYS.AQ$_REG_INFO_LIST, reg_count IN NUMBER); Parameters Table 22-15 UNREGISTER Procedure Parameters Parameter Description reg_list Specifies the list of subscriptions to which you want to register for message notifications. It is a list of AQ$_REG_INFO Type . reg_count Specifies the number of entries in the reg_list . Usage Notes This procedure is used to unregister a subscription which turns off notifications. Several subscriptions can be unregistered from at one time.