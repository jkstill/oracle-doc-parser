---
id: 19c__DBMS_SQLTUNE.REPORT_SQL_MONITOR_LIST
name: DBMS_SQLTUNE.REPORT_SQL_MONITOR_LIST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.REPORT_SQL_MONITOR_LIST

This function builds a report for all or a subset of statements monitored by Oracle Database. For each statement, the subprogram gives key information and associated global statistics.

## Syntax

```sql
DBMS_SQLTUNE.REPORT_SQL_MONITOR_LIST(
   sql_id                    IN VARCHAR2  DEFAULT  NULL,
   session_id                IN NUMBER    DEFAULT  NULL,
   session_serial            IN NUMBER    DEFAULT  NULL,
   inst_id                   IN NUMBER    DEFAULT  NULL,
   active_since_date         IN DATE      DEFAULT  NULL,
   active_since_sec          IN NUMBER    DEFAULT  NULL,
   active_before_date        IN DATE      DEFAULT  NULL,
   last_refresh_time         IN DATE      DEFAULT  NULL,
   dbop_name                 IN VARCHAR2  DEFAULT  NULL,
   monitor_type              IN NUMBER    DEFAULT  MONITOR_TYPE_ALL,
   max_sqltext_length        IN NUMBER    DEFAULT  NULL,
   top_n_count               IN NUMBER    DEFAULT  NULL,
   top_n_rankby              IN VARCHAR2  DEFAULT  'LAST_ACTIVE_TIME',
   report_level              IN VARCHAR2  DEFAULT  'TYPICAL',
   auto_refresh              IN NUMBER    DEFAULT  NULL,
   base_path                 IN VARCHAR2  DEFAULT  NULL,
   type                      IN VARCHAR2  DEFAULT 'TEXT',
   con_name                  IN VARCHAR2  DEFAULT  NULL,
   top_n_detail_count        IN NUMBER    DEFAULT  NULL)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2 | IN | SQL_ID for which monitoring information should be displayed. Use NULL (the default) to report on the last statement monitored by Oracle. |
| session_id | NUMBER | IN | If not NULL , then this parameter targets only the subset of statements executed by the specified session. Default is NULL . Use -1 or USERENV (' SID ') for current session. |
| session_serial | NUMBER | IN | In addition to the session_id parameter, you can also specify its session serial to ensure that the desired session incarnation is targeted. This parameter is ignored when session_id is NULL . |
| inst_id | NUMBER | IN | Only considers statements started on the specified instance. Use -1 to target the login instance. NULL (default) targets all instances. |
| active_since_date | DATE | IN | If not NULL (default), returns only monitored statements active since the specified time. This includes all statements that are still executing along with all statements that have completed their execution after the specified date and time. |
| active_since_sec | NUMBER | IN | Same as active_since_date but with the date specified relative to the current SYSDATE minus a specified number of seconds. For example, use 3600 to apply a limit of 1 hour. |
| active_before_date | DATE | IN | If not NULL (default), returns only monitored statements that have been active before the specified date and time. |
| last_refresh_time | DATE | IN | If not NULL (default), the date and time when the list report was last retrieved. This optimizes the case where an application shows the list and refreshes the report on a regular basis (such as once every 5 seconds). In this case, the report shows detail about the execution of monitored queries that active since the specified last_refresh_time . For other queries, the report returns the execution key ( sql_id , sql_exec_start , sql_exec_id ). For queries with a first refresh time after the specified date, the function returns only the SQL execution key and statistics. |
| dbop_name | VARCHAR2 | IN | DB operation name. Specify NULL to display all the monitored DB operations. |
| monitor_type | NUMBER | IN | Type of the SQL Monitor operation. Specify one of the following values: MONITOR_TYPE_SQL - Returns only SQL statements MONITOR_TYPE_DBOP - Returns only database operations MONITOR_TYPE_ALL - Returns SQL statements as well as database operations |
| max_sqltext_length | NUMBER | IN | Maximum length of the SQL text. Default is NULL (no limit). |
| top_n_count | NUMBER | IN | Limits the number of top-N SQL statements that need to be included in the report. |
| top_n_rankby | VARCHAR2 | IN | Specifies the attribute to rank the SQL statements. Specify this value when top_n_count value is not NULL . The ranking of an SQL statement is done based on one of the following values: LAST_ACTIVE_TIME - Last active date and time (top N most recent) DURATION - Total duration of execution DB_TIME - DB time used CPU_TIME - CPU time used IO_REQUESTS - Number of I/O requests IO_BYTES - Number of I/O bytes |
| report_level | VARCHAR2 | IN | Level of detail for the report. The level is one of the following: BASIC - SQL text up to 200 characters TYPICAL - include full SQL text assuming that cursor has not aged out, in which case the SQL text is included up to 2000 characters ALL - currently the same as TYPICAL |
| auto_refresh | NUMBER | IN | Currently non-operational, reserved for future use. |
| base_path | VARCHAR2 | IN | URL path for flex HTML resources because flex HTML format is required to access external files (java scripts and the flash SWF file itself). |
| type | VARCHAR2 | IN | Report format: TEXT (default), HTML , or XML . |
| con_name | VARCHAR2 | IN | Name of the multitenant container database (CDB) |
| top_n_detail_count | NUMBER | IN | Limits the number of top-N SQL statements for which the SQL monitor details need to be included in the report. |

**Returns:** `CLOB`

## Usage Notes

Use the REPORT_SQL_MONITOR Function to get detailed monitoring information for a single SQL statement. See Also: Real-Time SQL Monitoring for other subprograms in this group See Also: Real-Time SQL Monitoring for other subprograms in this group Syntax DBMS_SQLTUNE.REPORT_SQL_MONITOR_LIST( sql_id IN VARCHAR2 DEFAULT NULL, session_id IN NUMBER DEFAULT NULL, session_serial IN NUMBER DEFAULT NULL, inst_id IN NUMBER DEFAULT NULL, active_since_date IN DATE DEFAULT NULL, active_since_sec IN NUMBER DEFAULT NULL, active_before_date IN DATE DEFAULT NULL, last_refresh_time IN DATE DEFAULT NULL, dbop_name IN VARCHAR2 DEFAULT NULL, monitor_type IN NUMBER DEFAULT MONITOR_TYPE_ALL, max_sqltext_length IN NUMBER DEFAULT NULL, top_n_count IN NUMBER DEFAULT NULL, top_n_rankby IN VARCHAR2 DEFAULT 'LAST_ACTIVE_TIME', report_level IN VARCHAR2 DEFAULT 'TYPICAL', auto_refresh IN NUMBER DEFAULT NULL, base_path IN VARCHAR2 DEFAULT NULL, type IN VARCHAR2 DEFAULT 'TEXT', con_name IN VARCHAR2 DEFAULT NULL, top_n_detail_count IN NUMBER DEFAULT NULL) RETURN CLOB; Parameters Table 169-34 REPORT_SQL_MONITOR_LIST Function Parameters Parameter Description sql_id SQL_ID for which monitoring information should be displayed. Use NULL (the default) to report on the last statement monitored by Oracle. session_id If not NULL , then this parameter targets only the subset of statements executed by the specified session. Default is NULL . Use -1 or USERENV (' SID ') for current session. session_serial In addition to the session_id parameter, you can also specify its session serial to ensure that the desired session incarnation is targeted. This parameter is ignored when session_id is NULL . inst_id Only considers statements started on the specified instance. Use -1 to target the login instance. NULL (default) targets all instances. active_since_date If not NULL (default), returns only monitored statements active since the specified time. This includes all statements that are still executing along with all statements that have completed their execution after the specified date and time. active_since_sec Same as active_since_date but with the date specified relative to the current SYSDATE minus a specified number of seconds. For example, use 3600 to apply a limit of 1 hour. active_before_date If not NULL (default), returns only monitored statements that have been active before the specified date and time. last_refresh_time If not NULL (default), the date and time when the list report was last retrieved. This optimizes the case where an application shows the list and refreshes the report on a regular basis (such as once every 5 seconds). In this case, the report shows detail about the execution of monitored queries that active since the specified last_refresh_time . For other queries, the report returns the execution key ( sql_id , sql_exec_start , sql_exec_id ). For queries with a first refresh time after the specified date, the function returns only the SQL execution key and statistics. dbop_name DB operation name. Specify NULL to display all the monitored DB operations. monitor_type Type of the SQL Monitor operation. Specify one of the following values: MONITOR_TYPE_SQL - Returns only SQL statements MONITOR_TYPE_DBOP - Returns only database operations MONITOR_TYPE_ALL - Returns SQL statements as well as database operations max_sqltext_length Maximum length of the SQL text. Default is NULL (no limit). top_n_count Limits the number of top-N SQL statements that need to be included in the report. top_n_rankby Specifies the attribute to rank the SQL statements. Specify this value when top_n_count value is not NULL . The ranking of an SQL statement is done based on one of the following values: LAST_ACTIVE_TIME - Last active date and time (top N most recent) DURATION - Total duration of execution DB_TIME - DB time used CPU_TIME - CPU time used IO_REQUESTS - Number of I/O requests IO_BYTES - Number of I/O bytes report_level Level of detail for the report. The level is one of the following: BASIC - SQL text up to 200 characters TYPICAL - include full SQL text assuming that cursor has not aged out, in which case the SQL text is included up to 2000 characters ALL - currently the same as TYPICAL auto_refresh Currently non-operational, reserved for future use. base_path URL path for flex HTML resources because flex HTML format is required to access external files (java scripts and the flash SWF file itself). type Report format: TEXT (default), HTML , or XML . con_name Name of the multitenant container database (CDB) top_n_detail_count Limits the number of top-N SQL statements for which the SQL monitor details need to be included in the report. Return Values A report for the list of SQL statements that have been monitored. The report type is text, XML, or HTML.