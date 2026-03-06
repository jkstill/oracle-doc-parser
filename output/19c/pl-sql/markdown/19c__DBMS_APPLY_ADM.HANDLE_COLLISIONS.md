---
id: 19c__DBMS_APPLY_ADM.HANDLE_COLLISIONS
name: DBMS_APPLY_ADM.HANDLE_COLLISIONS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.HANDLE_COLLISIONS

This procedure enables or disables basic conflict resolution for an apply process and a table.

## Syntax

```sql
DBMS_APPLY_ADM.HANDLE_COLLISIONS(
   apply_name    IN  VARCHAR2,
   enable        IN  BOOLEAN,
   object        IN  VARCHAR2,
   source_object IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_name | VARCHAR2 | IN | The name of the apply process. |
| enable | BOOLEAN | IN | If TRUE , then the following conflict resolution methods are used: When a conflict is detected for a row that exists in the table, the data in the row LCR overwrites the data in the table. When a conflict is detected for a row that does not exist in the table, the data in the row LCR is ignored. If FALSE then it disables conflict resolution set by this procedure for the specified apply process and object. If NULL , then removes any explicit table-level setting for collision handling for the specified apply process and object. |
| object | VARCHAR2 | IN | The schema and name of the target table, specified as [ schema_name .] table_name for the change of the setting. For example, if you are changing the setting for table employees owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default. |
| source_object | VARCHAR2 | IN | The schema and object name of the source table, specified as [ schema_name .] table_name for the table where the change originated. For example, if the change originated at the employees table owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default. |

## Usage Notes

Syntax DBMS_APPLY_ADM.HANDLE_COLLISIONS( apply_name IN VARCHAR2, enable IN BOOLEAN, object IN VARCHAR2, source_object IN VARCHAR2 DEFAULT NULL); Parameters Table 21-14 HANDLE_COLLISIONS Procedure Parameters Parameter Description apply_name The name of the apply process. enable If TRUE , then the following conflict resolution methods are used: When a conflict is detected for a row that exists in the table, the data in the row LCR overwrites the data in the table. When a conflict is detected for a row that does not exist in the table, the data in the row LCR is ignored. If FALSE then it disables conflict resolution set by this procedure for the specified apply process and object. If NULL , then removes any explicit table-level setting for collision handling for the specified apply process and object. object The schema and name of the target table, specified as [ schema_name .] table_name for the change of the setting. For example, if you are changing the setting for table employees owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default. source_object The schema and object name of the source table, specified as [ schema_name .] table_name for the table where the change originated. For example, if the change originated at the employees table owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default.