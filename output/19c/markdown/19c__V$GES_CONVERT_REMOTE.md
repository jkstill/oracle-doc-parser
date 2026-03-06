---
id: 19c__V$GES_CONVERT_REMOTE
name: V$GES_CONVERT_REMOTE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GES_CONVERT_REMOTE.html
---

# V$GES_CONVERT_REMOTE

V$GES_CONVERT_REMOTE displays values for remote GES enqueue conversions. This view records average convert times, count information, and timed statistics for global enqueue requests.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER |  |
| CONVERT_TYPE | VARCHAR2(16) |  |
| AVERAGE_CONVERT_TIME | NUMBER |  |
| CONVERT_COUNT | NUMBER |  |
| CON_ID | NUMBER |  |