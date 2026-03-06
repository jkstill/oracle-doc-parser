---
id: 19c__V$INSTANCE_PING
name: V$INSTANCE_PING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-INSTANCE_PING.html
---

# V$INSTANCE_PING

V$INSTANCE_PING provides information about measured latency of the interconnect for all instances in an Oracle Real Application Clusters (Oracle RAC) environment.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INSTANCE | NUMBER |  |
| CURRENT_500B | NUMBER |  |
| AVERAGE_500B | NUMBER |  |
| MAX_500B | NUMBER |  |
| COUNT_500B | NUMBER |  |
| WAIT_TIME_500B | NUMBER |  |
| WAIT_TIME_SQUARED_500B | NUMBER |  |
| CURRENT_8K | NUMBER |  |
| AVERAGE_8K | NUMBER |  |
| MAX_8K | NUMBER |  |
| COUNT_8K | NUMBER |  |
| WAIT_TIME_8K | NUMBER |  |
| WAIT_TIME_SQUARED_8K | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

In an Oracle RAC environment, every few seconds the PING process of each instance checks the response of the interconnect to all instances of the same database. It sends two messages. One message is 500 bytes in size (referred to in the column descriptions as 500B), and the other is 8 kilobytes in size (referred to in column descriptions as 8K). For each message sent to each instance, the amount of time it took to get a response back is measured (in microseconds). The view records the latest measurements as well as cumulative data since instance startup.