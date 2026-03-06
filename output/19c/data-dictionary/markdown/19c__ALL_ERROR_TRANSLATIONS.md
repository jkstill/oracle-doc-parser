---
id: 19c__ALL_ERROR_TRANSLATIONS
name: ALL_ERROR_TRANSLATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ERROR_TRANSLATIONS.html
---

# ALL_ERROR_TRANSLATIONS

ALL_ERROR_TRANSLATIONS describes all error translations accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the SQL translation profile |
| PROFILE_NAME | VARCHAR2(128) | Name of the SQL translation profile |
| ERROR_CODE | NUMBER | The Oracle error code |
| TRANSLATED_CODE | NUMBER | The translated error code |
| TRANSLATED_SQLSTATE | VARCHAR2(5) | The translated SQLSTATE |
| ENABLED | VARCHAR2(5) | TRUE if the translation is enabled, FALSE otherwise. |
| REGISTRATION_TIME | TIMESTAMP(6) | Time the translation was registered |
| COMMENTS | VARCHAR2(4000) | Comment on the translation |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ERROR_TRANSLATIONS describes all error translations in the database. USER_ERROR_TRANSLATIONS describes all error translations owned by the user. This view does not display the OWNER column. See Also: " DBA_ERROR_TRANSLATIONS " " USER_ERROR_TRANSLATIONS " See Also: " DBA_ERROR_TRANSLATIONS " " USER_ERROR_TRANSLATIONS "