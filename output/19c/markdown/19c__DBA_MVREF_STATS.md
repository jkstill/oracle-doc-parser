---
id: 19c__DBA_MVREF_STATS
name: DBA_MVREF_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_MVREF_STATS.html
---

# DBA_MVREF_STATS

DBA_MVREF_STATS shows the REFRESH_ID associated with each refresh run of each materialized view for the database. It also provides some basic timing statistics related to that materialized view’s refresh in that run.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MV_OWNER | VARCHAR2(128) | Owner of the materialized view |
| MV_NAME | VARCHAR2(128) | Name of the materialized view |
| REFRESH_ID | NUMBER | The refresh ID of the refresh run |
| REFRESH_METHOD | VARCHAR2(30) | The refresh method used to refresh the materialized view: FAST PCT COMPLETE OUT OF PLACE FAST OUT OF PLACE PCT OUT OF PLACE COMPLETE |
| REFRESH_OPTIMIZATIONS | VARCHAR2(4000) | The refresh optimization, for example, a null refresh, or a primary key/foreign key that is applied during refresh of the materialize view |
| ADDITIONAL_EXECUTIONS | VARCHAR2(4000) | The additional executions, for example, an index rebuild, or log operations involved during refresh of the materialized view |
| START_TIME | TIMESTAMP(6) | Start time of the refresh run |
| END_TIME | TIMESTAMP(6) | End time of the refresh run |
| ELAPSED_TIME | NUMBER | The length of time for the refresh run, in seconds |
| LOG_SETUP_TIME | NUMBER | Log setup time (in seconds) for the materialized view for a non-atomic refresh; NULL for an atomic refresh |
| LOG_PURGE_TIME | NUMBER | Log purge time (in seconds) for the materialized view in the case of atomic refresh; NULL in the case of non-atomic refresh |
| INITIAL_NUM_ROWS | NUMBER | Initial number of rows in the materialized view (at the start of the refresh) |
| FINAL_NUM_ROWS | NUMBER | Final number of rows in the materialized view (at the end of the refresh) |

## Usage Notes

Related View USER_MVREF_STATS shows the REFRESH_ID associated with each refresh run of each materialized view for the database that is accessible to the current user. It also provides some basic timing statistics related to that materialized view’s refresh in that run. This view does not display the MV_OWNER column. See Also: " USER_MVREF_STATS " See Also: " USER_MVREF_STATS "