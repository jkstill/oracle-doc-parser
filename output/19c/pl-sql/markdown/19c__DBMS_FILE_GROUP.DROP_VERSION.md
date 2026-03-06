---
id: 19c__DBMS_FILE_GROUP.DROP_VERSION
name: DBMS_FILE_GROUP.DROP_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.DROP_VERSION

This procedure drops a version of a file group.

## Syntax

```sql
DBMS_FILE_GROUP.DROP_VERSION( 
  file_group_name  IN  VARCHAR2, 
  version_name     IN  VARCHAR2 DEFAULT NULL,
  keep_files       IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2 | IN | The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| version_name | VARCHAR2 | IN | The name of the version being dropped. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then version 1 of the file group is dropped. If NULL , then the procedure uses the version with the oldest creation time for the file group. If '*' , then the procedure drops all versions. |
| keep_files | VARCHAR2 | IN | If Y , then the procedure retains the files in the version on hard disk. If N , then the procedure deletes the files in the version from hard disk. If NULL , then the procedure uses the default keep files property of the file group. |

## Usage Notes

Syntax DBMS_FILE_GROUP.DROP_VERSION( file_group_name IN VARCHAR2, version_name IN VARCHAR2 DEFAULT NULL, keep_files IN VARCHAR2 DEFAULT NULL); Parameters Table 70-10 DROP_VERSION Procedure Parameters Parameter Description file_group_name The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. version_name The name of the version being dropped. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then version 1 of the file group is dropped. If NULL , then the procedure uses the version with the oldest creation time for the file group. If '*' , then the procedure drops all versions. keep_files If Y , then the procedure retains the files in the version on hard disk. If N , then the procedure deletes the files in the version from hard disk. If NULL , then the procedure uses the default keep files property of the file group. Usage Notes If this procedure deletes files on hard disk, then the user who runs the procedure must have WRITE privilege on the directory object that contains the files.