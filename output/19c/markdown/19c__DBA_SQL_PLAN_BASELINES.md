---
id: 19c__DBA_SQL_PLAN_BASELINES
name: DBA_SQL_PLAN_BASELINES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_SQL_PLAN_BASELINES.html
---

# DBA_SQL_PLAN_BASELINES

DBA_SQL_PLAN_BASELINES displays information about the SQL plan baselines currently created for specific SQL statements.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SIGNATURE | NUMBER | Unique SQL identifier generated from normalized SQL text |
| SQL_HANDLE | VARCHAR2(128) | Unique SQL identifier in string form as a search key |
| SQL_TEXT | CLOB | Un-normalized SQL text |
| PLAN_NAME | VARCHAR2(128) | Unique plan identifier in string form as a search key |
| CREATOR | VARCHAR2(128) | User who created the plan baseline |
| ORIGIN | VARCHAR2(14) | How the plan baseline was created: MANUAL-LOAD AUTO-CAPTURE MANUAL-SQLTUNE AUTO-SQLTUNE |
| PARSING_SCHEMA_NAME | VARCHAR2(128) | Name of the parsing schema |
| DESCRIPTION | VARCHAR2(500) | Text description provided for the plan baseline |
| VERSION | VARCHAR2(64) | Database version at the time of plan baseline creation |
| CREATED | TIMESTAMP(6) | Timestamp when the plan baseline was created |
| LAST_MODIFIED | TIMESTAMP(6) | Timestamp when the plan baseline was last modified |
| LAST_EXECUTED | TIMESTAMP(6) | Timestamp when the plan baseline was last executed Note: For performance reasons, this column is not updated immediately after each execution of the plan baseline. Therefore, the plan baseline may have been executed more recently than the value of this column indicates. |
| LAST_VERIFIED | TIMESTAMP(6) | Timestamp when the plan baseline was last verified |
| ENABLED | VARCHAR2(3) | Indicates whether the plan baseline is enabled ( YES ) or disabled ( NO ) |
| ACCEPTED | VARCHAR2(3) | Indicates whether the plan baseline is accepted ( YES ) or not ( NO ) |
| FIXED | VARCHAR2(3) | Indicates whether the plan baseline is fixed ( YES ) or not ( NO ) |
| REPRODUCED | VARCHAR2(3) | Indicates whether the optimizer was able to reproduce the plan ( YES ) or not ( NO ). The value of this column is set to YES when a plan is initially added to the plan baseline. |
| AUTOPURGE | VARCHAR2(3) | Indicates whether the plan baseline is auto-purged ( YES ) or not ( NO ) |
| ADAPTIVE | VARCHAR2(3) | Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not. When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan will be added to the SQL plan baseline as an unaccepted plan, and the ADAPTIVE column will be marked YES . When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed and the final plan determined at execution will become an accepted plan if its performance is better than the existing plan baseline. At this point, the value of the ADAPTIVE column is set to NO since the plan is no longer adaptive, but resolved. |
| OPTIMIZER_COST | NUMBER | Optimizer cost at the time the plan baseline was created |
| MODULE | VARCHAR2(64) | Application module name |
| ACTION | VARCHAR2(64) | Application action |
| EXECUTIONS Foot 1 | NUMBER | Number of executions at the time the plan baseline was created |
| ELAPSED_TIME Foot 1 | NUMBER | Total elapsed time (in microseconds) at the time the plan baseline was created |
| CPU_TIME Foot 1 | NUMBER | Total CPU time (in microseconds) at the time the plan baseline was created |
| BUFFER_GETS Foot 1 | NUMBER | Total buffer gets at the time the plan baseline was created |
| DISK_READS Foot 1 | NUMBER | Total disk reads at the time the plan baseline was created |
| DIRECT_WRITES Foot 1 | NUMBER | Total direct writes at the time the plan baseline was created |
| ROWS_PROCESSED Foot 1 | NUMBER | Total rows processed at the time the plan baseline was created |
| FETCHES Foot 1 | NUMBER | Total number of fetches at the time the plan baseline was created |
| END_OF_FETCH_COUNT Foot 1 | NUMBER | Total number of full fetches at the time the plan baseline was created |

## Usage Notes

See Also: Oracle Database SQL Tuning Guide for more information about SQL plan baselines The DBMS_SQLTUNE package in Oracle Database PL/SQL Packages and Types Reference See Also: Oracle Database SQL Tuning Guide for more information about SQL plan baselines The DBMS_SQLTUNE package in Oracle Database PL/SQL Packages and Types Reference