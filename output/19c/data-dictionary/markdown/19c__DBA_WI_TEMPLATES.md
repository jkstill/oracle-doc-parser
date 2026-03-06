---
id: 19c__DBA_WI_TEMPLATES
name: DBA_WI_TEMPLATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WI_TEMPLATES.html
---

# DBA_WI_TEMPLATES

Each row in DBA_WI_TEMPLATES describes a template that has been found in the workload that is related to the Workload Intelligence job whose identifier is equal to JOB_ID .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The identifier of the job in the workload of which the given template has been found |
| TEMPLATE_ID | NUMBER | The identifier of a template in a given job |
| IS_TRANSACTION | CHAR(1) | Flag that indicates whether the given template represents a transaction: Y - indicates that the given template represents a transaction N - indicates that the given template does not represent a transaction |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content A template can represent either a simple query, or an entire transaction. Two queries in the given workload belong to the same template, if they exhibit trivial differences, for example, if they contain different literal values, different bind variable names, different comments, or different white spaces.