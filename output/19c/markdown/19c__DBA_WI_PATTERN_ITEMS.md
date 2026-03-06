---
id: 19c__DBA_WI_PATTERN_ITEMS
name: DBA_WI_PATTERN_ITEMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WI_PATTERN_ITEMS.html
---

# DBA_WI_PATTERN_ITEMS

Each row in DBA_WI_PATTERN_ITEMS represents a template that participates in a significant pattern that has been found by the given Workload Intelligence job.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The identifier of the job in the workload of which the current pattern has been found |
| PATTERN_ID | NUMBER | The identifier of the pattern to which the current item (template) belongs |
| SEQUENCE_NUMBER | NUMBER | Number that indicates the position of the current item in the given pattern |
| TEMPLATE_ID | NUMBER | The identifier of the template that participates in the given position of the current pattern |
| IS_FIRST_IN_LOOP | CHAR(1) | A flag that indicates whether or not the current item marks the beginning of a loop in the given pattern. The possible values are Y and N . |
| IS_LAST_IN_LOOP | CHAR(1) | A flag that indicates whether or not the current item marks the end of a loop in the given pattern. The possible values are Y and N . |