---
id: 19c__DBMS_PERF.REPORT_SQL
name: DBMS_PERF.REPORT_SQL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PERF
tags: [dbms_perf]
source_file: DBMS_PERF.html
---

# DBMS_PERF.REPORT_SQL

This function generates an active performance report for a particular SQL statement identified by its sql_id .

## Syntax

```sql
DBMS_PERF.REPORT_SQL (
    sql_id               IN varchar2 default null,
    is_realtime          IN number   default null,
    outer_start_time     IN date     default null,
    outer_end_time       IN date     default null,
    selected_start_time  IN date     default null,
    selected_end_time    IN date     default null,
    inst_id              IN number   default null,
    dbid                 IN number   default null,
    monitor_list_detail  IN number   default null,
    report_reference     IN varchar2 default null,
    report_level         IN varchar2 default null,    type                 IN varchar2 default 'ACTIVE',
    base_path            IN varchar2 default null);
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | varchar2 | IN | SQL_ID for which to retrieve performance. If NULL , gets SQL details for the last executed SQL statement. |
| is_realtime | number | IN | If 1, then real-time. If NULL (default) or 0 , then historical mode. |
| outer_start_time | date | IN | Start time of outer period shown in the time selector. If NULL (default): If is_realtime = 0 (historical), then 24 hours before outer_end_time . If is_realtime = 1 (realtime mode), then 1 hour before outer_end_time . |
| outer_end_time | date | IN | End time of outer period shown in the time selector. If NULL (default), then latest AWR snapshot. If is_realtime = 0 (historical), then the latest AWR snapshot If is_realtime = 1 (realtime mode), this is the current time (and any input is ignored) |
| selected_start_time | date | IN | Start time period of selection. If NULL (default) If is_realtime = 0 , then 1 hour before selected_end_time If is_realtime = 1 , then 5 minutes before selected_end_time |
| selected_end_time | date | IN | End time period of selection. If NULL (default) If is_realtime = 0 , then latest AWR snapshot If is_realtime = 1 , then current time |
| inst_id | number | IN | Instance ID to for which to retrieve data. If NULL (default), then instance of current session. |
| dbid | number | IN | DBID to query. If NULL , then current DBID . If is_realtime = 1 , then DBID must be the local DBID .\ |
| monitor_list_detail | number | IN | Top N in SQL monitor list for which to retrieve SQL monitor details. If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details |
| report_reference | varchar2 | IN | Must be NULL when used from SQL*Plus. |
| report_level | varchar2 | IN | 'typical' will get all tabs in performance hub |
| type | varchar2 | IN | Report type: 'ACTIVE' (default) 'xml' returns XML |
| base_path | varchar2 | IN | URL path for HTML resources since flex HTML requires access to external files |

**Returns:** `CLOB`

## Usage Notes

The SQL-level performance report contains the following tabs: Summary - This tab contains an overview of the SQL statement with key attributes like the SQL text, user name, sessions executing it, and related information. It also contains a Plans tab which shows statistics and activity for each distinct plan for this SQL statement found in memory and in the AWR. Activity - This tab shows activity broken down by wait classes for this SQL statement. The data used for this chart is fetched from Active Session History (ASH). Execution Statistics - This tab shows statistics and activity for each distinct plan for this statement along with a graphical and tabular representation of the plan. Monitored SQL - All executions of this SQL statement that were monitored by Real-time SQL Monitoring are listed in this tab. Plan Control - This tab shows information about SQL Profiles and SQL Plan Baselines if they exist for this SQL statement. Historical Statistics - This tab is available only in Historical mode. It contains statistics, such as number of executions, number of I/Os, rows processed, and other information produced over time for different execution plans. This information is retrieved from AWR. Syntax DBMS_PERF.REPORT_SQL ( sql_id IN varchar2 default null, is_realtime IN number default null, outer_start_time IN date default null, outer_end_time IN date default null, selected_start_time IN date default null, selected_end_time IN date default null, inst_id IN number default null, dbid IN number default null, monitor_list_detail IN number default null, report_reference IN varchar2 default null, report_level IN varchar2 default null, type IN varchar2 default 'ACTIVE', base_path IN varchar2 default null); RETURN CLOB; Parameters Table 126-4 REPORT_SQL Function Parameters Parameter Description sql_id SQL_ID for which to retrieve performance. If NULL , gets SQL details for the last executed SQL statement. is_realtime If 1, then real-time. If NULL (default) or 0 , then historical mode. outer_start_time Start time of outer period shown in the time selector. If NULL (default): If is_realtime = 0 (historical), then 24 hours before outer_end_time . If is_realtime = 1 (realtime mode), then 1 hour before outer_end_time . outer_end_time End time of outer period shown in the time selector. If NULL (default), then latest AWR snapshot. If is_realtime = 0 (historical), then the latest AWR snapshot If is_realtime = 1 (realtime mode), this is the current time (and any input is ignored) selected_start_time Start time period of selection. If NULL (default) If is_realtime = 0 , then 1 hour before selected_end_time If is_realtime = 1 , then 5 minutes before selected_end_time selected_end_time End time period of selection. If NULL (default) If is_realtime = 0 , then latest AWR snapshot If is_realtime = 1 , then current time inst_id Instance ID to for which to retrieve data. If NULL (default), then instance of current session. dbid DBID to query. If NULL , then current DBID . If is_realtime = 1 , then DBID must be the local DBID .\ monitor_list_detail Top N in SQL monitor list for which to retrieve SQL monitor details. If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details report_reference Must be NULL when used from SQL*Plus. report_level 'typical' will get all tabs in performance hub type Report type: 'ACTIVE' (default) 'xml' returns XML base_path URL path for HTML resources since flex HTML requires access to external files