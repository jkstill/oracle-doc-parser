---
id: 19c__DBMS_FILE_GROUP.CREATE_VERSION
name: DBMS_FILE_GROUP.CREATE_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.CREATE_VERSION

This procedure creates a version of a file group.

## Syntax

```sql
DBMS_FILE_GROUP.CREATE_VERSION(
  file_group_name    IN  VARCHAR2,
  version_name       IN  VARCHAR2 DEFAULT NULL,
  default_directory  IN  VARCHAR2 DEFAULT NULL,
  comments           IN  VARCHAR2 DEFAULT NULL);

DBMS_FILE_GROUP.CREATE_VERSION(
  file_group_name    IN   VARCHAR2,
  version_name       IN   VARCHAR2 DEFAULT NULL,
  default_directory  IN   VARCHAR2 DEFAULT NULL,
  comments           IN   VARCHAR2 DEFAULT NULL,
  version_out        OUT  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2 | IN | The name of the file group to which the new version is added, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| version_name | VARCHAR2 | IN | The name of the version being created. Do not specify a schema. The specified version name cannot be a positive integer because, when a version is created, a version number is generated automatically. The specified version name cannot be an asterisk ( '*' ). |
| default_directory | VARCHAR2 | IN | The default directory object used when files are added to a version if no directory is specified when the files are added. |
| comments | VARCHAR2 | IN | Comments about the version being created |
| version_out | VARCHAR2) | OUT | If the version_name parameter is set to a non- NULL value, then this parameter contains the specified version name. If the version_name parameter is set to NULL , then this parameter contains the generated version number. |

## Usage Notes

This procedure automatically runs the PURGE_FILE_GROUP procedure. Therefore, versions can be purged based on the file group's retention policy. This procedure is overloaded. One version of the procedure contains the OUT parameter version_out , and the other does not. Syntax DBMS_FILE_GROUP.CREATE_VERSION( file_group_name IN VARCHAR2, version_name IN VARCHAR2 DEFAULT NULL, default_directory IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); DBMS_FILE_GROUP.CREATE_VERSION( file_group_name IN VARCHAR2, version_name IN VARCHAR2 DEFAULT NULL, default_directory IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL, version_out OUT VARCHAR2); Parameters Table 70-8 CREATE_VERSION Procedure Parameters Parameter Description file_group_name The name of the file group to which the new version is added, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. version_name The name of the version being created. Do not specify a schema. The specified version name cannot be a positive integer because, when a version is created, a version number is generated automatically. The specified version name cannot be an asterisk ( '*' ). default_directory The default directory object used when files are added to a version if no directory is specified when the files are added. comments Comments about the version being created version_out If the version_name parameter is set to a non- NULL value, then this parameter contains the specified version name. If the version_name parameter is set to NULL , then this parameter contains the generated version number. See Also: PURGE_FILE_GROUP Procedure See Also: PURGE_FILE_GROUP Procedure