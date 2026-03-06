---
id: 19c__V$SERVICE_REGION_METRIC
name: V$SERVICE_REGION_METRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SERVICE_REGION_METRIC.html
---

# V$SERVICE_REGION_METRIC

V$SERVICE_REGION_METRIC displays the metric values captured for the most recent 30-second intervals for the workload against each service region available on the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| SERVICE_ID | NUMBER |  |
| SERVICE_NETWORK_NAME | VARCHAR2(512) |  |
| REGION_NAME | VARCHAR2(30) |  |
| CALLSPERSEC | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$CHUNK_METRIC " See Also: " V$CHUNK_METRIC "