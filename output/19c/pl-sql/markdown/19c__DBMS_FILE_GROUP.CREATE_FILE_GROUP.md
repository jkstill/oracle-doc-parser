---
id: 19c__DBMS_FILE_GROUP.CREATE_FILE_GROUP
name: DBMS_FILE_GROUP.CREATE_FILE_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.CREATE_FILE_GROUP

This procedure creates a file group.

## Syntax

```sql
DBMS_FILE_GROUP.CREATE_FILE_GROUP(
  file_group_name    IN  VARCHAR2,
  keep_files         IN  VARCHAR2  DEFAULT 'Y',
  min_versions       IN  NUMBER    DEFAULT 2,
  max_versions       IN  NUMBER    DEFAULT DBMS_FILE_GROUP.INFINITE,
  retention_days     IN  NUMBER    DEFAULT DBMS_FILE_GROUP.INFINITE,
  default_directory  IN  VARCHAR2  DEFAULT NULL,
  comments           IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2 | IN | The name of the file group, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| keep_files | VARCHAR2 | IN | If Y , then the files in the file group are retained on hard disk if the file group or a version of the file group is dropped or purged. If N , then the files in the file group are deleted from hard disk if the file group or a version of the file group is dropped or purged. Note: If the file group is dropped because of a DROP USER CASCADE statement, then the setting of this parameter determines whether the files are dropped from the hard disk. |
| min_versions | NUMBER | IN | The minimum number of versions to retain. The specified value must be greater than or equal to 1 . |
| max_versions | NUMBER | IN | The maximum number of versions to retain. The specified value must be greater than or equal to the value specified for min_versions . When the number of versions exceeds the specified max_versions , the oldest version is purged. Specify DBMS_FILE_GROUP.INFINITE for no limit to the number of versions. |
| retention_days | NUMBER | IN | The maximum number of days to retain a version. The specified value must be greater than or equal to 0 (zero). When the age of a version exceeds the specified retention_days and there are more versions than the number specified in min_versions , the version is purged. The age of a version is calculated by subtracting the creation time from the current time. A decimal value can specify a fraction of a day. For example, 1.25 specifies one day and six hours. Specify DBMS_FILE_GROUP.INFINITE for no limit to the number of days a version can exist. |
| default_directory | VARCHAR2 | IN | The default directory object used when files are added to a file group if no directory is specified when the files are added, and no default directory object is specified for the version. |
| comments | VARCHAR2 | IN | Comments about the file group being created. |

## Usage Notes

Syntax DBMS_FILE_GROUP.CREATE_FILE_GROUP( file_group_name IN VARCHAR2, keep_files IN VARCHAR2 DEFAULT 'Y', min_versions IN NUMBER DEFAULT 2, max_versions IN NUMBER DEFAULT DBMS_FILE_GROUP.INFINITE, retention_days IN NUMBER DEFAULT DBMS_FILE_GROUP.INFINITE, default_directory IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 70-7 CREATE_FILE_GROUP Procedure Parameters Parameter Description file_group_name The name of the file group, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. keep_files If Y , then the files in the file group are retained on hard disk if the file group or a version of the file group is dropped or purged. If N , then the files in the file group are deleted from hard disk if the file group or a version of the file group is dropped or purged. Note: If the file group is dropped because of a DROP USER CASCADE statement, then the setting of this parameter determines whether the files are dropped from the hard disk. min_versions The minimum number of versions to retain. The specified value must be greater than or equal to 1 . max_versions The maximum number of versions to retain. The specified value must be greater than or equal to the value specified for min_versions . When the number of versions exceeds the specified max_versions , the oldest version is purged. Specify DBMS_FILE_GROUP.INFINITE for no limit to the number of versions. retention_days The maximum number of days to retain a version. The specified value must be greater than or equal to 0 (zero). When the age of a version exceeds the specified retention_days and there are more versions than the number specified in min_versions , the version is purged. The age of a version is calculated by subtracting the creation time from the current time. A decimal value can specify a fraction of a day. For example, 1.25 specifies one day and six hours. Specify DBMS_FILE_GROUP.INFINITE for no limit to the number of days a version can exist. default_directory The default directory object used when files are added to a file group if no directory is specified when the files are added, and no default directory object is specified for the version. comments Comments about the file group being created. Usage Notes If min_versions is set to 1 , then the only version of the file group can be purged when a new version is added. If the addition of the new version is not complete when the existing version is purged, then there can be a period of time when no version of the file group is available. Therefore, set min_versions to at least 2 if a version of the file group must be available at all times.