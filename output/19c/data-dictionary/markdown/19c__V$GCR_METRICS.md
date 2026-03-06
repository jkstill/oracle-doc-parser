---
id: 19c__V$GCR_METRICS
name: V$GCR_METRICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GCR_METRICS.html
---

# V$GCR_METRICS

V$GCR_METRICS displays information about the current status of the metrics defined to the GCR component that runs under the LMHB background process to detect and mitigate potential issues in the cluster instances.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| METRIC_ID | NUMBER |  |
| METRIC_NAME | VARCHAR2(40) |  |
| ENVIRONMENT | NUMBER |  |
| FREQUENCY | NUMBER |  |
| SCOPE | NUMBER |  |
| DATA_TYPE | VARCHAR2(7) |  |
| STATUS | VARCHAR2(9) |  |
| STATUS_CHANGE_TIME | TIMESTAMP(6) |  |
| LAST_RAN_ITERATION | NUMBER |  |
| LAST_RAN_TIME | TIMESTAMP(6) |  |
| LAST_PASS_ITERATION | NUMBER |  |
| LAST_PASS_TIME | TIMESTAMP(6) |  |
| TOTAL_PASSES | NUMBER |  |
| LAST_FAIL_ITERATION | NUMBER |  |
| LAST_FAIL_TIME | TIMESTAMP(6) |  |
| TOTAL_FAILS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content