---
id: 19c__V$SHARED_SERVER_STAT
name: V$SHARED_SERVER_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SHARED_SERVER_STAT.html
---

# V$SHARED_SERVER_STAT

V$SHARED_SERVER_STAT displays statistics for all shared server processes. The statistics are cumulative from the start of the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MESSAGES | NUMBER |  |
| BYTES | NUMBER |  |
| IDLE | NUMBER |  |
| BUSY | NUMBER |  |
| IN_NET | NUMBER |  |
| OUT_NET | NUMBER |  |
| REQUESTS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Column Datatype Description MESSAGES NUMBER Number of messages processed BYTES NUMBER Total number of bytes in all messages IDLE NUMBER Total idle time (in hundredths of a second) BUSY NUMBER Total busy time (in hundredths of a second) IN_NET NUMBER Total incoming network wait time (in hundredths of a second) OUT_NET NUMBER Total outgoing network wait time (in hundredths of a second) REQUESTS NUMBER Total number of requests taken from the common queue CON_ID NUMBER The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data Note: This view is available starting with Oracle Database release 19c, version 19.1. Note: This view is available starting with Oracle Database release 19c, version 19.1.