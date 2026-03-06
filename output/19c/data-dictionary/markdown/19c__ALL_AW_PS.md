---
id: 19c__ALL_AW_PS
name: ALL_AW_PS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_AW_PS.html
---

# ALL_AW_PS

ALL_AW_PS describes the page spaces in the analytic workspaces accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic workspace |
| AW_NUMBER | NUMBER | Number of the analytic workspace |
| AW_NAME | VARCHAR2(128) | Name of the analytic workspace |
| PSNUMBER | NUMBER(10) | Number of the page space |
| GENERATIONS | NUMBER | Number of active generations in the page space |
| MAXPAGES | NUMBER | Maximum pages allocated in the page space |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_AW_PS describes the page spaces in all analytic workspaces in the database. USER_AW_PS describes the page spaces in the analytic workspaces owned by the current user. This view does not display the OWNER column. See Also: " DBA_AW_PS " " USER_AW_PS " Oracle OLAP User’s Guide for more information about the OLAP option for Oracle Database See Also: " DBA_AW_PS " " USER_AW_PS " Oracle OLAP User’s Guide for more information about the OLAP option for Oracle Database