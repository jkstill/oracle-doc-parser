---
id: 19c__DBA_WI_TEMPLATE_EXECUTIONS
name: DBA_WI_TEMPLATE_EXECUTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WI_TEMPLATE_EXECUTIONS.html
---

# DBA_WI_TEMPLATE_EXECUTIONS

Each row in DBA_WI_TEMPLATE_EXECUTIONS represents an execution of a template in a capture that belongs to the workload that is associated with the current Workload Intelligence job.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The identifier of the job in the workload of which the current execution of the given template belongs |
| CAPTURE_FILE_ID | NUMBER | The identifier of the capture file in which the current execution of the given template was found |
| SEQUENCE_NUMBER | NUMBER | A number that indicates the order of the current execution in the given capture file |
| TEMPLATE_ID | NUMBER | The identifier of the template that was executed in the execution represented by the current row |
| DB_TIME | NUMBER | The time that the current execution consumed on the database server |