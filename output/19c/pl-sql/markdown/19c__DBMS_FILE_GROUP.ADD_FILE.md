---
id: 19c__DBMS_FILE_GROUP.ADD_FILE
name: DBMS_FILE_GROUP.ADD_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.ADD_FILE

This procedure adds a file to a version of a file group.

## Syntax

```sql
DBMS_FILE_GROUP.ADD_FILE(
  file_group_name  IN  VARCHAR2,
  file_name        IN  VARCHAR2,
  file_type        IN  VARCHAR2  DEFAULT NULL,
  file_directory   IN  VARCHAR2  DEFAULT NULL,
  version_name     IN  VARCHAR2  DEFAULT NULL,
  comments         IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2 | IN | The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| file_name | VARCHAR2 | IN | The name of the file being added to the version. Each file name in a version must be unique. |
| file_type | VARCHAR2 | IN | The file type. The following are reserved file types: If the file is a datafile, then enter the following: 'DATAFILE' If the file is a Data Pump export dump file, then enter the following: 'DUMPSET' Data Pump metadata is populated when a Data Pump export dump file is imported. If the file is a Data Pump export log file, then enter the following: 'DATAPUMPLOG' If the file type is not one of the reserved file types, then either enter a text description of the file type, or specify NULL to omit a file type description. See " Constants " for more information about the reserved file types. |
| file_directory | VARCHAR2 | IN | The name of the directory object that corresponds to the directory containing the file. If NULL , then the procedure uses the default directory object for the version. If NULL and no default directory object exists for the version, then the procedure uses the default directory object for the file group. If NULL and no default directory object exists for the version or file group, then the procedure raises an error. |
| version_name | VARCHAR2 | IN | The name of the version to which the file is added. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then the file is added to version 1 of the file group. If NULL , then the procedure uses the version with the latest creation time for the file group. |
| comments | VARCHAR2 | IN | Comments about the file being added |

## Usage Notes

Syntax DBMS_FILE_GROUP.ADD_FILE( file_group_name IN VARCHAR2, file_name IN VARCHAR2, file_type IN VARCHAR2 DEFAULT NULL, file_directory IN VARCHAR2 DEFAULT NULL, version_name IN VARCHAR2 DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 70-3 ADD_FILE Procedure Parameters Parameter Description file_group_name The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. file_name The name of the file being added to the version. Each file name in a version must be unique. file_type The file type. The following are reserved file types: If the file is a datafile, then enter the following: 'DATAFILE' If the file is a Data Pump export dump file, then enter the following: 'DUMPSET' Data Pump metadata is populated when a Data Pump export dump file is imported. If the file is a Data Pump export log file, then enter the following: 'DATAPUMPLOG' If the file type is not one of the reserved file types, then either enter a text description of the file type, or specify NULL to omit a file type description. See " Constants " for more information about the reserved file types. file_directory The name of the directory object that corresponds to the directory containing the file. If NULL , then the procedure uses the default directory object for the version. If NULL and no default directory object exists for the version, then the procedure uses the default directory object for the file group. If NULL and no default directory object exists for the version or file group, then the procedure raises an error. version_name The name of the version to which the file is added. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then the file is added to version 1 of the file group. If NULL , then the procedure uses the version with the latest creation time for the file group. comments Comments about the file being added Usage Notes To run this procedure with either DBMS_FILE_GROUP.EXPORT_DUMP_FILE or 'DUMPSET' specified for the file_type parameter, a user must meet the following requirements: Have the appropriate privileges to import the Data Pump export dump file Have READ privilege on the directory object that contains the Data Pump export dump file See Also: Oracle Database Utilities for more information about Data Pump privileges See Also: Oracle Database Utilities for more information about Data Pump privileges