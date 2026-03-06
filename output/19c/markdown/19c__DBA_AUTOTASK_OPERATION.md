---
id: 19c__DBA_AUTOTASK_OPERATION
name: DBA_AUTOTASK_OPERATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AUTOTASK_OPERATION.html
---

# DBA_AUTOTASK_OPERATION

DBA_AUTOTASK_OPERATION displays all automated maintenance task operations for each client.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENT_NAME | VARCHAR2(64) | Name of the client |
| OPERATION_NAME | VARCHAR2(64) | Name of the operation |
| OPERATION_TAG | VARCHAR2(3) | Tag for the operation |
| PRIORITY_OVERRIDE | VARCHAR2(7) | User-specified priority at which the task executes: URGENT HIGH MEDIUM LOW |
| ATTRIBUTES | VARCHAR2(4000) | Attributes of the operation |
| USE_RESOURCE_ESTIMATES | VARCHAR2(5) | Indicates whether resource usage estimates are used for the operation ( TRUE ) or not ( FALSE ) |
| STATUS | VARCHAR2(8) | Job status: ENABLED DISABLED |
| LAST_CHANGE | TIMESTAMP(6) WITH TIME ZONE | Timestamp of the last change |