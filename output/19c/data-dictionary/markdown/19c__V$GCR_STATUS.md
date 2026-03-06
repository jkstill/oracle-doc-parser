---
id: 19c__V$GCR_STATUS
name: V$GCR_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-GCR_STATUS.html
---

# V$GCR_STATUS

V$GCR_STATUS provides information on the current GCR status, what metrics ran and their result. It records the last 100 events.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER |  |
| ITERATION | NUMBER |  |
| TIME | TIMESTAMP(6) |  |
| TYPE | VARCHAR2(14) |  |
| DESCRIPTION | VARCHAR2(40) |  |
| RESULT | VARCHAR2(7) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content