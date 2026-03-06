---
id: 19c__DBMS_SQLPA.CREATE_ANALYSIS_TASK
name: DBMS_SQLPA.CREATE_ANALYSIS_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.CREATE_ANALYSIS_TASK

These functions create an advisor task to process and analyze one or more SQL statements.

## Syntax

```sql
DBMS_SQLPA.CREATE_ANALYSIS_TASK(
  sql_text         IN CLOB,
  bind_list        IN sql_binds := NULL,
  parsing_schema   IN VARCHAR2  := NULL,
  task_name        IN VARCHAR2  := NULL,
  description      IN VARCHAR2  := NULL)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB | IN | Text of a SQL statement |
| bind_list | sql_binds | IN | A set of bind values |
| parsing_schema | VARCHAR2 | IN | Name of the schema where the statement can be compiled |
| task_name | VARCHAR2 | IN | Optional analysis task name |
| dbid |  |  | The DBID for imported or PDB-level AWR data. If NULL , then the current database DBID is used |
| con_name |  |  | Container for the SPA task. The semantics depend on the function format: For the SQL ID format, this parameter specifies the container from which the database fetches the SQL statement for using with SPA. SPA will analyze the statement in this container. If null, then the database uses the current PDB for SPA analysis. For the AWR format, this parameter specifies the container from whose AWR data the database fetches the SQL statement for using with SPA. SPA will analyze the statement in this container. If null, then the database uses the current PDB for SPA analysis. The following statements are true of all function formats: In a non-CDB, this parameter is ignored. In a PDB, this parameter must be null or match the container name of the PDB. Otherwise, error occurs. In a CDB root, this parameter must be null or match the container name of a container in this CDB. Otherwise, error occurs. |
| description | VARCHAR2 | IN | Description of the SQL analysis task to a maximum of 256 characters |
| sql_id |  |  | Identifier of a SQL statement |
| plan_hash_value |  |  | Hash value of the SQL execution plan |
| begin_snap |  |  | Begin snapshot identifier |
| end_snap |  |  | End snapshot identifier |
| sqlset_name |  |  | SQL tuning set name |
| basic_filter |  |  | SQL predicate to filter the SQL from the SQL tuning set |
| order_by |  |  | Order-by clause on the selected SQL |
| top_sql |  |  | Top N SQL after filtering and ranking |
| sqlset_owner |  |  | The owner of the SQL tuning set, or NULL for the current schema owner |

**Returns:** `VARCHAR2`

## Usage Notes

You can use different forms of this function to: Create an analysis task for a single statement given its text. Create an analysis task for a single statement from the cursor cache given its identifier. Create an analysis task for a single statement from the workload repository given a range of snapshot identifiers. Create an analysis task for a SQL tuning set. In all cases, the function creates an advisor task and sets its parameters. Syntax SQL text format. This form of the function is called to prepare the analysis of a single statement given its text. DBMS_SQLPA.CREATE_ANALYSIS_TASK( sql_text IN CLOB, bind_list IN sql_binds := NULL, parsing_schema IN VARCHAR2 := NULL, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL) RETURN VARCHAR2; SQL ID format. This form of the function is called to prepare the analysis of a single statement from the cursor cache given its identifier. DBMS_SQLPA.CREATE_ANALYSIS_TASK( sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, task_name IN VARCHAR2 := NULL, con_name IN VARCHAR2 DEFAULT, description IN VARCHAR2 := NULL) RETURN VARCHAR2; Workload Repository format. This form of the function is called to prepare the analysis of a single statement from the workload repository given a range of snapshot identifiers. DBMS_SQLPA.CREATE_ANALYSIS_TASK( dbid IN NUMBER DEFAULT, begin_snap IN NUMBER, end_snap IN NUMBER, sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL) con_name IN VARCHAR2 DEFAULT, RETURN VARCHAR2; SQLSET format. This form of the function is called to prepare the analysis of a SQL tuning set. DBMS_SQLPA.CREATE_ANALYSIS_TASK( sqlset_name IN VARCHAR2, basic_filter IN VARCHAR2 := NULL, con_name IN VARCHAR2 DEFAULT, order_by IN VARCHAR2 := NULL, top_sql IN VARCHAR2 := NULL, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL sqlset_owner IN VARCHAR2 := NULL) RETURN VARCHAR2; Parameters Table 166-3 CREATE_ANALYSIS_TASK Function Parameters Parameter Description sql_text Text of a SQL statement bind_list A set of bind values parsing_schema Name of the schema where the statement can be compiled task_name Optional analysis task name dbid The DBID for imported or PDB-level AWR data. If NULL , then the current database DBID is used con_name Container for the SPA task. The semantics depend on the function format: For the SQL ID format, this parameter specifies the container from which the database fetches the SQL statement for using with SPA. SPA will analyze the statement in this container. If null, then the database uses the current PDB for SPA analysis. For the AWR format, this parameter specifies the container from whose AWR data the database fetches the SQL statement for using with SPA. SPA will analyze the statement in this container. If null, then the database uses the current PDB for SPA analysis. The following statements are true of all function formats: In a non-CDB, this parameter is ignored. In a PDB, this parameter must be null or match the container name of the PDB. Otherwise, error occurs. In a CDB root, this parameter must be null or match the container name of a container in this CDB. Otherwise, error occurs. description Description of the SQL analysis task to a maximum of 256 characters sql_id Identifier of a SQL statement plan_hash_value Hash value of the SQL execution plan begin_snap Begin snapshot identifier end_snap End snapshot identifier sqlset_name SQL tuning set name basic_filter SQL predicate to filter the SQL from the SQL tuning set order_by Order-by clause on the selected SQL top_sql Top N SQL after filtering and ranking sqlset_owner The owner of the SQL tuning set, or NULL for the current schema owner Return Values A SQL analysis task name that is unique by user (two different users can give the same name to their advisor tasks). Examples variable stmt_task VARCHAR2(64); variable sts_task VARCHAR2(64); -- Sql text format EXEC :stmt_task := DBMS_SQLPA.CREATE_ANALYSIS_TASK( sql_text => 'select quantity_sold from sales s, times t where s.time_id = t.time_id and s.time_id = TO_DATE(''24-NOV-00'')'); -- Sql id format (cursor cache) EXEC :stmt_task := DBMS_SQLPA.CREATE_ANALYSIS_TASK( sql_id => 'ay1m3ssvtrh24'); -- Workload repository format exec :stmt_task := DBMS_SQLPA.CREATE_ANALYSIS_TASK( begin_snap => 1, end_snap => 2, sql_id => 'ay1m3ssvtrh24'); -- Sql tuning set format (first we need to load an STS, then analyze it) EXEC :sts_task := DBMS_SQLPA.CREATE_ANALYSIS_TASK( - sqlset_name => 'my_workload', - order_by => 'BUFFER_GETS', - description => 'process workload ordered by buffer gets');