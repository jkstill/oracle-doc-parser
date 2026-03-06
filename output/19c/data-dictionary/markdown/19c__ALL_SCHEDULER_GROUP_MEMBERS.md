---
id: 19c__ALL_SCHEDULER_GROUP_MEMBERS
name: ALL_SCHEDULER_GROUP_MEMBERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_GROUP_MEMBERS.html
---

# ALL_SCHEDULER_GROUP_MEMBERS

ALL_SCHEDULER_GROUP_MEMBERS displays information about the members of the Scheduler object groups accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the group |
| GROUP_NAME | VARCHAR2(128) | Name of the group |
| MEMBER_NAME | VARCHAR2(523) | Name of the member of this group |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SCHEDULER_GROUP_MEMBERS displays information about the members of all Scheduler object groups in the database. USER_SCHEDULER_GROUP_MEMBERS displays information about the members of the Scheduler object groups owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_GROUP_MEMBERS " " USER_SCHEDULER_GROUP_MEMBERS " See Also: " DBA_SCHEDULER_GROUP_MEMBERS " " USER_SCHEDULER_GROUP_MEMBERS "