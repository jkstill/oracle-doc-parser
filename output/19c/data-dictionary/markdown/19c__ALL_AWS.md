---
id: 19c__ALL_AWS
name: ALL_AWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_AWS.html
---

# ALL_AWS

ALL_AWS describes the analytic workspaces accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the analytic workspace |
| AW_NUMBER | NUMBER | Number of the analytic workspace |
| AW_NAME | VARCHAR2(128) | Name of the analytic workspace |
| AW_VERSION | VARCHAR2(4) | Format version of the analytic workspace: 9.1 10.1 10.2 11.1 |
| PAGESPACES | NUMBER | Number of pagespaces in the analytic workspace |
| GENERATIONS | NUMBER | Number of active generations in the analytic workspace |
| FROZEN | VARCHAR2(6) | Freeze state of the analytic workspace: Frozen NoThaw |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_AWS describes all analytic workspaces in the database. USER_AWS describes the analytic workspaces owned by the current user. This view does not display the OWNER column. See Also: " DBA_AWS " " USER_AWS " Oracle OLAP User’s Guide for more information about the OLAP option for Oracle Database See Also: " DBA_AWS " " USER_AWS " Oracle OLAP User’s Guide for more information about the OLAP option for Oracle Database