---
id: 19c__ALL_SCHEDULER_GROUPS
name: ALL_SCHEDULER_GROUPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_GROUPS.html
---

# ALL_SCHEDULER_GROUPS

ALL_SCHEDULER_GROUPS displays information about the Scheduler object groups accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the group |
| GROUP_NAME | VARCHAR2(128) | Name of the group |
| GROUP_TYPE | VARCHAR2(13) | Type of object contained in the group: WINDOW JOB DB_DEST EXTERNAL_DEST |
| ENABLED | VARCHAR2(5) | Indicates whether the group is enabled ( TRUE ) or disabled ( FALSE ) |
| NUMBER_OF_MEMBERS | NUMBER | Number of members in this group |
| COMMENTS | VARCHAR2(4000) | An optional comment about this group |

## Usage Notes

Related Views DBA_SCHEDULER_GROUPS displays information about all Scheduler object groups in the database. USER_SCHEDULER_GROUPS displays information about the Scheduler object groups owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_GROUPS " " USER_SCHEDULER_GROUPS " See Also: " DBA_SCHEDULER_GROUPS " " USER_SCHEDULER_GROUPS "