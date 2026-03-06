---
id: 19c__DBA_HIST_CHANNEL_WAITS
name: DBA_HIST_CHANNEL_WAITS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_CHANNEL_WAITS.html
---

# DBA_HIST_CHANNEL_WAITS

DBA_HIST_CHANNEL_WAITS display the amount of messages broadcast on KSR and KSXR channels as well as the total time taken for the broadcast to complete.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| CHANNEL | VARCHAR2(64) | The name of the KSR or KSXR channel |
| MESSAGES_PUBLISHED | NUMBER | The cumulative count of messages published on the channel (from instance startup) |
| WAIT_COUNT | NUMBER | The total number of times a publisher has waited for a broadcast to complete. This metric is only pertinent for asynchronous broadcasts where the broadcast can be dispatched and publisher can wait for completion at a later point of time. A high wait count along with increased wait time can indicate a potential performance bottleneck. |
| WAIT_TIME_USEC | NUMBER | The cumulative amount of time in microseconds that publishers have waited for message broadcast to complete. Average time for broadcast on a channel can be computed by dividing WAIT_TIME_USEC by WAIT_COUNT . A high average time can indicate a potential performance bottleneck. |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

KSR channels are local to an instance, that is, only processes within an instance subscribed to the channel can receive the message. KSXR channels allow messages to be broadcast across instances. The messages broadcast and the total time to broadcast are cumulative from the start of the instance. Channels with high overall average wait times could indicate potential problems with a subscriber on that channel which can lead to poor scaled performance.