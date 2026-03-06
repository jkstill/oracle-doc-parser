---
id: 19c__DBMS_PERF.REPORT_SESSION
name: DBMS_PERF.REPORT_SESSION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PERF
tags: [dbms_perf]
source_file: DBMS_PERF.html
---

# DBMS_PERF.REPORT_SESSION

This function produces a performance report for a specific database session where a session is identified by inst_id , sid , and serial_num .

## Syntax

```sql
DBMS_PERF.REPORT_SESSION (
    inst_id              IN NUMBER   DEFAULT NULL,
    sid                  IN NUMBER   DEFAULT NULL,
    serial               IN NUMBER   DEFAULT NULL,
    is_realtime          IN NUMBER   DEFAULT NULL,
    outer_start_time     IN DATE     DEFAULT NULL,
    outer_end_time       IN DATE     DEFAULT NULL,
    selected_start_time  IN DATE     DEFAULT NULL,
    selected_end_time    IN DATE     DEFAULT NULL,
    dbid                 IN NUMBER   DEFAULT NULL,
    monitor_list_detail  IN NUMBER   DEFAULT NULL,
    report_reference     IN VARCHAR2 DEFAULT NULL,
    report_level         IN VARCHAR2 DEFAULT NULL,
    type                 IN VARCHAR2 DEFAULT 'ACTIVE',
    base_path            IN VARCHAR2 DEFAULT NULL)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| inst_id | NUMBER | IN | Instance ID to for which to retrieve data. If NULL (default), then instance of current session. |
| sid | NUMBER | IN | Session ID for which to retrieve performance. If NULL , uses current session. |
| serial | NUMBER | IN | Serial# of session. If NULL , then the serial# of the specified sid is used provided the session is connected. |
| is_realtime | NUMBER | IN | If 1, then real-time. If NULL (default) or 0 , then historical mode. |
| outer_start_time | DATE | IN | Start time of outer period shown in the time selector. If NULL (default): If is_realtime = 0 (historical), then 24 hours before outer_end_time . If is_realtime = 1 (realtime mode), then 1 hour before outer_end_time . |
| outer_end_time | DATE | IN | End time of outer period shown in the time selector. If NULL (default), then latest AWR snapshot. If is_realtime = 0 (historical), then the latest AWR snapshot If is_realtime = 1 (realtime mode), this is the current time (and any input is ignored) |
| selected_start_time | DATE | IN | Start time period of selection. If NULL (default) If is_realtime = 0 , then 1 hour before selected_end_time If is_realtime = 1 , then 5 minutes before selected_end_time |
| selected_end_time | DATE | IN | End time period of selection. If NULL (default) If is_realtime = 0 , then latest AWR snapshot If is_realtime = 1 , then current time |
| dbid | NUMBER | IN | DBID to query. If NULL , then current DBID . If is_realtime = 1 , then DBID must be the local DBID .\ |
| monitor_list_detail | NUMBER | IN | Top N in SQL monitor list for which to retrieve SQL monitor details. If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details |
| report_reference | VARCHAR2 | IN | Must be NULL when used from SQL*Plus. |
| report_level | VARCHAR2 | IN | 'typical' will get all tabs in the session hub (or session details) |
| type | VARCHAR2 | IN | Report type: 'ACTIVE' (default) 'xml' returns XML |
| base_path | VARCHAR2 | IN | URL path for HTML resources since flex HTML requires access to external files |

**Returns:** `CLOB`

## Usage Notes

If any of those parameters are missing, then the report is for the current session. The session-level performance report contains the following tabs: Summary - This tab contains key identifiers and attributes of the session along with a summary of its activity data. It also contains a list of SQLs, PLSQL blocks and Database Operations (DBOP) executed by that session that were monitored by Real-time SQL Monitoring. Activity - This tab shows activity broken down by wait classes for this session. The data used for this chart is fetched from Active Session History (ASH). Metrics - This tab shows charts for certain key metrics for the selected session over time and is only available in historical mode. Some of the metrics shown are CPU usage, PGA usage, IO Throughput and IO Requests. Syntax DBMS_PERF.REPORT_SESSION ( inst_id IN NUMBER DEFAULT NULL, sid IN NUMBER DEFAULT NULL, serial IN NUMBER DEFAULT NULL, is_realtime IN NUMBER DEFAULT NULL, outer_start_time IN DATE DEFAULT NULL, outer_end_time IN DATE DEFAULT NULL, selected_start_time IN DATE DEFAULT NULL, selected_end_time IN DATE DEFAULT NULL, dbid IN NUMBER DEFAULT NULL, monitor_list_detail IN NUMBER DEFAULT NULL, report_reference IN VARCHAR2 DEFAULT NULL, report_level IN VARCHAR2 DEFAULT NULL, type IN VARCHAR2 DEFAULT 'ACTIVE', base_path IN VARCHAR2 DEFAULT NULL) RETURN CLOB; Parameters Table 126-3 REPORT_SESSION Function Parameters Parameter Description inst_id Instance ID to for which to retrieve data. If NULL (default), then instance of current session. sid Session ID for which to retrieve performance. If NULL , uses current session. serial Serial# of session. If NULL , then the serial# of the specified sid is used provided the session is connected. is_realtime If 1, then real-time. If NULL (default) or 0 , then historical mode. outer_start_time Start time of outer period shown in the time selector. If NULL (default): If is_realtime = 0 (historical), then 24 hours before outer_end_time . If is_realtime = 1 (realtime mode), then 1 hour before outer_end_time . outer_end_time End time of outer period shown in the time selector. If NULL (default), then latest AWR snapshot. If is_realtime = 0 (historical), then the latest AWR snapshot If is_realtime = 1 (realtime mode), this is the current time (and any input is ignored) selected_start_time Start time period of selection. If NULL (default) If is_realtime = 0 , then 1 hour before selected_end_time If is_realtime = 1 , then 5 minutes before selected_end_time selected_end_time End time period of selection. If NULL (default) If is_realtime = 0 , then latest AWR snapshot If is_realtime = 1 , then current time dbid DBID to query. If NULL , then current DBID . If is_realtime = 1 , then DBID must be the local DBID .\ monitor_list_detail Top N in SQL monitor list for which to retrieve SQL monitor details. If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details report_reference Must be NULL when used from SQL*Plus. report_level 'typical' will get all tabs in the session hub (or session details) type Report type: 'ACTIVE' (default) 'xml' returns XML base_path URL path for HTML resources since flex HTML requires access to external files