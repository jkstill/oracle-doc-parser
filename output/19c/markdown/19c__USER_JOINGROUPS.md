---
id: 19c__USER_JOINGROUPS
name: USER_JOINGROUPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_JOINGROUPS.html
---

# USER_JOINGROUPS

USER_JOINGROUPS describes join groups belonging to the user. A join group is a user-created object that consists of two or more columns that can be meaningfully joined. The maximum number of columns that can be included in a join group is 255. The USER_JOINGROUPS columns (except for JOINGROUP_OWNER ) are the same as those in DBA_JOINGROUPS .

## Usage Notes

In certain queries, join groups enable the database to eliminate the performance overhead of decompressing and hashing column values. Join groups require an In-Memory column store (IM column store). See Also: " DBA_JOINGROUPS " Oracle Database In-Memory Guide for an introduction to join groups Oracle Database SQL Language Reference for information about creating a join group using the CREATE INMEMORY JOIN GROUP statement See Also: " DBA_JOINGROUPS " Oracle Database In-Memory Guide for an introduction to join groups Oracle Database SQL Language Reference for information about creating a join group using the CREATE INMEMORY JOIN GROUP statement