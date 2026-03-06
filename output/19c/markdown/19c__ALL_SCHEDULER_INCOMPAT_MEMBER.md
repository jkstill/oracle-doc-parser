---
id: 19c__ALL_SCHEDULER_INCOMPAT_MEMBER
name: ALL_SCHEDULER_INCOMPAT_MEMBER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_INCOMPAT_MEMBER.html
---

# ALL_SCHEDULER_INCOMPAT_MEMBER

ALL_SCHEDULER_INCOMPAT_MEMBER displays all Scheduler incompatibility resource objects members accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INCOMPATIBILITY_OWNER | VARCHAR2(128) | Owner of the incompatibility resource object containing this member |
| INCOMPATIBILITY_NAME | VARCHAR2(128) | Name of the incompatibility resource object containing this member |
| OBJECT_OWNER | VARCHAR2(128) | Owner of the incompatibility resource member |
| OBJECT_NAME | VARCHAR2(128) | Name of the incompatibility resource member |

## Usage Notes

Related Views DBA_SCHEDULER_INCOMPAT_MEMBER displays all Scheduler incompatibility resource objects members in the database. USER_SCHEDULER_INCOMPAT_MEMBER displays all Scheduler incompatibility resource objects members owned by the current user. See Also: " DBA_SCHEDULER_INCOMPAT_MEMBER " " USER_SCHEDULER_INCOMPAT_MEMBER " See Also: " DBA_SCHEDULER_INCOMPAT_MEMBER " " USER_SCHEDULER_INCOMPAT_MEMBER "