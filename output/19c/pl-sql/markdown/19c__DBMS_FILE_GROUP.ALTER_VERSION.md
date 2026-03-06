---
id: 19c__DBMS_FILE_GROUP.ALTER_VERSION
name: DBMS_FILE_GROUP.ALTER_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.ALTER_VERSION

This procedure alters a version of a file group.

## Syntax

```sql
DBMS_FILE_GROUP.ALTER_VERSION( 
  file_group_name           IN  VARCHAR2, 
  version_name              IN  VARCHAR2  DEFAULT NULL,
  new_version_name          IN  VARCHAR2  DEFAULT NULL,
  remove_version_name       IN  VARCHAR2  DEFAULT 'N',
  new_default_directory     IN  VARCHAR2  DEFAULT NULL,
  remove_default_directory  IN  VARCHAR2  DEFAULT 'N',
  new_comments              IN  VARCHAR2  DEFAULT NULL,
  remove_comments           IN  VARCHAR2  DEFAULT 'N');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2 | IN | The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| version_name | VARCHAR2 | IN | The name of the version being altered. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then version 1 of the file group is altered. If '*' is specified, then the procedure alters all versions, and the new_version_name parameter must be NULL . If NULL , then the procedure uses the version with the latest creation time for the file group. |
| new_version_name | VARCHAR2 | IN | The new name of the version. Do not specify a schema. The specified version name cannot be a positive integer or an asterisk ( '*' ). If NULL , then the procedure does not change the version name. |
| remove_version_name | VARCHAR2 | IN | If Y , then the procedure removes the version name. If the version name is removed, then the version number must be used to manage the version. If Y and the new_version_name parameter is set to a non- NULL value, then the procedure raises an error. If N , then the procedure does not remove the version name. |
| new_default_directory | VARCHAR2 | IN | The default directory object used when files are added to a version if no directory is specified when the files are added. If NULL , then the procedure does not change the default directory. |
| remove_default_directory | VARCHAR2 | IN | If Y , then the procedure removes the default directory. If Y and the new_default_directory parameter is set to a non- NULL value, then the procedure raises an error. If N , then the procedure does not remove the default directory. |
| new_comments | VARCHAR2 | IN | Comments about the version. If non- NULL , then the new comments replace the existing comments for the version. If NULL , then the procedure does not change the comments. |
| remove_comments | VARCHAR2 | IN | If Y , then the procedure removes the comments for the version. If Y and the new_comments parameter is set to a non- NULL value, then the procedure raises an error. If N , then the procedure does not remove the comments for the version. |

## Usage Notes

Syntax DBMS_FILE_GROUP.ALTER_VERSION( file_group_name IN VARCHAR2, version_name IN VARCHAR2 DEFAULT NULL, new_version_name IN VARCHAR2 DEFAULT NULL, remove_version_name IN VARCHAR2 DEFAULT 'N', new_default_directory IN VARCHAR2 DEFAULT NULL, remove_default_directory IN VARCHAR2 DEFAULT 'N', new_comments IN VARCHAR2 DEFAULT NULL, remove_comments IN VARCHAR2 DEFAULT 'N'); Parameters Table 70-6 ALTER_VERSION Procedure Parameters Parameter Description file_group_name The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. version_name The name of the version being altered. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then version 1 of the file group is altered. If '*' is specified, then the procedure alters all versions, and the new_version_name parameter must be NULL . If NULL , then the procedure uses the version with the latest creation time for the file group. new_version_name The new name of the version. Do not specify a schema. The specified version name cannot be a positive integer or an asterisk ( '*' ). If NULL , then the procedure does not change the version name. remove_version_name If Y , then the procedure removes the version name. If the version name is removed, then the version number must be used to manage the version. If Y and the new_version_name parameter is set to a non- NULL value, then the procedure raises an error. If N , then the procedure does not remove the version name. new_default_directory The default directory object used when files are added to a version if no directory is specified when the files are added. If NULL , then the procedure does not change the default directory. remove_default_directory If Y , then the procedure removes the default directory. If Y and the new_default_directory parameter is set to a non- NULL value, then the procedure raises an error. If N , then the procedure does not remove the default directory. new_comments Comments about the version. If non- NULL , then the new comments replace the existing comments for the version. If NULL , then the procedure does not change the comments. remove_comments If Y , then the procedure removes the comments for the version. If Y and the new_comments parameter is set to a non- NULL value, then the procedure raises an error. If N , then the procedure does not remove the comments for the version.