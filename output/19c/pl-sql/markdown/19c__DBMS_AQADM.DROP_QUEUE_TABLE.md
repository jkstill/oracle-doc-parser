---
id: 19c__DBMS_AQADM.DROP_QUEUE_TABLE
name: DBMS_AQADM.DROP_QUEUE_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.DROP_QUEUE_TABLE

This procedure drops an existing queue table.

## Syntax

```sql
DBMS_AQADM.DROP_QUEUE_TABLE (
   queue_table       IN    VARCHAR2,
   force             IN    BOOLEAN DEFAULT FALSE,
   auto_commit       IN    BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_table | VARCHAR2 | IN | Name of a queue table to be dropped. |
| force | BOOLEAN | IN | FALSE means the operation does not succeed if there are any queues in the table. This is the default. TRUE means all queues in the table are stopped and dropped automatically. |
| auto_commit | BOOLEAN | IN | TRUE causes the current transaction, if any, to commit before the DROP_QUEUE_TABLE operation is carried out. The DROP_QUEUE_TABLE operation becomes persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. |

## Usage Notes

Syntax DBMS_AQADM.DROP_QUEUE_TABLE ( queue_table IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE, auto_commit IN BOOLEAN DEFAULT TRUE); Parameters Table 23-30 DROP_QUEUE_TABLE Procedure Parameters Parameter Description queue_table Name of a queue table to be dropped. force FALSE means the operation does not succeed if there are any queues in the table. This is the default. TRUE means all queues in the table are stopped and dropped automatically. auto_commit TRUE causes the current transaction, if any, to commit before the DROP_QUEUE_TABLE operation is carried out. The DROP_QUEUE_TABLE operation becomes persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. Usage Notes All the queues in a queue table must be stopped and dropped before the queue table can be dropped. You must do this explicitly unless the force option is used, in which case this is done automatically.