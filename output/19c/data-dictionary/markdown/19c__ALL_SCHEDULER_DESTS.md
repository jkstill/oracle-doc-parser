---
id: 19c__ALL_SCHEDULER_DESTS
name: ALL_SCHEDULER_DESTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_DESTS.html
---

# ALL_SCHEDULER_DESTS

ALL_SCHEDULER_DESTS displays information about the destination objects for jobs accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of this destination object |
| DESTINATION_NAME | VARCHAR2(128) | Name of this destination object |
| DESTINATION_TYPE | VARCHAR2(8) | Type of this destination object: EXTERNAL DATABASE |
| ENABLED | VARCHAR2(5) | Indicates whether this destination object is enabled ( TRUE ) or disabled ( FALSE ) |
| COMMENTS | VARCHAR2(4000) | Optional comment |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SCHEDULER_DESTS displays information about all destination objects for jobs in the database. USER_SCHEDULER_DESTS displays information about the destination objects for jobs owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_DESTS " " USER_SCHEDULER_DESTS " See Also: " DBA_SCHEDULER_DESTS " " USER_SCHEDULER_DESTS "