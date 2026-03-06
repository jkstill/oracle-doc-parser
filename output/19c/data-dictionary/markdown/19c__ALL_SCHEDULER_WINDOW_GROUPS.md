---
id: 19c__ALL_SCHEDULER_WINDOW_GROUPS
name: ALL_SCHEDULER_WINDOW_GROUPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_WINDOW_GROUPS.html
---

# ALL_SCHEDULER_WINDOW_GROUPS

ALL_SCHEDULER_WINDOW_GROUPS displays information about the Scheduler window groups accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WINDOW_GROUP_NAME | VARCHAR2(128) | Name of the window group |
| ENABLED | VARCHAR2(5) | Indicates whether the window group is enabled ( TRUE ) or disabled ( FALSE ) |
| NUMBER_OF_WINDOWS | NUMBER | Number of members in the window group |
| NEXT_START_DATE | VARCHAR2(64) | If a window group is disabled, then this column will be NULL. Otherwise, it will be set to the earliest NEXT_START_DATE from the enabled windows in the group. |
| COMMENTS | VARCHAR2(4000) | Optional comment about the window group |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_SCHEDULER_WINDOW_GROUPS displays information about all Scheduler window groups in the database. See Also: " DBA_SCHEDULER_WINDOW_GROUPS " See Also: " DBA_SCHEDULER_WINDOW_GROUPS "