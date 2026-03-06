---
id: 19c__DBMS_ADDM.ANALYZE_DB
name: DBMS_ADDM.ANALYZE_DB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.ANALYZE_DB

This procedure creates an ADDM task for analyzing in database analysis mode and executes it.

## Syntax

```sql
DBMS_ADDM.ANALYZE_DB (
   task_name           IN OUT VARCHAR2,
   begin_snapshot      IN     NUMBER,
   end_snapshot        IN     NUMBER,
   db_id               IN     NUMBER := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN OUT | Name of the task to be created |
| begin_snapshot | NUMBER | IN | Number of the snapshot that starts the analysis period |
| end_snapshot | NUMBER | IN | Number of the snapshot that ends the analysis period |
| db_id | NUMBER | IN | Database ID for the database you to analyze. By default, this is the database currently connected |

## Usage Notes

Syntax DBMS_ADDM.ANALYZE_DB ( task_name IN OUT VARCHAR2, begin_snapshot IN NUMBER, end_snapshot IN NUMBER, db_id IN NUMBER := NULL); Parameters Table 14-2 ANALYZE_DB Procedure Parameters Parameter Description task_name Name of the task to be created begin_snapshot Number of the snapshot that starts the analysis period end_snapshot Number of the snapshot that ends the analysis period db_id Database ID for the database you to analyze. By default, this is the database currently connected Return Values The name of the created task is returned in the task_name parameter. It may be different from the value that is given as input (only in cases that name is already used by another task). Examples To create an ADDM task in database analysis mode and execute it, with its name in variable tname : var tname VARCHAR2(60); BEGIN :tname := 'my_database_analysis_mode_task'; DBMS_ADDM.ANALYZE_DB(:tname, 1, 2); END To see a report: SET LONG 100000 SET PAGESIZE 50000 SELECT DBMS_ADDM.GET_REPORT(:tname) FROM DUAL; Note that the return type of a report is a CLOB , formatted to fit line size of 80.