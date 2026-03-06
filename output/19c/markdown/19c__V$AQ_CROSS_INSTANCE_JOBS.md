---
id: 19c__V$AQ_CROSS_INSTANCE_JOBS
name: V$AQ_CROSS_INSTANCE_JOBS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_CROSS_INSTANCE_JOBS.html
---

# V$AQ_CROSS_INSTANCE_JOBS

V$AQ_CROSS_INSTANCE_JOBS describes each of the cross process jobs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER |  |
| SCHEMA_NAME | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| SHARD_ID | NUMBER |  |
| START_SUBSHARD_ID | NUMBER |  |
| DESTINATION_INSTANCE_ID | NUMBER |  |
| COORDINATOR_ID | NUMBER |  |
| DEST_SERVER_PROCESS_ID | NUMBER |  |
| JOB_STATE | VARCHAR2(28) |  |
| FLOW_CONTROL | NUMBER |  |
| MSGS_SENT | NUMBER |  |
| BYTES_SENT | NUMBER |  |
| ACK_LATENCY | NUMBER |  |
| JOB_TYPE | VARCHAR2(26) |  |
| PRIORITY0_CROSS_LWM | NUMBER |  |
| PRIORITY1_CROSS_LWM | NUMBER |  |
| PRIORITY2_CROSS_LWM | NUMBER |  |
| PRIORITY3_CROSS_LWM | NUMBER |  |
| PRIORITY4_CROSS_LWM | NUMBER |  |
| PRIORITY5_CROSS_LWM | NUMBER |  |
| PRIORITY6_CROSS_LWM | NUMBER |  |
| PRIORITY7_CROSS_LWM | NUMBER |  |
| PRIORITY8_CROSS_LWM | NUMBER |  |
| PRIORITY9_CROSS_LWM | NUMBER |  |
| JOB_START_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| SUBSCRIBER_ID | NUMBER |  |
| SUBSCRIBER_NAME | VARCHAR2(512) |  |
| OWNER_INSTANCE_ID | NUMBER |  |
| QUEUE_ID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Each job serves to forward messages for a shard from a source instance to a destination instance for a set of subscribers of a sharded queue. See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing