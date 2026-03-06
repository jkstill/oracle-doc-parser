---
id: 19c__V$DISPATCHER_RATE
name: V$DISPATCHER_RATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DISPATCHER_RATE.html
---

# V$DISPATCHER_RATE

V$DISPATCHER_RATE displays rate statistics for a number of activities performed by the dispatcher processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(4) |  |
| PADDR | RAW(4 | 8) |  |
| CUR_LOOP_RATE | NUMBER |  |
| CUR_EVENT_RATE | NUMBER |  |
| CUR_EVENTS_PER_LOOP | NUMBER |  |
| CUR_MSG_RATE | NUMBER |  |
| CUR_SVR_BUF_RATE | NUMBER |  |
| CUR_SVR_BYTE_RATE | NUMBER |  |
| CUR_SVR_BYTE_PER_BUF | NUMBER |  |
| CUR_CLT_BUF_RATE | NUMBER |  |
| CUR_CLT_BYTE_RATE | NUMBER |  |
| CUR_CLT_BYTE_PER_BUF | NUMBER |  |
| CUR_BUF_RATE | NUMBER |  |
| CUR_BYTE_RATE | NUMBER |  |
| CUR_BYTE_PER_BUF | NUMBER |  |
| CUR_IN_CONNECT_RATE | NUMBER |  |
| CUR_OUT_CONNECT_RATE | NUMBER |  |
| CUR_RECONNECT_RATE | NUMBER |  |
| MAX_LOOP_RATE | NUMBER |  |
| MAX_EVENT_RATE | NUMBER |  |
| MAX_EVENTS_PER_LOOP | NUMBER |  |
| MAX_MSG_RATE | NUMBER |  |
| MAX_SVR_BUF_RATE | NUMBER |  |
| MAX_SVR_BYTE_RATE | NUMBER |  |
| MAX_SVR_BYTE_PER_BUF | NUMBER |  |
| MAX_CLT_BUF_RATE | NUMBER |  |
| MAX_CLT_BYTE_RATE | NUMBER |  |
| MAX_CLT_BYTE_PER_BUF | NUMBER |  |
| MAX_BUF_RATE | NUMBER |  |
| MAX_BYTE_RATE | NUMBER |  |
| MAX_BYTE_PER_BUF | NUMBER |  |
| MAX_IN_CONNECT_RATE | NUMBER |  |
| MAX_OUT_CONNECT_RATE | NUMBER |  |
| MAX_RECONNECT_RATE | NUMBER |  |
| AVG_LOOP_RATE | NUMBER |  |
| AVG_EVENT_RATE | NUMBER |  |
| AVG_EVENTS_PER_LOOP | NUMBER |  |
| AVG_MSG_RATE | NUMBER |  |
| AVG_SVR_BUF_RATE | NUMBER |  |
| AVG_SVR_BYTE_RATE | NUMBER |  |
| AVG_SVR_BYTE_PER_BUF | NUMBER |  |
| AVG_CLT_BUF_RATE | NUMBER |  |
| AVG_CLT_BYTE_RATE | NUMBER |  |
| AVG_CLT_BYTE_PER_BUF | NUMBER |  |
| AVG_BUF_RATE | NUMBER |  |
| AVG_BYTE_RATE | NUMBER |  |
| AVG_BYTE_PER_BUF | NUMBER |  |
| AVG_IN_CONNECT_RATE | NUMBER |  |
| AVG_OUT_CONNECT_RATE | NUMBER |  |
| AVG_RECONNECT_RATE | NUMBER |  |
| TTL_LOOPS | NUMBER |  |
| TTL_MSG | NUMBER |  |
| TTL_SVR_BUF | NUMBER |  |
| TTL_CLT_BUF | NUMBER |  |
| TTL_BUF | NUMBER |  |
| TTL_IN_CONNECT | NUMBER |  |
| TTL_OUT_CONNECT | NUMBER |  |
| TTL_RECONNECT | NUMBER |  |
| SCALE_LOOPS | NUMBER |  |
| SCALE_MSG | NUMBER |  |
| SCALE_SVR_BUF | NUMBER |  |
| SCALE_CLT_BUF | NUMBER |  |
| SCALE_BUF | NUMBER |  |
| SCALE_IN_CONNECT | NUMBER |  |
| SCALE_OUT_CONNECT | NUMBER |  |
| SCALE_RECONNECT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Collected samples have an activity-specific "time-to-live" ( TTL_* columns). Statistics are reported over the following two types of time intervals: Current statistics ( CUR_ columns) Current statistics use samples collected over the most recent time-to-live interval. Historical statistics ( AVG_ and most of the MAX_ columns) Historical statistics make use of all samples that are no longer current. At the time of collection, a sample is current. After the time-to-live has elapsed, the sample becomes historical. Each type of activity has a specific scale (represented by the SCALE_* columns) at which the statistics are reported.