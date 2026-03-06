---
id: 19c__V$AW_OLAP
name: V$AW_OLAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AW_OLAP.html
---

# V$AW_OLAP

V$AW_OLAP provides a record of active sessions and their use with analytic workspaces.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| AW_NUMBER | NUMBER |  |
| ATTACH_MODE | VARCHAR2(10) |  |
| GENERATION | NUMBER |  |
| TEMP_SPACE_PAGES | NUMBER |  |
| TEMP_SPACE_READS | NUMBER |  |
| LOB_READS | NUMBER |  |
| POOL_CHANGED_PAGES | NUMBER |  |
| POOL_UNCHANGED_PAGES | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

A row is generated whenever an analytic workspace is created or attached. The first row for a session is created when the first command is issued. It identifies the SYS.EXPRESS workspace, which is attached automatically to each session. Rows related to a particular analytic workspace are deleted when the workspace is detached from the session or the session ends.