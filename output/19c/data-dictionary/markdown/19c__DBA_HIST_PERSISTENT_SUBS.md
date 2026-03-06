---
id: 19c__DBA_HIST_PERSISTENT_SUBS
name: DBA_HIST_PERSISTENT_SUBS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_PERSISTENT_SUBS.html
---

# DBA_HIST_PERSISTENT_SUBS

DBA_HIST_PERSISTENT_SUBS displays Oracle Database AQ persistent queue subscribers historical statistics information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| QUEUE_SCHEMA | VARCHAR2(128) | Owner of the queue |
| QUEUE_NAME | VARCHAR2(128) | Name of the queue |
| SUBSCRIBER_ID | NUMBER | Internal subscriber number |
| SUBSCRIBER_NAME | VARCHAR2(128) | Name of the subscriber |
| SUBSCRIBER_ADDRESS | VARCHAR2(1024) | Address of the subscribing agent |
| SUBSCRIBER_TYPE | VARCHAR2(128) | Type of the subscriber: PROXY - Propagation subscriber SUBSCRIBER - Normal subscriber RECIPIENT - Recipient |
| FIRST_ACTIVITY_TIME | TIMESTAMP(6) | First subscriber activity time since database startup |
| ENQUEUED_MSGS | NUMBER | Number of messages enqueued since FIRST_ACTIVITY_TIME |
| DEQUEUED_MSGS | NUMBER | Number of messages dequeued since FIRST_ACTIVITY_TIME |
| AVG_MSG_AGE | NUMBER | Average age of messages in the queue |
| BROWSED_MSGS | NUMBER | Number of messages that have been browsed |
| EXPIRED_MSGS | NUMBER | Number of messages expired since FIRST_ACTIVITY_TIME |
| DEQUEUED_MSG_LATENCY | NUMBER | Last dequeued message latency (in seconds) |
| LAST_ENQUEUE_TIME | TIMESTAMP(6) | Timestamp of the last enqueued message |
| LAST_DEQUEUE_TIME | TIMESTAMP(6) | Timestamp of the last dequeued message |
| ELAPSED_DEQUEUE_TIME | NUMBER | Total time spent in dequeue (in hundredths of a second) |
| DEQUEUE_CPU_TIME | NUMBER | Total CPU time for dequeue (in hundredths of a second) |
| DEQUEUE_TRANSACTIONS | NUMBER | Number of dequeue transactions |
| EXECUTION_COUNT | NUMBER | Number of executions of the dequeue index cursor |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$PERSISTENT_SUBSCRIBERS . See Also: " V$PERSISTENT_SUBSCRIBERS " See Also: " V$PERSISTENT_SUBSCRIBERS "