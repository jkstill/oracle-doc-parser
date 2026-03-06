---
id: 19c__ALL_SCHEDULER_RESOURCES
name: ALL_SCHEDULER_RESOURCES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_RESOURCES.html
---

# ALL_SCHEDULER_RESOURCES

ALL_SCHEDULER_RESOURCES displays all scheduler resource objects in the database that are accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the resource object |
| RESOURCE_NAME | VARCHAR2(128) | Name of the resource object |
| STATUS | VARCHAR2(19) | Resource status for resource object. |
| RESOURCE_UNITS | NUMBER | Maximum number of available units for the resource object |
| UNITS_USED | NUMBER | Current number of resource units in use for the resource object |
| JOBS_RUNNING_COUNT | NUMBER | Current number of running jobs using the resource object |
| COMMENTS | VARCHAR2(256) | Comments for the resource object |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SCHEDULER_RESOURCES displays all scheduler resource objects in the database. USER_SCHEDULER_RESOURCES displays all scheduler resource objects in the database from the schema of the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_RESOURCES " " USER_SCHEDULER_RESOURCES " See Also: " DBA_SCHEDULER_RESOURCES " " USER_SCHEDULER_RESOURCES "