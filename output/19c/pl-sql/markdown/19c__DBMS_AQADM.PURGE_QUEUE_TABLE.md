---
id: 19c__DBMS_AQADM.PURGE_QUEUE_TABLE
name: DBMS_AQADM.PURGE_QUEUE_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.PURGE_QUEUE_TABLE

This procedure purges messages from queue tables. You can perform various purge operations on both single-consumer and multiconsumer queue tables for persistent and buffered messages.

## Syntax

```sql
DBMS_AQADM.PURGE_QUEUE_TABLE(
   queue_table        IN   VARCHAR2,
   purge_condition    IN   VARCHAR2,
   purge_options      IN   aq$_purge_options_t);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_table | VARCHAR2 | IN | Specifies the name of the queue table to be purged. |
| purge_condition | VARCHAR2 | IN | Specifies the purge condition to use when purging the queue table. The purge condition must be in the format of a SQL WHERE clause, and it is case-sensitive. The condition is based on the columns of aq$queue_table_name view. When specifying the purge_condition , qualify the column names in aq$queue_table_name view with qtview . To purge all queues in a queue table, set purge_condition to either NULL (a bare null word, no quotes) or '' (two single quotes). |
| purge_options | aq$_purge_options_t) | IN | Type aq$_purge_options_t contains a block parameter and a delivery_mode parameter. If block is TRUE , then an exclusive lock on all the queues in the queue table is held while purging the queue table. This will cause concurrent enqueuers and dequeuers to block while the queue table is purged. The purge call always succeeds if block is TRUE . The default for block is FALSE . This will not block enqueuers and dequeuers, but it can cause the purge to fail with an error during high concurrency times. delivery_mode is used to specify whether DBMS_AQADM.PERSISTENT , DBMS_AQADM.BUFFERED or DBMS_AQADM.PERSISTENT_OR_BUFFERED types of messages are to be purged. You cannot implement arbitrary purge conditions if buffered messages have to be purged. |

## Usage Notes

Syntax DBMS_AQADM.PURGE_QUEUE_TABLE( queue_table IN VARCHAR2, purge_condition IN VARCHAR2, purge_options IN aq$_purge_options_t); where type aq$_purge_options_t is described in Oracle Database Advanced Queuing (AQ) Types . Parameters Table 23-44 PURGE_QUEUE_TABLE Procedure Parameters Parameter Description queue_table Specifies the name of the queue table to be purged. purge_condition Specifies the purge condition to use when purging the queue table. The purge condition must be in the format of a SQL WHERE clause, and it is case-sensitive. The condition is based on the columns of aq$queue_table_name view. When specifying the purge_condition , qualify the column names in aq$queue_table_name view with qtview . To purge all queues in a queue table, set purge_condition to either NULL (a bare null word, no quotes) or '' (two single quotes). purge_options Type aq$_purge_options_t contains a block parameter and a delivery_mode parameter. If block is TRUE , then an exclusive lock on all the queues in the queue table is held while purging the queue table. This will cause concurrent enqueuers and dequeuers to block while the queue table is purged. The purge call always succeeds if block is TRUE . The default for block is FALSE . This will not block enqueuers and dequeuers, but it can cause the purge to fail with an error during high concurrency times. delivery_mode is used to specify whether DBMS_AQADM.PERSISTENT , DBMS_AQADM.BUFFERED or DBMS_AQADM.PERSISTENT_OR_BUFFERED types of messages are to be purged. You cannot implement arbitrary purge conditions if buffered messages have to be purged. Usage Notes You an purge selected messages from the queue table by specifying a purge_condition. Table 23-44 describes these parameters. Messages can be enqueued to and dequeued from the queue table while the queue table is being purged. A trace file is generated in the udump destination when you run this procedure. It details what the procedure is doing. This procedure commits batches of messages in autonomous transactions. Several such autonomous transactions may get executed as a part of one purge_queue_table call depending on the number of messages in the queue table.