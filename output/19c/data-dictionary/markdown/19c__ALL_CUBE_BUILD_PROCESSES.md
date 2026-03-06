---
id: 19c__ALL_CUBE_BUILD_PROCESSES
name: ALL_CUBE_BUILD_PROCESSES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_BUILD_PROCESSES.html
---

# ALL_CUBE_BUILD_PROCESSES

ALL_CUBE_BUILD_PROCESSES describes the OLAP build processes and maintenance scripts accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the build process |
| BUILD_PROCESS_NAME | VARCHAR2(128) | Name of the build process |
| BUILD_PROCESS_ID | NUMBER | ID of the build process |
| BUILD_PROCESS | CLOB | Syntax of the build process |
| DESCRIPTION | NVARCHAR2(300) | Description of the build process in the session language |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CUBE_BUILD_PROCESSES describes all OLAP build processes and maintenance scripts in the database. USER_CUBE_BUILD_PROCESSES describes the OLAP build processes and maintenance scripts owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_BUILD_PROCESSES " " USER_CUBE_BUILD_PROCESSES " See Also: " DBA_CUBE_BUILD_PROCESSES " " USER_CUBE_BUILD_PROCESSES "