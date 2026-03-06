---
id: 19c__DBMS_SQLTUNE.REPORT_SQL_DETAIL
name: DBMS_SQLTUNE.REPORT_SQL_DETAIL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.REPORT_SQL_DETAIL

This function builds a report for a specific SQLID. For each SQLID it gives various statistics and details as obtained from the V$ views and AWR.

## Syntax

```sql
DBMS_SQLTUNE.REPORT_SQL_DETAIL (
   sql_id                   IN  VARCHAR2   DEFAULT NULL,
   sql_plan_hash_value      IN  NUMBER     DEFAULT NULL,
   start_time               IN  DATE       DEFAULT NULL,
   duration                 IN  NUMBER     DEFAULT NULL,
   inst_id                  IN  NUMBER     DEFAULT NULL,
   dbid                     IN  NUMBER     DEFAULT NULL,
   event_detail             IN  VARCHAR2   DEFAULT 'YES',
   bucket_max_count         IN  NUMBER     DEFAULT 128,
   bucket_interval          IN  NUMBER     DEFAULT NULL,
   top_n                    IN  NUMBER     DEFAULT 10,
   report_level             IN  VARCHAR2   DEFAULT 'TYPICAL',
   type                     IN  VARCHAR2   DEFAULT 'ACTIVE',
   data_source              IN  VARCHAR2   DEFAULT 'AUTO',
   end_time                 IN  DATE       DEFAULT NULL,
   duration_stats           IN  NUMBER     DEFAULT NULL,
   con_name                 IN  VARCHAR2   DEFAULT NULL)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2 | IN | SQLID for which monitoring information should be displayed. If NULL (the default), display statistics for the SQLID of the last SQL statement executed in the current session. |
| sql_plan_hash_value | NUMBER | IN | Displays SQL statistics and details for a specific plan_hash_value . If NULL (default), displays statistics and details for all plans of the SQL_ID. |
| start_time | DATE | IN | If specified, shows SQL activity (from GV$ACTIVE_SESSION_HISTORY ) starting at this time. On Oracle RAC, the minimum start_time is the earliest sample_time of the in-memory ASH buffers across all instances. If NULL (default), one hour before the current time. |
| duration | NUMBER | IN | Duration of activity in seconds for the report. If NULL (default) uses a value of 1 hour. |
| inst_id | NUMBER | IN | Target instance to get SQL details from. If NULL , uses data from all instances. If 0 or -1, uses current instance. |
| dbid | NUMBER | IN | DBID from which to get SQL details. If NULL , uses current DBID. |
| event_detail | VARCHAR2 | IN | When set to 'NO' , the activity is aggregated by wait_class only. Use 'YES' (the default) to aggregate by ( wait_class , event_name ). |
| bucket_max_count | NUMBER | IN | If specified, this should be the maximum number of histogram buckets created in the report. If not specified, a value of 128 is used. |
| bucket_interval | NUMBER | IN | If specified, this represents the exact time interval in seconds, of all histogram buckets. If specified, bucket_max_count is ignored. |
| top_n | NUMBER | IN | Controls the number of entries to display per dimension in the top dimensions section. If not specified, a default value of 10 is used. |
| report_level | VARCHAR2 | IN | Level of detail for the report, either 'BASIC' , 'TYPICAL' or 'ALL' . Default assumes 'TYPICAL' . Their meanings are explained below. In addition, individual report sections can also be enabled or disabled by using a +/- section_name . Several sections are defined: 'TOP' - Show top values for the ASH dimensions for a SQL statement; ON by default 'SPM' - Show existing plan baselines for a SQL statement; OFF by default 'MISMATCH' - Show reasons for creating new child cursors (sharing criteria violations); OFF by default. 'STATS' - Show SQL execution statistics per plan from GV$SQLAREA_PLAN_HASH ; ON by default 'ACTIVITY' - Show top activity from ASH for each plan of a SQL statement; ON by default 'ACTIVITY_ALL' - Show top activity from ASH for each line of the plan for a SQL statement; OFF by default 'HISTOGRAM' - Show activity histogram for each plan of a SQL statement (plan time line histogram); ON by default 'SESSIONS' - Show activity for top sessions for each plan of a SQL statement; OFF by default 'MONITOR' - Show show one monitored SQL execution per execution plan; ON by default 'XPLAN' - Show execution plans; ON by default 'BINDS' - show captured bind data; ON by default In addition, SQL text can be specified at different levels: - SQL_TEXT - No SQL text in report +SQL_TEXT - OK with partial SQL text up to the first 2000 chars as stored in GV$SQL_MONITOR -SQL_FULLTEXT - No full SQL text ( +SQL_TEXT ) +SQL_FULLTEXT - Show full SQL text (default value) The meanings of the three top-level report levels are: NONE - minimum possible BASIC - SQL_TEXT+STATS+ACTIVITY+HISTOGRAM TYPICAL - SQL_FULLTEXT+TOP+STATS+ACTIVITY+HISTOGRAM+XPLAN+MONITOR ALL - everything Only one of these 4 levels can be specified and, if it is, it has to be at the start of the REPORT_LEVEL string |
| type | VARCHAR2 | IN | Report format: 'ACTIVE' by default. Can also be 'XML' (see Usage Notes). |
| data_source | VARCHAR2 | IN | Determines the data source of SQL data based on one of the following values: MEMORY : The data source is GV$ view DISK : The data source is DBA_HIST_* view AUTO : Automatically determines the data source based on the time frame (default) |
| end_time | DATE | IN | If specified, shows SQL activity from start_time to end_time . If NULL (default), shows SQL activity for systimestamp . |
| duration_stats | NUMBER | IN | Duration of additional SQL execution statistics from AWR (in hours), for the report. If NULL (default), then the duration of 24 hours is considered. |
| con_name | VARCHAR2 | IN | Name of the multitenant container database (CDB). |

**Returns:** `CLOB`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Performance Reporting Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Performance Reporting Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.REPORT_SQL_DETAIL ( sql_id IN VARCHAR2 DEFAULT NULL, sql_plan_hash_value IN NUMBER DEFAULT NULL, start_time IN DATE DEFAULT NULL, duration IN NUMBER DEFAULT NULL, inst_id IN NUMBER DEFAULT NULL, dbid IN NUMBER DEFAULT NULL, event_detail IN VARCHAR2 DEFAULT 'YES', bucket_max_count IN NUMBER DEFAULT 128, bucket_interval IN NUMBER DEFAULT NULL, top_n IN NUMBER DEFAULT 10, report_level IN VARCHAR2 DEFAULT 'TYPICAL', type IN VARCHAR2 DEFAULT 'ACTIVE', data_source IN VARCHAR2 DEFAULT 'AUTO', end_time IN DATE DEFAULT NULL, duration_stats IN NUMBER DEFAULT NULL, con_name IN VARCHAR2 DEFAULT NULL) RETURN CLOB; Parameters Table 169-32 REPORT_SQL_DETAIL Function Parameters Parameter Description sql_id SQLID for which monitoring information should be displayed. If NULL (the default), display statistics for the SQLID of the last SQL statement executed in the current session. sql_plan_hash_value Displays SQL statistics and details for a specific plan_hash_value . If NULL (default), displays statistics and details for all plans of the SQL_ID. start_time If specified, shows SQL activity (from GV$ACTIVE_SESSION_HISTORY ) starting at this time. On Oracle RAC, the minimum start_time is the earliest sample_time of the in-memory ASH buffers across all instances. If NULL (default), one hour before the current time. duration Duration of activity in seconds for the report. If NULL (default) uses a value of 1 hour. inst_id Target instance to get SQL details from. If NULL , uses data from all instances. If 0 or -1, uses current instance. dbid DBID from which to get SQL details. If NULL , uses current DBID. event_detail When set to 'NO' , the activity is aggregated by wait_class only. Use 'YES' (the default) to aggregate by ( wait_class , event_name ). bucket_max_count If specified, this should be the maximum number of histogram buckets created in the report. If not specified, a value of 128 is used. bucket_interval If specified, this represents the exact time interval in seconds, of all histogram buckets. If specified, bucket_max_count is ignored. top_n Controls the number of entries to display per dimension in the top dimensions section. If not specified, a default value of 10 is used. report_level Level of detail for the report, either 'BASIC' , 'TYPICAL' or 'ALL' . Default assumes 'TYPICAL' . Their meanings are explained below. In addition, individual report sections can also be enabled or disabled by using a +/- section_name . Several sections are defined: 'TOP' - Show top values for the ASH dimensions for a SQL statement; ON by default 'SPM' - Show existing plan baselines for a SQL statement; OFF by default 'MISMATCH' - Show reasons for creating new child cursors (sharing criteria violations); OFF by default. 'STATS' - Show SQL execution statistics per plan from GV$SQLAREA_PLAN_HASH ; ON by default 'ACTIVITY' - Show top activity from ASH for each plan of a SQL statement; ON by default 'ACTIVITY_ALL' - Show top activity from ASH for each line of the plan for a SQL statement; OFF by default 'HISTOGRAM' - Show activity histogram for each plan of a SQL statement (plan time line histogram); ON by default 'SESSIONS' - Show activity for top sessions for each plan of a SQL statement; OFF by default 'MONITOR' - Show show one monitored SQL execution per execution plan; ON by default 'XPLAN' - Show execution plans; ON by default 'BINDS' - show captured bind data; ON by default In addition, SQL text can be specified at different levels: - SQL_TEXT - No SQL text in report +SQL_TEXT - OK with partial SQL text up to the first 2000 chars as stored in GV$SQL_MONITOR -SQL_FULLTEXT - No full SQL text ( +SQL_TEXT ) +SQL_FULLTEXT - Show full SQL text (default value) The meanings of the three top-level report levels are: NONE - minimum possible BASIC - SQL_TEXT+STATS+ACTIVITY+HISTOGRAM TYPICAL - SQL_FULLTEXT+TOP+STATS+ACTIVITY+HISTOGRAM+XPLAN+MONITOR ALL - everything Only one of these 4 levels can be specified and, if it is, it has to be at the start of the REPORT_LEVEL string type Report format: 'ACTIVE' by default. Can also be 'XML' (see Usage Notes). data_source Determines the data source of SQL data based on one of the following values: MEMORY : The data source is GV$ view DISK : The data source is DBA_HIST_* view AUTO : Automatically determines the data source based on the time frame (default) end_time If specified, shows SQL activity from start_time to end_time . If NULL (default), shows SQL activity for systimestamp . duration_stats Duration of additional SQL execution statistics from AWR (in hours), for the report. If NULL (default), then the duration of 24 hours is considered. con_name Name of the multitenant container database (CDB). Security Model The invoker needs the EXECUTE privilege on the DBMS_XPLAN package.