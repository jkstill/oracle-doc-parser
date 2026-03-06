---
id: 19c__ALL_STAT_EXTENSIONS
name: ALL_STAT_EXTENSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_STAT_EXTENSIONS.html
---

# ALL_STAT_EXTENSIONS

ALL_STAT_EXTENSIONS displays information about the optimizer statistics extensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the extension |
| TABLE_NAME | VARCHAR2(128) | Name of the table to which the extension belongs |
| EXTENSION_NAME | VARCHAR2(128) | Name of the statistics extension |
| EXTENSION | CLOB | Extension (the expression or column group) |
| CREATOR | VARCHAR2(6) | Creator of the extension: USER SYSTEM |
| DROPPABLE | VARCHAR2(3) | Indicates whether the extension is droppable using DBMS_STATS.DROP_EXTENDED_STATS ( YES ) or not ( NO ) |

## Usage Notes

Related Views DBA_STAT_EXTENSIONS displays information about all optimizer statistics extensions in the database. USER_STAT_EXTENSIONS displays information about the optimizer statistics extensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_STAT_EXTENSIONS " " USER_STAT_EXTENSIONS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS.DROP_EXTENDED_STATS procedure See Also: " DBA_STAT_EXTENSIONS " " USER_STAT_EXTENSIONS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS.DROP_EXTENDED_STATS procedure