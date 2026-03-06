---
id: 19c__DBA_WI_OBJECTS
name: DBA_WI_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_WI_OBJECTS.html
---

# DBA_WI_OBJECTS

Each row in DBA_WI_OBJECTS represents a database object (table) that is accessed by the given template in the given Workload Intelligence job.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The identifier of the job in the workload of which the given object has been accessed |
| TEMPLATE_ID | NUMBER | The identifier of the template in the given job by which the current object has been accessed |
| OBJECT_ID | NUMBER | The identifier of the current object |
| ACCESS_TYPE | VARCHAR2(2) | Possible values: R - Indicates that the current object has been accessed for reading by the given template W - Indicates that the current object has been accessed for writing by the given template RW - Indicates that the current object has been accessed for both reading and writing by the given template |