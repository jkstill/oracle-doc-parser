---
id: 19c__DBMS_PERF.REPORT_PERFHUB
name: DBMS_PERF.REPORT_PERFHUB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PERF
tags: [dbms_perf]
source_file: DBMS_PERF.html
---

# DBMS_PERF.REPORT_PERFHUB

This function generates a composite active performance report of the entire database system for a specified time period.

## Syntax

```sql
DBMS_PERF.REPORT_PERFHUB (
   is_realtime          IN NUMBER   DEFAULT NULL,
   outer_start_time     IN DATE     DEFAULT NULL,
   outer_end_time       IN DATE     DEFAULT NULL,
   selected_start_time  IN DATE     DEFAULT NULL,
   selected_end_time    IN DATE     DEFAULT NULL,
   inst_id              IN NUMBER   DEFAULT NULL,
   dbid                 IN NUMBER   DEFAULT NULL,
   monitor_list_detail  IN NUMBER   DEFAULT NULL,
   workload_sql_detail  IN NUMBER   DEFAULT NULL,
   addm_task_detail     IN NUMBER   DEFAULT NULL,
   report_reference     IN VARCHAR2 DEFAULT NULL,
   report_level         IN VARCHAR2 DEFAULT NULL,
   type                 IN VARCHAR2 DEFAULT 'ACTIVE',
   base_path            IN VARCHAR2 DEFAULT NULL);
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| is_realtime | NUMBER | IN | If 1, then real-time. If NULL (default) or 0 , then historical mode. |
| outer_start_time | DATE | IN | Start time of outer period shown in the time selector. If NULL (default): If is_realtime = 0 (historical), then 24 hours before outer_end_time . If is_realtime = 1 (realtime mode), then 1 hour before outer_end_time . |
| outer_end_time | DATE | IN | End time of outer period shown in the time selector. If NULL (default), then latest AWR snapshot. If is_realtime = 0 (historical), then the latest AWR snapshot If is_realtime = 1 (realtime mode), this is the current time (and any input is ignored) |
| selected_start_time | DATE | IN | Start time period of selection. If NULL (default) If is_realtime = 0 , then 1 hour before selected_end_time If is_realtime = 1 , then 5 minutes before selected_end_time |
| selected_end_time | DATE | IN | End time period of selection. If NULL (default) If is_realtime = 0 , then latest AWR snapshot If is_realtime = 1 , then current time |
| inst_id | NUMBER | IN | Instance ID to for which to retrieve data If -1 , then current instance If number is specified, then for that instance If NULL (default), then all instances |
| dbid | NUMBER | IN | DBID to query. If NULL , then current DBID . If is_realtime = 1 , then DBID must be the local DBID . |
| monitor_list_detail | NUMBER | IN | Top N in SQL monitor list for which to retrieve SQL monitor details. If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details |
| workload_sql_detail | NUMBER | IN | Top N in Workload Top SQL list to retrieve monitor details, If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details |
| addm_task_detail | NUMBER | IN | Maximum N latest ADDM tasks to retrieve If NULL (default), retrieves available data but no more than N If 0 , then retrieves no ADDM task details |
| report_reference | VARCHAR2 | IN | Must be NULL when used from SQL*Plus. |
| report_level | VARCHAR2 | IN | 'typical' will get all tabs in performance hub |
| type | VARCHAR2 | IN | Report type: 'ACTIVE' (default) 'xml' returns XML |
| base_path | VARCHAR2 | IN | URL path for HTML resources since flex HTML requires access to external files. This is only valid for type=' ACTIVE' and is typically not used. Default value will retrieve the required files from OTN. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_PERF.REPORT_PERFHUB ( is_realtime IN NUMBER DEFAULT NULL, outer_start_time IN DATE DEFAULT NULL, outer_end_time IN DATE DEFAULT NULL, selected_start_time IN DATE DEFAULT NULL, selected_end_time IN DATE DEFAULT NULL, inst_id IN NUMBER DEFAULT NULL, dbid IN NUMBER DEFAULT NULL, monitor_list_detail IN NUMBER DEFAULT NULL, workload_sql_detail IN NUMBER DEFAULT NULL, addm_task_detail IN NUMBER DEFAULT NULL, report_reference IN VARCHAR2 DEFAULT NULL, report_level IN VARCHAR2 DEFAULT NULL, type IN VARCHAR2 DEFAULT 'ACTIVE', base_path IN VARCHAR2 DEFAULT NULL); RETURN CLOB; Parameters Table 126-2 REPORT_PERFHUB Function Parameters Parameter Description is_realtime If 1, then real-time. If NULL (default) or 0 , then historical mode. outer_start_time Start time of outer period shown in the time selector. If NULL (default): If is_realtime = 0 (historical), then 24 hours before outer_end_time . If is_realtime = 1 (realtime mode), then 1 hour before outer_end_time . outer_end_time End time of outer period shown in the time selector. If NULL (default), then latest AWR snapshot. If is_realtime = 0 (historical), then the latest AWR snapshot If is_realtime = 1 (realtime mode), this is the current time (and any input is ignored) selected_start_time Start time period of selection. If NULL (default) If is_realtime = 0 , then 1 hour before selected_end_time If is_realtime = 1 , then 5 minutes before selected_end_time selected_end_time End time period of selection. If NULL (default) If is_realtime = 0 , then latest AWR snapshot If is_realtime = 1 , then current time inst_id Instance ID to for which to retrieve data If -1 , then current instance If number is specified, then for that instance If NULL (default), then all instances dbid DBID to query. If NULL , then current DBID . If is_realtime = 1 , then DBID must be the local DBID . monitor_list_detail Top N in SQL monitor list for which to retrieve SQL monitor details. If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details workload_sql_detail Top N in Workload Top SQL list to retrieve monitor details, If NULL (default), then retrieves top 10 If 0 , then retrieves no monitor list details addm_task_detail Maximum N latest ADDM tasks to retrieve If NULL (default), retrieves available data but no more than N If 0 , then retrieves no ADDM task details report_reference Must be NULL when used from SQL*Plus. report_level 'typical' will get all tabs in performance hub type Report type: 'ACTIVE' (default) 'xml' returns XML base_path URL path for HTML resources since flex HTML requires access to external files. This is only valid for type=' ACTIVE' and is typically not used. Default value will retrieve the required files from OTN. Usage Notes Once a time period is selected, the performance information is collected and presented based on performance subject areas. The time period can be real-time or historical. When real-time data is selected, more granular data is presented because data points are available every minute. When historical data is selected, more detailed data (broken down by different metrics) is presented, but the data points are averaged out to the Automatic Workload Repository (AWR) interval (usually an hour). Different tabs are available in the Performance Hub, depending on whether is_real-time is 1 for real time mode or 0 for historical mode.