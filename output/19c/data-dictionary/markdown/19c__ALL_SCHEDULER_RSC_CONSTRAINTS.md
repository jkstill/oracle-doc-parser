---
id: 19c__ALL_SCHEDULER_RSC_CONSTRAINTS
name: ALL_SCHEDULER_RSC_CONSTRAINTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: integrity
tags: [all]
source_file: ALL_SCHEDULER_RSC_CONSTRAINTS.html
---

# ALL_SCHEDULER_RSC_CONSTRAINTS

ALL_SCHEDULER_RSC_CONSTRAINTS lists all Oracle Scheduler resource constraint members accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the resource object the member is in |
| OBJECT_NAME | VARCHAR2(128) | Name of the resource object the member is in |
| RESOURCE_OWNER | VARCHAR2(128) | Owner of the resource constraint resource member |
| RESOURCE_NAME | VARCHAR2(128) | Name of the resource constraint resource member |
| UNITS_USED | NUMBER | Number of units used of the resource by this constraint resource member |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SCHEDULER_RSC_CONSTRAINTS lists all Oracle Scheduler resource constraint members in the database. USER_SCHEDULER_RSC_CONSTRAINTS lists all Oracle Scheduler resource constraint members owned by the current user. See Also: " DBA_SCHEDULER_RSC_CONSTRAINTS " " USER_SCHEDULER_RSC_CONSTRAINTS " See Also: " DBA_SCHEDULER_RSC_CONSTRAINTS " " USER_SCHEDULER_RSC_CONSTRAINTS "