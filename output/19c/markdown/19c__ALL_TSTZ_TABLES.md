---
id: 19c__ALL_TSTZ_TABLES
name: ALL_TSTZ_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_TSTZ_TABLES.html
---

# ALL_TSTZ_TABLES

ALL_TSTZ_TABLES displays information about the tables accessible to the current user, which have columns defined on TIMESTAMP WITH TIME ZONE data types or object types containing attributes of TIMESTAMP WITH TIME ZONE data types.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| UPGRADE_IN_PROGRESS | VARCHAR2(3) | Indicates whether a table upgrade is in progress ( YES ) or not ( NO ) |

## Usage Notes

Related Views DBA_TSTZ_TABLES displays information about all tables in the database, which have columns defined on TIMESTAMP WITH TIME ZONE data types or object types containing attributes of TIMESTAMP WITH TIME ZONE data types. USER_TSTZ_TABLES displays information about the tables owned by the current user, which have columns defined on TIMESTAMP WITH TIME ZONE data types or object types containing attributes of TIMESTAMP WITH TIME ZONE data types. This view does not display the OWNER column. See Also: " DBA_TSTZ_TABLES " " USER_TSTZ_TABLES " See Also: " DBA_TSTZ_TABLES " " USER_TSTZ_TABLES "