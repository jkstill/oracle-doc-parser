---
id: 19c__DBA_WI_CAPTURE_FILES
name: DBA_WI_CAPTURE_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WI_CAPTURE_FILES.html
---

# DBA_WI_CAPTURE_FILES

Each row in DBA_WI_CAPTURE_FILES represents a capture file that belongs to the workload analyzed in the current Workload Intelligence job.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The identifier of the job in the workload to which the given capture file belongs |
| FILE_ID | NUMBER | The identifier of the current capture file |
| FILE_PATH | VARCHAR2(4000) | The path of the current capture file |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content