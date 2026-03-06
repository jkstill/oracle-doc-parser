---
id: 19c__DBMS_ADVISOR.CREATE_FILE
name: DBMS_ADVISOR.CREATE_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.CREATE_FILE

This procedure creates an external file from a PL/SQL CLOB variable, which is used for creating scripts and reports.

## Syntax

```sql
DBMS_ADVISOR.CREATE_FILE (
   buffer       IN  CLOB,
   location     IN  VARCHAR2,
   filename     IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| buffer | CLOB | IN | A CLOB buffer containing report or script information. |
| location | VARCHAR2 | IN | The name of the directory that will contain the output file. You must use the alias as defined by the CREATE DIRECTORY statement. The Advisor translates the alias into the actual directory location. |
| filename | VARCHAR2) | IN | The name of the output file. The file name can only contain the name and an optional file type of the form filename.filetype . |

## Usage Notes

Syntax DBMS_ADVISOR.CREATE_FILE ( buffer IN CLOB, location IN VARCHAR2, filename IN VARCHAR2); Parameters Table 16-7 CREATE_FILE Procedure Parameters Parameter Description buffer A CLOB buffer containing report or script information. location The name of the directory that will contain the output file. You must use the alias as defined by the CREATE DIRECTORY statement. The Advisor translates the alias into the actual directory location. filename The name of the output file. The file name can only contain the name and an optional file type of the form filename.filetype . Usage Notes You must embed all formatting within the CLOB . The database restricts file access within stored procedures. This means that file locations and names must adhere to the known file permissions in the server. Examples CREATE DIRECTORY MY_DIR as '/homedir/user4/gssmith'; GRANT READ,WRITE ON DIRECTORY MY_DIR TO PUBLIC; DECLARE v_task_id NUMBER; v_task_name VARCHAR2(30); v_workload_name VARCHAR2(30); BEGIN v_task_name := 'My Task'; v_workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK( advisor_name => DBMS_ADVISOR.SQLACCESS_ADVISOR , task_id => v_task_id , task_name => v_task_name ); DBMS_ADVISOR.CREATE_SQLWKLD( workload_name => v_workload_name , description => 'My Workload' ); DBMS_ADVISOR.ADD_SQLWKLD_REF( task_name => v_task_name , workload_name => v_workload_name); DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT( workload_name => v_workload_name , module => 'MONTHLY' , action => 'ROLLUP' , cpu_time => 100 , elapsed_time => 400 , disk_reads => 5041 , buffer_gets => 103 , rows_processed => 640445 , optimizer_cost => 680000 , executions => 2 , priority => 1 , last_execution_date => SYSDATE , stat_period => 1 , username => 'SH' , sql_text => 'SELECT AVG(amount_sold) FROM sh.sales' ); DBMS_ADVISOR.EXECUTE_TASK(v_task_name); DBMS_ADVISOR.CREATE_FILE( buffer => DBMS_ADVISOR.GET_TASK_SCRIPT(v_task_name) , location => 'MY_DIR' , filename => 'script.sql' ); END; /