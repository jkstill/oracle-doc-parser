---
id: 19c__DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET
name: DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET

This procedure captures a workload from the shared SQL area into a SQL tuning set.

## Syntax

```sql
DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET (
    sqlset_name         IN VARCHAR2, 
    time_limit          IN POSITIVE := 1800,
    repeat_interval     IN POSITIVE := 300,
    capture_option      IN VARCHAR2 := 'MERGE',
    capture_mode        IN NUMBER   := MODE_REPLACE_OLD_STATS,
    basic_filter        IN VARCHAR2 := NULL,
    sqlset_owner        IN VARCHAR2 := NULL,
    recursive_sql       IN VARCHAR2 := HAS_RECURSIVE_SQL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the SQL tuning set name |
| time_limit | POSITIVE | IN | Defines the total amount of time, in seconds, to execute. |
| repeat_interval | POSITIVE | IN | Defines the amount of time, in seconds, to pause between sampling. |
| capture_option | VARCHAR2 | IN | Specifies whether to insert new statements, update existing statements, or both. Values are INSERT , UPDATE , or MERGE . The values are the same as for load_option in load_sqlset . |
| capture_mode | NUMBER | IN | Specifies the capture mode ( UPDATE and MERGE capture options). Possible values: MODE_REPLACE_OLD_STATS — Replaces statistics when the number of executions is greater than the number stored in the SQL tuning set MODE_ACCUMULATE_STATS — Adds new values to current values for SQL that is already stored. Note that this mode detects if a statement has been aged out, so the final value for a statistics is the sum of the statistics of all cursors that statement existed under. |
| basic_filter | VARCHAR2 | IN | Defines a filter to apply to the shared SQL area for each sample. If basic_filter is not set by the caller, then the subprogram captures only statements of type CREATE TABLE , INSERT , SELECT , UPDATE , DELETE , and MERGE . |
| sqlset_owner | VARCHAR2 | IN | Specifies the owner of the SQL tuning set or NULL for current schema owner |
| recursive_sql | VARCHAR2 | IN | Defines a filter that includes recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL ) or excludes it ( NO_RECURSIVE_SQL ). |

## Usage Notes

The procedure polls the cache multiple times over a time period, and updates the workload data stored there. It can execute over as long a period as required to capture an entire system workload. See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET ( sqlset_name IN VARCHAR2, time_limit IN POSITIVE := 1800, repeat_interval IN POSITIVE := 300, capture_option IN VARCHAR2 := 'MERGE', capture_mode IN NUMBER := MODE_REPLACE_OLD_STATS, basic_filter IN VARCHAR2 := NULL, sqlset_owner IN VARCHAR2 := NULL, recursive_sql IN VARCHAR2 := HAS_RECURSIVE_SQL); Parameters The parameters are the same for both DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET and DBMS_SQLSET.CAPTURE_CURSOR_CACHE . Table 169-13 CAPTURE_CURSOR_CACHE_SQLSET and CAPTURE_CURSOR_CACHE Procedure Parameters Parameter Description sqlset_name Specifies the SQL tuning set name time_limit Defines the total amount of time, in seconds, to execute. repeat_interval Defines the amount of time, in seconds, to pause between sampling. capture_option Specifies whether to insert new statements, update existing statements, or both. Values are INSERT , UPDATE , or MERGE . The values are the same as for load_option in load_sqlset . capture_mode Specifies the capture mode ( UPDATE and MERGE capture options). Possible values: MODE_REPLACE_OLD_STATS — Replaces statistics when the number of executions is greater than the number stored in the SQL tuning set MODE_ACCUMULATE_STATS — Adds new values to current values for SQL that is already stored. Note that this mode detects if a statement has been aged out, so the final value for a statistics is the sum of the statistics of all cursors that statement existed under. basic_filter Defines a filter to apply to the shared SQL area for each sample. If basic_filter is not set by the caller, then the subprogram captures only statements of type CREATE TABLE , INSERT , SELECT , UPDATE , DELETE , and MERGE . sqlset_owner Specifies the owner of the SQL tuning set or NULL for current schema owner recursive_sql Defines a filter that includes recursive SQL in the SQL tuning set ( HAS_RECURSIVE_SQL ) or excludes it ( NO_RECURSIVE_SQL ). Examples In this example capture takes place over a 30-second period, polling the cache once every five seconds. This captures all statements run during that period but not before or after. If the same statement appears a second time, the process replaces the stored statement with the new occurrence. Note that in production systems the time limit and repeat interval would be set much higher. You should tune the time_limit and repeat_interval parameters based on the workload time and shared SQL area turnover properties of your system. EXEC DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET( - sqlset_name => 'my_workload', - time_limit => 30, - repeat_interval => 5); In the following call you accumulate execution statistics as you go. This option produces an accurate picture of the cumulative activity of each cursor, even across age-outs, but it is more expensive than the previous example. EXEC DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET( - sqlset_name => 'my_workload', - time_limit => 30, - repeat_interval => 5, - capture_mode => dbms_sqltune.MODE_ACCUMULATE_STATS); This call performs a very inexpensive capture where you only insert new statements and do not update their statistics once they have been inserted into the SQL tuning set EXEC DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET( - sqlset_name => 'my_workload', - time_limit => 30, - repeat_interval => 5, - capture_option => 'INSERT');