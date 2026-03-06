---
id: 19c__V$CHUNK_METRIC
name: V$CHUNK_METRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CHUNK_METRIC.html
---

# V$CHUNK_METRIC

V$CHUNK_METRIC displays the metric values captured for the most recent 30-second intervals for the workload against each chunk available on the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| CHUNK_ID | NUMBER |  |
| CALLSPERSEC | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$SERVICE_REGION_METRIC " See Also: " V$SERVICE_REGION_METRIC "