---
id: 19c__DBMS_AQADM.DROP_SHARDED_QUEUE
name: DBMS_AQADM.DROP_SHARDED_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.DROP_SHARDED_QUEUE

This procedure drops an existing sharded queue from the database queuing system.

## Syntax

```sql
DBMS_AQADM.DROP_SHARDED_QUEUE( 
       queue_name IN VARCHAR2, 
       force      IN BOOLEAN DEFAULT FALSE )
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | This required parameter specifies the name of the sharded queue. |
| force | BOOLEAN | IN | The sharded queue is dropped even if the queue is not stopped. |

## Usage Notes

You must stop the queue before calling DROP_SHARDED_QUEUE . User must stop the queue explicitly if force is set to FALSE before calling DROP_SHARDED_QUEUE . If force is set to TRUE then queue will be stopped internally and then dropped. Syntax DBMS_AQADM.DROP_SHARDED_QUEUE( queue_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE ) Parameters Table 23-31 DROP_SHARDED_QUEUE Procedure Parameters Parameter Description queue_name This required parameter specifies the name of the sharded queue. force The sharded queue is dropped even if the queue is not stopped.