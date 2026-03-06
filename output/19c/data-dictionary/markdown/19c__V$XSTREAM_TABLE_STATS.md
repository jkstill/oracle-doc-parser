---
id: 19c__V$XSTREAM_TABLE_STATS
name: V$XSTREAM_TABLE_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dynamic_performance]
source_file: V-XSTREAM_TABLE_STATS.html
---

# V$XSTREAM_TABLE_STATS

V$XSTREAM_TABLE_STATS shows the statistics for all the tables processed by each apply server for the XStream session.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLY_NAME | VARCHAR2(128) |  |
| SERVER_ID | NUMBER |  |
| SOURCE_TABLE_OWNER | VARCHAR2(128) |  |
| SOURCE_TABLE_NAME | VARCHAR2(128) |  |
| DESTINATION_TABLE_OWNER | VARCHAR2(128) |  |
| DESTINATION_TABLE_NAME | VARCHAR2(128) |  |
| LAST_UPDATE | DATE |  |
| TOTAL_INSERTS | NUMBER |  |
| TOTAL_UPDATES | NUMBER |  |
| TOTAL_DELETES | NUMBER |  |
| INSERT_COLLISIONS | NUMBER |  |
| UPDATE_COLLISIONS | NUMBER |  |
| DELETE_COLLISIONS | NUMBER |  |
| REPERROR_RECORDS | NUMBER |  |
| REPERROR_IGNORES | NUMBER |  |
| WAIT_DEPENDENCIES | NUMBER |  |
| CON_ID | NUMBER |  |
| CDR_INSERT_ROW_EXISTS | NUMBER |  |
| CDR_UPDATE_ROW_EXISTS | NUMBER |  |
| CDR_UPDATE_ROW_MISSING | NUMBER |  |
| CDR_DELETE_ROW_EXISTS | NUMBER |  |
| CDR_DELETE_ROW_MISSING | NUMBER |  |
| CDR_SUCCESSFUL_RESOLUTIONS | NUMBER |  |
| CDR_FAILED_RESOLUTIONS | NUMBER |  |
| LOB_OPERATIONS | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database XStream Guide for more information about XStream conflict detection and resolution See Also: Oracle Database XStream Guide for more information about XStream conflict detection and resolution