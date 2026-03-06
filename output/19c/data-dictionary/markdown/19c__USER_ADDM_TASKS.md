---
id: 19c__USER_ADDM_TASKS
name: USER_ADDM_TASKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_ADDM_TASKS.html
---

# USER_ADDM_TASKS

USER_ADDM_TASKS displays information about the ADDM tasks owned by the current user.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The view contains one row for each row in the related USER_ADVISOR_TASKS view that has ADVISOR_NAME=ADDM and STATUS=COMPLETED . Its columns (except for OWNER ) are the same as those in DBA_ADDM_TASKS . See Also: " DBA_ADDM_TASKS " See Also: " DBA_ADDM_TASKS "