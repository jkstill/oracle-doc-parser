---
id: 19c__DBMS_AQADM.DROP_QUEUE
name: DBMS_AQADM.DROP_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.DROP_QUEUE

This procedure drops an existing queue.

## Syntax

```sql
DBMS_AQADM.DROP_QUEUE (
   queue_name        IN    VARCHAR2,
   auto_commit       IN    BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue that is to be dropped. |
| auto_commit | BOOLEAN | IN | TRUE causes the current transaction, if any, to commit before the DROP_QUEUE operation is carried out. The DROP_QUEUE operation becomes persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. |

## Usage Notes

Syntax DBMS_AQADM.DROP_QUEUE ( queue_name IN VARCHAR2, auto_commit IN BOOLEAN DEFAULT TRUE); Parameters Table 23-29 DROP_QUEUE Procedure Parameters Parameter Description queue_name Name of the queue that is to be dropped. auto_commit TRUE causes the current transaction, if any, to commit before the DROP_QUEUE operation is carried out. The DROP_QUEUE operation becomes persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. Usage Notes DROP_QUEUE is not allowed unless STOP_QUEUE has been called to disable the queue for both enqueuing and dequeuing. All the queue data is deleted as part of the drop operation.