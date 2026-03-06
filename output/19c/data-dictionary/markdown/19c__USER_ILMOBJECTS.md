---
id: 19c__USER_ILMOBJECTS
name: USER_ILMOBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_ILMOBJECTS.html
---

# USER_ILMOBJECTS

USER_ILMOBJECTS displays all the Automatic Data Optimization policies and objects for a user.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Many objects inherit policies via their parent objects or because they were created in a particular tablespace. This view provides a mapping between the policies and objects and indicates whether a policy is inherited by an object or is directly specified on it. Its columns are the same as those in DBA_ILMOBJECTS . Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. See Also: " DBA_ILMOBJECTS " Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. See Also: " DBA_ILMOBJECTS "