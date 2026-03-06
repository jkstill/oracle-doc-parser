---
id: 19c__DBMS_ADDM.ANALYZE_INST
name: DBMS_ADDM.ANALYZE_INST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.ANALYZE_INST

This procedure creates an ADDM task for analyzing in instance analysis mode and executes it.

## Syntax

```sql
DBMS_ADDM.ANALYZE_INST (
   task_name                 IN OUT VARCHAR2,
   begin_snapshot            IN     NUMBER,
   end_snapshot              IN     NUMBER,
   cdb_type_override         IN     VARCHAR2,
   read_only_type_override   IN     VARCHAR2,
   instance_number           IN     NUMBER := NULL,
   db_id                     IN     NUMBER := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN OUT | Name of the task to be created |
| begin_snapshot | NUMBER | IN | Number of the snapshot that starts the analysis period |
| end_snapshot | NUMBER | IN | Number of the snapshot that ends the analysis period |
| cdb_type_override | VARCHAR2 | IN | Overrides the type of CDB that ADDM determines for doing analysis. The possible values are: AUTONOMOUS OLTP —autonomous OLTP inside a PDB AUTONOMOUS DATA WAREHOUSE —autonomous data warehouse (ADWH) inside a PDB PDB —a regular PDB CDB ROOT —the root of a CDB NON-CDB —a system that is not CDB or PDB AUTO —allows ADDM to decide the type of CDB to override based on the data |
| read_only_type_override | VARCHAR2 | IN | Overrides the type of CDB ADDM determines for analysis. The possible values are: READ-WRITE —a regular database or the primary database in a data guard configuration READ-ONLY —a database open in read-only mode, such as an active data guard standby AUTO —allows ADDM to decide the type of CDB to override based on the data |
| instance_number | NUMBER | IN | Number of the instance to analyze. By default it is the instance currently connected |
| db_id | NUMBER | IN | Database ID for the database you to analyze. By default, this is the database currently connected |

## Usage Notes

Syntax DBMS_ADDM.ANALYZE_INST ( task_name IN OUT VARCHAR2, begin_snapshot IN NUMBER, end_snapshot IN NUMBER, cdb_type_override IN VARCHAR2, read_only_type_override IN VARCHAR2, instance_number IN NUMBER := NULL, db_id IN NUMBER := NULL); Parameters Table 14-3 ANALYZE_INST Procedure Parameters Parameter Description task_name Name of the task to be created begin_snapshot Number of the snapshot that starts the analysis period end_snapshot Number of the snapshot that ends the analysis period cdb_type_override Overrides the type of CDB that ADDM determines for doing analysis. The possible values are: AUTONOMOUS OLTP —autonomous OLTP inside a PDB AUTONOMOUS DATA WAREHOUSE —autonomous data warehouse (ADWH) inside a PDB PDB —a regular PDB CDB ROOT —the root of a CDB NON-CDB —a system that is not CDB or PDB AUTO —allows ADDM to decide the type of CDB to override based on the data read_only_type_override Overrides the type of CDB ADDM determines for analysis. The possible values are: READ-WRITE —a regular database or the primary database in a data guard configuration READ-ONLY —a database open in read-only mode, such as an active data guard standby AUTO —allows ADDM to decide the type of CDB to override based on the data instance_number Number of the instance to analyze. By default it is the instance currently connected db_id Database ID for the database you to analyze. By default, this is the database currently connected Return Values The name of the created task is returned in the task_name parameter. It may be different from the value that is given as input (only in cases that name is already used by another task). Usage Notes On single instance systems (when not using Oracle RAC) the resulting task is identical to using the ANALYZE_DB procedure. Examples To create an ADDM task in instance analysis mode and execute it, with its name in variable tname : var tname VARCHAR2(60); BEGIN :tname := 'my_instance_analysis_mode_task'; DBMS_ADDM.ANALYZE_INST(:tname, 1, 2); END To see a report: SET LONG 100000 SET PAGESIZE 50000 SELECT DBMS_ADDM.GET_REPORT(:tname) FROM DUAL; Note that the return type of a report is a CLOB , formatted to fit line size of 80.