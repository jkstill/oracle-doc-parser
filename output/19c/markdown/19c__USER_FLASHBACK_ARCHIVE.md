---
id: 19c__USER_FLASHBACK_ARCHIVE
name: USER_FLASHBACK_ARCHIVE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_FLASHBACK_ARCHIVE.html
---

# USER_FLASHBACK_ARCHIVE

USER_FLASHBACK_ARCHIVE describes flashback data archives, which consist of multiple tablespaces and historic data from all transactions against tracked tables.

## Usage Notes

The content of this view depends on the privileges of the user who queries it, as follows: If the user has the FLASHBACK ARCHIVE ADMINISTER system privilege, then USER_FLASHBACK_ARCHIVE describes the flashback archives for all users who have been granted the FLASHBACK ARCHIVE object privilege. If the user does not have the FLASHBACK ARCHIVE ADMINISTER system privilege, then USER_FLASHBACK_ARCHIVE describes flashback archives for which the current user has been granted the FLASHBACK ARCHIVE object privilege. The columns of the USER_FLASHBACK_ARCHIVE view are the same as those in DBA_FLASHBACK_ARCHIVE . See Also: " DBA_FLASHBACK_ARCHIVE " See Also: " DBA_FLASHBACK_ARCHIVE "