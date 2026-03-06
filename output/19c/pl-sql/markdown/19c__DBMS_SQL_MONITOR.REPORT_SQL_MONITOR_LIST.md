---
id: 19c__DBMS_SQL_MONITOR.REPORT_SQL_MONITOR_LIST
name: DBMS_SQL_MONITOR.REPORT_SQL_MONITOR_LIST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_MONITOR
tags: [dbms_sql_monitor]
source_file: DBMS_SQL_MONITOR.html
---

# DBMS_SQL_MONITOR.REPORT_SQL_MONITOR_LIST

This function builds a report for all or a subset of database operations that have been monitored by Oracle Database.

## Syntax

```sql
DBMS_SQL_MONITOR.REPORT_SQL_MONITOR_LIST (
   sql_id                    IN VARCHAR2 DEFAULT  NULL,
   dbop_name                 IN VARCHAR2 DEFAULT  NULL,
   monitor_type              IN NUMBER   DEFAULT  MONITOR_TYPE_ALL, 
   session_id                IN NUMBER   DEFAULT  NULL,
   session_serial            IN NUMBER   DEFAULT  NULL,
   inst_id                   IN NUMBER   DEFAULT  NULL,
   active_since_date         IN DATE     DEFAULT  NULL,
   active_since_sec          IN NUMBER   DEFAULT  NULL,
   last_refresh_time         IN DATE     DEFAULT  NULL,
   report_level              IN VARCHAR2 DEFAULT 'TYPICAL',
   auto_refresh              IN NUMBER   DEFAULT  NULL, 
   base_path                 IN VARCHAR2 DEFAULT  NULL,
   type                      IN VARCHAR2 DEFAULT 'TEXT',
   con_name                  IN VARCHAR2 DEFAULT  NULL)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2 | IN | SQL_ID of the simple database operation for which monitoring information should be displayed. Use NULL (default) to display monitoring information for the last operation monitored by Oracle Database. |
| dbop_name | VARCHAR2 | IN | DBOP_NAME for which monitoring information of the composite database operation is displayed. |
| monitor_type | NUMBER | IN | Monitor type: MONITOR_TYPE_SQL returns only simple database operations MONITOR_TYPE_DBOP returns composite database operations MONITOR_TYPE_ALL returns all types |
| session_id | NUMBER | IN | Targets only the subset of database operations executed and monitored on behalf of the specified session. Default is NULL . Use -1 or USERENV('SID') for the current session. |
| session_serial | NUMBER | IN | In addition to session_id , you can specify the session serial number to ensure the desired session incarnation is targeted. This is ignored when session_id is NULL . |
| inst_id | NUMBER | IN | Looks only at monitored database operations originating from the specified instance. Use -1 to target the instance where the report executed. To target all instances, use NULL (default). |
| active_since_date | DATE | IN | If not NULL (default), returns monitored database operations that have been active since the specified time. This includes all operations that are executing, as well as all operations that have completed their execution after the specified start time. |
| active_since_sec | NUMBER | IN | If not NULL (default), returns monitored database operations that have been active since the specified time. This includes all operations that are executing, as well as all operations that have completed their execution after the specified date and time. In this case, the start time is specified relative to the current SYSDATE minus a specified number of seconds. For example, use 3600 to limit the report to all operations that have been active in the past 1 hour. |
| last_refresh_time | DATE | IN | If not NULL (default), the time when the list report was last retrieved. This optimizes the case where an application shows the list and refreshes the report on a regular basis (such as once every 5 seconds). In this case, the report will show details about the execution of monitored queries that have been active since the specified last_refresh_time . For other queries, the report returns the execution key ( sql_id , sql_exec_start , and sql_exec_id ). Also, for queries that have their first refresh time after the specified date, only the SQL execution key and statistics are returned. |
| report_level | VARCHAR2 | IN | Level of detail for the report. The level can be BASIC (SQL text up to 200 character), TYPICAL (which include full SQL text assuming that cursor has not aged out, in which case the SQL text is included up to 2000 characters), or ALL which is the same as TYPICAL . |
| auto_refresh | NUMBER | IN | Specifies the duration in seconds after which report data will be automatically refreshed while the monitored SQL or database operation is still executing. This applies to active report types. |
| base_path | VARCHAR2 | IN | URL path for flex HTML resources since flex HTML format requires access to external files (java scripts and the flash swf file). |
| type | VARCHAR2 | IN | Report type: TEXT : text report (default) HTML : simple HTML report ACTIVE : database active report. Some information (explain plan, activity_histogram , metrics, and plan_histogram ) is only shown when this type is selected. XML : raw data for the report |
| con_name | VARCHAR2 | IN | Container name in a multitenant database. |

**Returns:** `CLOB`

## Usage Notes

For each database operation, it gives key information and associated global statistics. Syntax DBMS_SQL_MONITOR.REPORT_SQL_MONITOR_LIST ( sql_id IN VARCHAR2 DEFAULT NULL, dbop_name IN VARCHAR2 DEFAULT NULL, monitor_type IN NUMBER DEFAULT MONITOR_TYPE_ALL, session_id IN NUMBER DEFAULT NULL, session_serial IN NUMBER DEFAULT NULL, inst_id IN NUMBER DEFAULT NULL, active_since_date IN DATE DEFAULT NULL, active_since_sec IN NUMBER DEFAULT NULL, last_refresh_time IN DATE DEFAULT NULL, report_level IN VARCHAR2 DEFAULT 'TYPICAL', auto_refresh IN NUMBER DEFAULT NULL, base_path IN VARCHAR2 DEFAULT NULL, type IN VARCHAR2 DEFAULT 'TEXT', con_name IN VARCHAR2 DEFAULT NULL) RETURN CLOB; Parameters Table 163-6 REPORT_SQL_MONITOR_LIST Procedure Parameters Parameter Description sql_id SQL_ID of the simple database operation for which monitoring information should be displayed. Use NULL (default) to display monitoring information for the last operation monitored by Oracle Database. dbop_name DBOP_NAME for which monitoring information of the composite database operation is displayed. monitor_type Monitor type: MONITOR_TYPE_SQL returns only simple database operations MONITOR_TYPE_DBOP returns composite database operations MONITOR_TYPE_ALL returns all types session_id Targets only the subset of database operations executed and monitored on behalf of the specified session. Default is NULL . Use -1 or USERENV('SID') for the current session. session_serial In addition to session_id , you can specify the session serial number to ensure the desired session incarnation is targeted. This is ignored when session_id is NULL . inst_id Looks only at monitored database operations originating from the specified instance. Use -1 to target the instance where the report executed. To target all instances, use NULL (default). active_since_date If not NULL (default), returns monitored database operations that have been active since the specified time. This includes all operations that are executing, as well as all operations that have completed their execution after the specified start time. active_since_sec If not NULL (default), returns monitored database operations that have been active since the specified time. This includes all operations that are executing, as well as all operations that have completed their execution after the specified date and time. In this case, the start time is specified relative to the current SYSDATE minus a specified number of seconds. For example, use 3600 to limit the report to all operations that have been active in the past 1 hour. last_refresh_time If not NULL (default), the time when the list report was last retrieved. This optimizes the case where an application shows the list and refreshes the report on a regular basis (such as once every 5 seconds). In this case, the report will show details about the execution of monitored queries that have been active since the specified last_refresh_time . For other queries, the report returns the execution key ( sql_id , sql_exec_start , and sql_exec_id ). Also, for queries that have their first refresh time after the specified date, only the SQL execution key and statistics are returned. report_level Level of detail for the report. The level can be BASIC (SQL text up to 200 character), TYPICAL (which include full SQL text assuming that cursor has not aged out, in which case the SQL text is included up to 2000 characters), or ALL which is the same as TYPICAL . auto_refresh Specifies the duration in seconds after which report data will be automatically refreshed while the monitored SQL or database operation is still executing. This applies to active report types. base_path URL path for flex HTML resources since flex HTML format requires access to external files (java scripts and the flash swf file). type Report type: TEXT : text report (default) HTML : simple HTML report ACTIVE : database active report. Some information (explain plan, activity_histogram , metrics, and plan_histogram ) is only shown when this type is selected. XML : raw data for the report con_name Container name in a multitenant database. Return Values A report in text, XML, or HTML format that contains the list of the database operations monitored. Usage Notes Use the REPORT_SQL_MONITOR Function to get detailed monitoring information for a single database operation. The user invoking this function needs to have the privilege to access the fixed views GV$SQL_MONITOR and GV$SQL .