---
id: 19c__DBMS_AQADM.START_QUEUE
name: DBMS_AQADM.START_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.START_QUEUE

This procedure enables the specified queue for enqueuing or dequeuing.

## Syntax

```sql
DBMS_AQADM.START_QUEUE ( 
   queue_name      IN     VARCHAR2,
   enqueue         IN     BOOLEAN DEFAULT TRUE,
   dequeue         IN     BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue to be enabled |
| enqueue | BOOLEAN | IN | Specifies whether ENQUEUE should be enabled on this queue. TRUE means enable ENQUEUE . This is the default. FALSE means do not alter the current setting. |
| dequeue | BOOLEAN | IN | Specifies whether DEQUEUE should be enabled on this queue. TRUE means enable DEQUEUE . This is the default. FALSE means do not alter the current setting. |

## Usage Notes

Syntax DBMS_AQADM.START_QUEUE ( queue_name IN VARCHAR2, enqueue IN BOOLEAN DEFAULT TRUE, dequeue IN BOOLEAN DEFAULT TRUE); Parameters Table 23-56 START_QUEUE Procedure Parameters Parameter Description queue_name Name of the queue to be enabled enqueue Specifies whether ENQUEUE should be enabled on this queue. TRUE means enable ENQUEUE . This is the default. FALSE means do not alter the current setting. dequeue Specifies whether DEQUEUE should be enabled on this queue. TRUE means enable DEQUEUE . This is the default. FALSE means do not alter the current setting. Usage Notes After creating a queue, the administrator must use START_QUEUE to enable the queue. The default is to enable it for both ENQUEUE and DEQUEUE . Only dequeue operations are allowed on an exception queue. This operation takes effect when the call completes and does not have any transactional characteristics.