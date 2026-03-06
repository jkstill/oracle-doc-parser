---
id: 19c__ALL_TAB_STAT_PREFS
name: ALL_TAB_STAT_PREFS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_TAB_STAT_PREFS.html
---

# ALL_TAB_STAT_PREFS

ALL_TAB_STAT_PREFS displays information about statistics preferences for the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PREFERENCE_NAME | VARCHAR2(30) | Name of the preference |
| PREFERENCE_VALUE | VARCHAR2(4000) | Value of the preference |

## Usage Notes

Related Views DBA_TAB_STAT_PREFS displays information about statistics preferences for all tables in the database. USER_TAB_STAT_PREFS displays information about statistics preferences for the tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_TAB_STAT_PREFS " " USER_TAB_STAT_PREFS " See Also: " DBA_TAB_STAT_PREFS " " USER_TAB_STAT_PREFS "