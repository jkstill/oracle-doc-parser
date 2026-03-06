---
id: 19c__DBMS_XSTREAM_ADM.REMOVE_QUEUE
name: DBMS_XSTREAM_ADM.REMOVE_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.REMOVE_QUEUE

This procedure removes the specified ANYDATA queue.

## Syntax

```sql
DBMS_XSTREAM_ADM.REMOVE_QUEUE(
   queue_name               IN  VARCHAR2,
   cascade                  IN  BOOLEAN  DEFAULT FALSE,
   drop_unused_queue_table  IN  BOOLEAN  DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | The name of the queue to remove, specified as [ schema_name .] queue_name . For example, strmadmin.streams_queue . If the schema is not specified, then the current user is the default. |
| cascade | BOOLEAN | IN | If TRUE , then the procedure drops any XStream clients that use the queue. If FALSE , then the procedure raises an error if there are any XStream clients that use the queue. Before you run this procedure with the cascade parameter set to FALSE , make sure no XStream clients are using the queue currently. |
| drop_unused_queue_table | BOOLEAN | IN | If TRUE and the queue table for the queue is empty, then the procedure drops the queue table. The queue table is not dropped if it contains any messages or if it is used by another queue. If FALSE , then the procedure does not drop the queue table. |

## Usage Notes

Specifically, this procedure performs the following actions: Waits until all current enqueue and dequeue transactions commit. Stops the queue, which means that no further enqueues into the queue or dequeues from the queue are allowed. Drops the queue. If the drop_unused_queue_table parameter is set to TRUE , then drops the queue table if it is empty and no other queues are using it. If the cascade parameter is set to TRUE , then drops all of the XStream clients that are using the queue. Note: The specified queue must be a ANYDATA queue. Note: The specified queue must be a ANYDATA queue. Syntax DBMS_XSTREAM_ADM.REMOVE_QUEUE( queue_name IN VARCHAR2, cascade IN BOOLEAN DEFAULT FALSE, drop_unused_queue_table IN BOOLEAN DEFAULT TRUE); Parameters Table 217-26 REMOVE_QUEUE Procedure Parameters Parameter Description queue_name The name of the queue to remove, specified as [ schema_name .] queue_name . For example, strmadmin.streams_queue . If the schema is not specified, then the current user is the default. cascade If TRUE , then the procedure drops any XStream clients that use the queue. If FALSE , then the procedure raises an error if there are any XStream clients that use the queue. Before you run this procedure with the cascade parameter set to FALSE , make sure no XStream clients are using the queue currently. drop_unused_queue_table If TRUE and the queue table for the queue is empty, then the procedure drops the queue table. The queue table is not dropped if it contains any messages or if it is used by another queue. If FALSE , then the procedure does not drop the queue table.