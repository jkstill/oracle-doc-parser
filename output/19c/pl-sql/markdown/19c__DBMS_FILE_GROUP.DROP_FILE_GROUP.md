---
id: 19c__DBMS_FILE_GROUP.DROP_FILE_GROUP
name: DBMS_FILE_GROUP.DROP_FILE_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.DROP_FILE_GROUP

This procedure drops a file group.

## Syntax

```sql
DBMS_FILE_GROUP.DROP_FILE_GROUP(
  file_group_name  IN  VARCHAR2,
  keep_files       IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2 | IN | The name of the file group being dropped, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| keep_files | VARCHAR2 | IN | If Y , then the procedure retains the files in the file group on hard disk. If N , then the procedure deletes the files in the file group from hard disk. If NULL , then the procedure uses the default keep files property of the file group. |

## Usage Notes

Syntax DBMS_FILE_GROUP.DROP_FILE_GROUP( file_group_name IN VARCHAR2, keep_files IN VARCHAR2 DEFAULT NULL); Parameters Table 70-9 DROP_FILE_GROUP Procedure Parameters Parameter Description file_group_name The name of the file group being dropped, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. keep_files If Y , then the procedure retains the files in the file group on hard disk. If N , then the procedure deletes the files in the file group from hard disk. If NULL , then the procedure uses the default keep files property of the file group. Usage Notes If this procedure deletes files on hard disk, then the user who runs the procedure must have WRITE privilege on the directory object that contains the files.