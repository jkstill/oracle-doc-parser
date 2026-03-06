---
id: 19c__ALL_SQL_TRANSLATION_PROFILES
name: ALL_SQL_TRANSLATION_PROFILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_SQL_TRANSLATION_PROFILES.html
---

# ALL_SQL_TRANSLATION_PROFILES

ALL_SQL_TRANSLATION_PROFILES describes all SQL translation profiles accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the SQL translation profile |
| PROFILE_NAME | VARCHAR2(128) | Name of the SQL translation profile |
| TRANSLATOR | VARCHAR2(261) | The translator package |
| FOREIGN_SQL_SYNTAX | VARCHAR2(5) | Indicates whether the SQL syntax is foreign. Possible values: TRUE FALSE |
| TRANSLATE_NEW_SQL | VARCHAR2(5) | Indicates whether to translate new SQL statements and errors using the translator. Possible values: TRUE FALSE |
| RAISE_TRANSLATION_ERROR | VARCHAR2(5) | Indicates whether to raise translation error. Possible values: TRUE FALSE |
| LOG_TRANSLATION_ERROR | VARCHAR2(5) | Indicates whether to log translation error. Possible values: TRUE FALSE |
| TRACE_TRANSLATION | VARCHAR2(5) | Indicates whether to trace translation. Possible values: TRUE FALSE |
| LOG_ERRORS | VARCHAR2(5) | Indicates whether there are log errors ( TRUE ) or not ( FALSE ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SQL_TRANSLATION_PROFILES describes all SQL translation profiles in the database. USER_SQL_TRANSLATION_PROFILES describes all SQL translation profiles owned by the user. This view does not display the OWNER column. See Also: " DBA_SQL_TRANSLATION_PROFILES " " USER_SQL_TRANSLATION_PROFILES " See Also: " DBA_SQL_TRANSLATION_PROFILES " " USER_SQL_TRANSLATION_PROFILES "