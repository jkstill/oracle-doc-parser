---
id: 19c__DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_TEXT
name: DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_TEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_TEXT

This table function displays the ASH Spot report in text.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_TEXT(
   l_dbid          IN NUMBER,
   l_inst_num      IN NUMBER,
   l_btime         IN DATE,
   l_etime         IN DATE,
   l_options       IN NUMBER    DEFAULT 0,
   l_slot_width    IN NUMBER    DEFAULT 0,
   l_sid           IN NUMBER    DEFAULT NULL,
   l_sql_id        IN VARCHAR2  DEFAULT NULL,
   l_wait_class    IN VARCHAR2  DEFAULT NULL,
   l_service_hash  IN NUMBER    DEFAULT NULL,
   l_module        IN VARCHAR2  DEFAULT NULL,
   l_action        IN VARCHAR2  DEFAULT NULL,
   l_client_id     IN VARCHAR2  DEFAULT NULL,
   l_plsql_entry   IN VARCHAR2  DEFAULT NULL,
   l_data_src      IN NUMBER    DEFAULT 0,
   l_container     IN VARCHAR2  DEFAULT NULL)
 RETURN awrrpt_text_type_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| l_dbid | NUMBER | IN | Database identifier |
| l_inst_num | NUMBER | IN | Instance number |
| l_btime | DATE | IN | The 'begin time' |
| l_etime | DATE | IN | The 'end time' |
| l_options | NUMBER | IN | Report level (currently not used) |
| l_slot_width | NUMBER | IN | Specifies (in seconds) how wide the slots used in the "Top Activity" section of the report should be. This argument is optional, and if it is not specified the time interval between l_btime and l_etime is appropriately split into not more than 10 slots. |
| l_sid | NUMBER | IN | Session ID (see Usage Notes) |
| l_sql_id | VARCHAR2 | IN | SQL ID (see Usage Notes) |
| l_wait_class | VARCHAR2 | IN | Wait class name (see Usage Notes) |
| l_service_hash | NUMBER | IN | Service name hash (see Usage Notes) |
| l_module | VARCHAR2 | IN | Module name (see Usage Notes) |
| l_action | VARCHAR2 | IN | Action name (see Usage Notes) |
| l_client_id | VARCHAR2 | IN | Client ID for end-to-end backtracing (see Usage Notes) |
| l_plsql_entry | VARCHAR2 | IN | PL/SQL entry point (see Usage Notes) |
| l_data_src | NUMBER | IN | Can be used to specify a data source (see Usage Notes) 1 => memory ( V$ACTIVE_SESION_HISTORY) 2 => disk ( DBA_HIST_ACTIVE_SESS_HISTORY ) 0 => both. This is the default value. Here, the begin and end time parameters are used to get the samples from the appropriate data source, which can be memory, disk, or both. |
| l_container | VARCHAR2 | IN | Name of the container for which report activity is limited. Valid values other than NULL (default) should be taken from container names in V$CONTAINERS . Behavior is as follows: If NULL : When connected to a root container the report is on all containers. When connected to a PDB the report is on only that PDB. If not NULL : When connected to a root container the report is on activity from the specified container. When connected to a PDB the report is the same as NULL value for l_container regarding the connected PDB. Note: If while connected to a PDB you request information from another PDB this produces an empty report. |

**Returns:** `awrrpt_text_type_table`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_TEXT( l_dbid IN NUMBER, l_inst_num IN NUMBER, l_btime IN DATE, l_etime IN DATE, l_options IN NUMBER DEFAULT 0, l_slot_width IN NUMBER DEFAULT 0, l_sid IN NUMBER DEFAULT NULL, l_sql_id IN VARCHAR2 DEFAULT NULL, l_wait_class IN VARCHAR2 DEFAULT NULL, l_service_hash IN NUMBER DEFAULT NULL, l_module IN VARCHAR2 DEFAULT NULL, l_action IN VARCHAR2 DEFAULT NULL, l_client_id IN VARCHAR2 DEFAULT NULL, l_plsql_entry IN VARCHAR2 DEFAULT NULL, l_data_src IN NUMBER DEFAULT 0, l_container IN VARCHAR2 DEFAULT NULL) RETURN awrrpt_text_type_table PIPELINED; Parameters Table 192-11 ASH_REPORT_TEXT Parameters Parameter Description l_dbid Database identifier l_inst_num Instance number l_btime The 'begin time' l_etime The 'end time' l_options Report level (currently not used) l_slot_width Specifies (in seconds) how wide the slots used in the "Top Activity" section of the report should be. This argument is optional, and if it is not specified the time interval between l_btime and l_etime is appropriately split into not more than 10 slots. l_sid Session ID (see Usage Notes) l_sql_id SQL ID (see Usage Notes) l_wait_class Wait class name (see Usage Notes) l_service_hash Service name hash (see Usage Notes) l_module Module name (see Usage Notes) l_action Action name (see Usage Notes) l_client_id Client ID for end-to-end backtracing (see Usage Notes) l_plsql_entry PL/SQL entry point (see Usage Notes) l_data_src Can be used to specify a data source (see Usage Notes) 1 => memory ( V$ACTIVE_SESION_HISTORY) 2 => disk ( DBA_HIST_ACTIVE_SESS_HISTORY ) 0 => both. This is the default value. Here, the begin and end time parameters are used to get the samples from the appropriate data source, which can be memory, disk, or both. l_container Name of the container for which report activity is limited. Valid values other than NULL (default) should be taken from container names in V$CONTAINERS . Behavior is as follows: If NULL : When connected to a root container the report is on all containers. When connected to a PDB the report is on only that PDB. If not NULL : When connected to a root container the report is on activity from the specified container. When connected to a PDB the report is the same as NULL value for l_container regarding the connected PDB. Note: If while connected to a PDB you request information from another PDB this produces an empty report. Return Values The output will be one column of VARCHAR2(80) . Usage Notes You can call the function directly but Oracle recommends you use the ashrpti.sql script which prompts users for the required information. By default, the report uses the begin and end time parameters ( l_btime and l_etime , respectively) to find all rows in that time range either from memory, or disk, or both. However, using l_data_src , one can explicitly specify one of those data sources. For example, to generate an ASH report on all rows between l_btime and l_time found in memory, use l_data_src => 1 Similarly, to generate a report on samples found only on disk, use l_data_src => 2 The unspecified optional arguments are used to generate an ASH Reports that specify 'report targets' such as a SQL statement, or a session, or a particular Service/Module combination. These arguments are specified to restrict the ASH rows that would be used to generate the report. For example, to generate an ASH report on a particular SQL statement, such as SQL_ID ' abcdefghij123 ' pass that SQL_ID value to the l_sql_id argument: l_sql_id => 'abcdefghij123' Table 192-12 ASH_REPORT_TEXT: Wildcards Allowed (or Not) in Arguments Argument Name Comment Wildcard Allowed l_sid Session ID (for example, V$SESSION.SID ) No l_sql_id SQL ID (for example, V$SQL.SQL_ID ) Yes l_wait_class Wait class name (for example, V$EVENT_NAME.WAIT_CLASS ) Yes l_service_hash Service name hash (for example, V$ACTIVE_SERVICES.NAME_HASH ) No l_module Module name (for example, V$SESSION.MODULE ) Yes l_action Action name (for example, V$SESSION.ACTION ) Yes l_client_id Client ID for end-to-end backtracing (for example, V$SESSION.CLIENT_IDENTIFIER ) Yes l_plsql_entry PL/SQL entry point (for example, " SYS . DBMS_LOB .*") Yes l_data_src Wildcards are not allowed for l_data_src as it is of numeric datatype No Any combination of those optional arguments can be passed in, and only rows in ASH that satisfy all of those 'report targets' will be used. If multiple 'report targets' are specified, AND conditional logic is used to connect them. For example, to generate an ASH report on MODULE " PAYROLL " and ACTION " PROCESS ", use the following predicate: l_module => 'PAYROLL', l_action => 'PROCESS' Valid SQL wildcards can be used in all the arguments that are of type VARCHAR2 .