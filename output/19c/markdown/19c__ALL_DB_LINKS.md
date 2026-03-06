---
id: 19c__ALL_DB_LINKS
name: ALL_DB_LINKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DB_LINKS.html
---

# ALL_DB_LINKS

ALL_DB_LINKS describes the database links accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the database link |
| DB_LINK | VARCHAR2(128) | Name of the database link |
| USERNAME | VARCHAR2(128) | Name of the user when logging in |
| HOST | VARCHAR2(2000) | Oracle Net connect string |
| CREATED | DATE | Creation time of the database link |
| HIDDEN | VARCHAR2(3) | For internal use only |
| SHARD_INTERNAL | VARCHAR2(3) | Indicates whether the database link is used to support operations across sharded databases. Possible values: YES : The database link is used and managed for to support sharded databases NO : The database link is not used and managed to support sharded databases Users should not alter or delete database links that are used and managed to support sharded databases. |
| VALID | VARCHAR2(3) | Indicates whether the database link is valid and usable. Possible values: YES : The database link is valid and usable. NO : The database link is invalid and unusable. |
| INTRA_CDB Foot 1 | VARCHAR2(3) | For internal use only |

## Usage Notes

Related Views DBA_DB_LINKS describes all database links in the database. USER_DB_LINKS describes the database links owned by the current user. This view does not display the OWNER column. See Also: " DBA_DB_LINKS " " USER_DB_LINKS " " DBA_DB_LINK_SOURCES " " DBA_EXTERNAL_SCN_ACTIVITY " See Also: " DBA_DB_LINKS " " USER_DB_LINKS " " DBA_DB_LINK_SOURCES " " DBA_EXTERNAL_SCN_ACTIVITY "