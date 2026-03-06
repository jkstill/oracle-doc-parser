---
id: 19c__V$METRIC
name: V$METRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-METRIC.html
---

# V$METRIC

V$METRIC displays the most recent statistic values for the complete set of metrics captured by the Automatic Workload Repository (AWR) infrastructure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| GROUP_ID | NUMBER |  |
| ENTITY_ID | NUMBER |  |
| ENTITY_SEQUENCE | NUMBER |  |
| METRIC_ID | NUMBER |  |
| METRIC_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| METRIC_UNIT | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

The following table describes what the ENTITY_ID and ENTITY_SEQUENCE are for each metric group: