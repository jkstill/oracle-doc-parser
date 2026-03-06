---
id: 19c__USER_MVIEW_ANALYSIS
name: USER_MVIEW_ANALYSIS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_MVIEW_ANALYSIS.html
---

# USER_MVIEW_ANALYSIS

USER_MVIEW_ANALYSIS describes all materialized views owned by the current user that potentially support query rewrite and that provide additional information for analysis by applications. Its columns are the same as those in ALL_MVIEW_ANALYSIS .

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view excludes materialized views that reference remote tables or that include references to non-static values such as SYSDATE or USER . This view also excludes materialized views that were created as snapshots before Oracle8 i and that were never altered to enable query rewrite. See Also: " ALL_MVIEW_ANALYSIS " Note: This view excludes materialized views that reference remote tables or that include references to non-static values such as SYSDATE or USER . This view also excludes materialized views that were created as snapshots before Oracle8 i and that were never altered to enable query rewrite. See Also: " ALL_MVIEW_ANALYSIS "