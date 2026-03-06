---
id: 19c__DBMS_AQADM.STOP_QUEUE
name: DBMS_AQADM.STOP_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.STOP_QUEUE

This procedure disables enqueuing or dequeuing on the specified queue.

## Syntax

```sql
DBMS_AQADM.STOP_QUEUE (   
   queue_name      IN   VARCHAR2,
   enqueue         IN   BOOLEAN DEFAULT TRUE,
   dequeue         IN   BOOLEAN DEFAULT TRUE,
   wait            IN   BOOLEAN DEFAULT TRUE,
   free_memory     IN   BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue to be disabled |
| enqueue | BOOLEAN | IN | Specifies whether ENQUEUE should be disabled on this queue. TRUE means disable ENQUEUE . This is the default. FALSE means do not alter the current setting. |
| dequeue | BOOLEAN | IN | Specifies whether DEQUEUE should be disabled on this queue. TRUE means disable DEQUEUE . This is the default. FALSE means do not alter the current setting. |
| wait | BOOLEAN | IN | Specifies whether to wait for the completion of outstanding transactions. TRUE means wait if there are any outstanding transactions. In this state no new transactions are allowed to enqueue to or dequeue from this queue. FALSE means return immediately either with a success or an error. |
| free_memory | BOOLEAN | IN | Specifies whether the queue should be stopped. |

## Usage Notes

Syntax DBMS_AQADM.STOP_QUEUE ( queue_name IN VARCHAR2, enqueue IN BOOLEAN DEFAULT TRUE, dequeue IN BOOLEAN DEFAULT TRUE, wait IN BOOLEAN DEFAULT TRUE, free_memory IN BOOLEAN DEFAULT FALSE); Parameters Table 23-57 STOP_QUEUE Procedure Parameters Parameter Description queue_name Name of the queue to be disabled enqueue Specifies whether ENQUEUE should be disabled on this queue. TRUE means disable ENQUEUE . This is the default. FALSE means do not alter the current setting. dequeue Specifies whether DEQUEUE should be disabled on this queue. TRUE means disable DEQUEUE . This is the default. FALSE means do not alter the current setting. wait Specifies whether to wait for the completion of outstanding transactions. TRUE means wait if there are any outstanding transactions. In this state no new transactions are allowed to enqueue to or dequeue from this queue. FALSE means return immediately either with a success or an error. free_memory Specifies whether the queue should be stopped. Usage Notes By default, this call disables both ENQUEUE and DEQUEUE . A queue cannot be stopped if there are outstanding transactions against the queue. This operation takes effect when the call completes and does not have any transactional characteristics.