---
id: 19c__DBA_WI_JOBS
name: DBA_WI_JOBS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WI_JOBS.html
---

# DBA_WI_JOBS

Each row in DBA_WI_JOBS describes a Workload Intelligence job, that is, a task that applies the algorithms of Workload Intelligence on a given capture directory.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The job identifier |
| JOB_NAME | VARCHAR2(128) | A name that uniquely identifies the given job |
| CAPTURE_DIRECTORY | VARCHAR2(4000) | Path to the capture directory on which the given job has been applied |
| MODEL_ORDER | NUMBER | The order of the markov model that describes the workload associated with the current job. If NULL , the corresponding order has not been calculated yet. |
| THRESHOLD | NUMBER | A number in the range [0, 1] that represents the threshold that the user has given as an input parameter to the current job of Workload Intelligence for the identification of significant patterns. If NULL , the process of pattern identification has not been initiated yet. |