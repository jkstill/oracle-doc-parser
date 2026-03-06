---
id: 19c__USER_MVREF_STATS_SYS_DEFAULTS
name: USER_MVREF_STATS_SYS_DEFAULTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_MVREF_STATS_SYS_DEFAULTS.html
---

# USER_MVREF_STATS_SYS_DEFAULTS

USER_MVREF_STATS_SYS_DEFAULTS displays the system-wide defaults for the refresh history statistics properties for materialized views accessible to the current user. These values can be altered with the SET_SYSTEM_DEFAULTS procedure by a database administrator.

## Usage Notes

Its columns are the same as those in DBA_MVREF_STATS_SYS_DEFAULTS . This view contains exactly two rows corresponding to the collection-level and retention-period properties; their initial values are TYPICAL and 31 respectively. See Also: " DBA_MVREF_STATS_SYS_DEFAULTS " See Also: " DBA_MVREF_STATS_SYS_DEFAULTS "