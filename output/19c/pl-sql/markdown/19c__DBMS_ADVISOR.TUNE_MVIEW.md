---
id: 19c__DBMS_ADVISOR.TUNE_MVIEW
name: DBMS_ADVISOR.TUNE_MVIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.TUNE_MVIEW

This procedure shows how to decompose a materialized view into multiple views and to restate the materialized view to be optimized for fast refresh and query rewrite. It also shows how to fix materialized view logs and to enable query rewrite.

## Syntax

```sql
DBMS_ADVISOR.TUNE_MVIEW (
   task_name        IN OUT VARCHAR2, 
   mv_create_stmt   IN     [CLOB | VARCHAR2]);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN OUT | The task name for querying the results in a catalog view. If not specified, the database generates a task name, and then returns. |
| mv_create_stmt | IN | IN | The original materialized view creation statement. |

## Usage Notes

Syntax DBMS_ADVISOR.TUNE_MVIEW ( task_name IN OUT VARCHAR2, mv_create_stmt IN [CLOB | VARCHAR2]); Parameters Table 16-39 TUNE_MVIEW Procedure Parameters Parameter Description task_name The task name for querying the results in a catalog view. If not specified, the database generates a task name, and then returns. mv_create_stmt The original materialized view creation statement. Usage Notes Executing TUNE_MVIEW generates two sets of output results: one for the implementation, and the other for undoing the implementation. The output is accessible through USER_TUNE_MVIEW and DBA_TUNE_MVIEW views. You can also use DBMS_ADVISOR.GET_TASK_SCRIPT and DBMS_ADVISOR.CREATE_FILE to print the TUNE_MVIEW results into a script file for later execution. Table 16-40 USER_TUNE_MVIEW and DBA_TUNE_MVIEW Views Column Name Column Description OWNER The name of the materialized view owner. TASK_NAME The name of the task. This name serves as a key to access the set of recommendations. SCRIPT_TYPE Recommendation ID that indicates whether the row is for the IMPLEMENTATION or UNDO script. ACTION_ID Action ID used as the command order number. STATEMENT For TUNE_MVIEW output, this column represents the following statements, and includes statement properties such as REFRESH and REWRITE options: CREATE MATERIALIZED VIEW LOG ALTER MATERIALIZED VIEW LOG FORCE [CREATE | DROP] MATERIALIZED VIEW Examples The following example shows how to use TUNE_MVIEW to optimize a CREATE MATERIALIZED VIEW statement: DECLARE v_tname VARCHAR2(30); BEGIN v_tname := 'mview_task'; DBMS_ADVISOR.TUNE_MVIEW( task_name => v_tname , mv_create_stmt => 'CREATE MATERIALIZED VIEW omv REFRESH WITH ROWID AS SELECT * FROM orders'); END; You can view the results by querying USER_TUNE_MVIEW or DBA_TUNE_MVIEW as the following example (sample output included): SET LINESIZE 120 COL TASK_NAME FORMAT a20 COL STATEMENT FORMAT a40 SELECT * FROM USER_TUNE_MVIEW WHERE TASK_NAME='mview_task' AND SCRIPT_TYPE='IMPLEMENTATION'; TASK_NAME ACTION_ID SCRIPT_TYPE STATEMENT -------------------- ---------- -------------- ---------------------------------------- mview_task 1 IMPLEMENTATION CREATE MATERIALIZED VIEW LOG ON "OE"."OR DERS" WITH ROWID mview_task 2 IMPLEMENTATION ALTER MATERIALIZED VIEW LOG FORCE ON "OE "."ORDERS" ADD ROWID mview_task 3 IMPLEMENTATION CREATE MATERIALIZED VIEW OE.OMV REFRESH FAST WITH ROWID DISABLE QUERY REWRITE Alternatively, you can save the output results in an external script file as in the following example: CREATE DIRECTORY TUNE_RESULTS_DIR AS '/tmp'; GRANT READ, WRITE ON DIRECTORY TUNE_RESULTS_DIR TO PUBLIC; BEGIN DBMS_ADVISOR.CREATE_FILE( buffer => DBMS_ADVISOR.GET_TASK_SCRIPT( task_name => 'mview_task') , location => 'TUNE_RESULTS_DIR' , filename => 'mview_create.sql' ); END; The preceding statement will save the results in /tmp/mview_create.sql . See Also: Oracle Database SQL Tuning Guide for more information about using the TUNE_MVIEW procedure See Also: Oracle Database SQL Tuning Guide for more information about using the TUNE_MVIEW procedure