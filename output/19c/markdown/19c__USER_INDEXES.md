---
id: 19c__USER_INDEXES
name: USER_INDEXES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [user]
source_file: USER_INDEXES.html
---

# USER_INDEXES

USER_INDEXES describes indexes owned by the current user. To gather statistics for this view, use the DBMS_STATS package. This view supports parallel partitioned index scans. Its columns (except for OWNER ) are the same as those in ALL_INDEXES .

## Usage Notes

See Also: " ALL_INDEXES " See Also: " ALL_INDEXES "