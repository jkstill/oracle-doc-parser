---
id: 19c__USER_OBJECT_USAGE
name: USER_OBJECT_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_OBJECT_USAGE.html
---

# USER_OBJECT_USAGE

USER_OBJECT_USAGE displays statistics about index usage gathered from the database for the indexes owned by the current user.

## Usage Notes

You can use this view to monitor index usage. All indexes owned by the current user that have been used at least once can be monitored and displayed in this view. Its columns (except for OWNER ) are the same as those in DBA_OBJECT_USAGE . See Also: " DBA_OBJECT_USAGE " See Also: " DBA_OBJECT_USAGE "