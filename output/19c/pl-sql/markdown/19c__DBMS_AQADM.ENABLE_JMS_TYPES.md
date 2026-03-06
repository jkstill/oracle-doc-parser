---
id: 19c__DBMS_AQADM.ENABLE_JMS_TYPES
name: DBMS_AQADM.ENABLE_JMS_TYPES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ENABLE_JMS_TYPES

Enqueue JMS types and XML types.

## Syntax

```sql
DBMS_AQADM.ENABLE_JMS_TYPES (
   queue_table   IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_table | VARCHAR2) | IN | Specifies name of the queue table to be enabled for JMS and XML types. |

## Usage Notes

Syntax DBMS_AQADM.ENABLE_JMS_TYPES ( queue_table IN VARCHAR2); Parameters Table 23-33 ENABLE_JMS_TYPES Procedure Parameters Parameter Description queue_table Specifies name of the queue table to be enabled for JMS and XML types.