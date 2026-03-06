---
id: 19c__DBMS_FILE_GROUP.ALTER_FILE
name: DBMS_FILE_GROUP.ALTER_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_GROUP
tags: [dbms_file_group]
source_file: DBMS_FILE_GROUP.html
---

# DBMS_FILE_GROUP.ALTER_FILE

This procedure alters a file in a version of a file group.

## Syntax

```sql
DBMS_FILE_GROUP.ALTER_FILE( 
  file_group_name     IN  VARCHAR2,
  file_name           IN  VARCHAR2,
  version_name        IN  VARCHAR2  DEFAULT NULL,
  new_file_name       IN  VARCHAR2  DEFAULT NULL,
  new_file_directory  IN  VARCHAR2  DEFAULT NULL,
  new_file_type       IN  VARCHAR2  DEFAULT NULL,
  remove_file_type    IN  VARCHAR2  DEFAULT 'N', 
  new_comments        IN  VARCHAR2  DEFAULT NULL,
  remove_comments     IN  VARCHAR2  DEFAULT 'N');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_group_name | VARCHAR2 | IN | The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. |
| file_name | VARCHAR2 | IN | The name of the file being altered in the version |
| version_name | VARCHAR2 | IN | The name of the version that contains the file being altered. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then the file in version 1 of the file group is altered. If NULL , then the procedure uses the version with the latest creation time for the file group. |
| new_file_name | VARCHAR2 | IN | The new name of the file if the file name is being changed. Each file name in a version must be unique. If NULL , then the procedure does not change the file name. Note: When a non- NULL new file name is specified, this procedure changes the metadata for the file name in the data dictionary, but it does not change the file name on the hard disk. |
| new_file_directory | VARCHAR2 | IN | The new name of the directory object that corresponds to the directory containing the file, if the directory object is being changed. If NULL , then the procedure does not change the directory object name. Note: When a non- NULL new file directory is specified, this procedure changes the metadata for the file directory in the data dictionary, but it does not change the file directory on the hard disk. |
| new_file_type | VARCHAR2 | IN | The file type. The following are reserved file types: If the file is a datafile, then enter the following: 'DATAFILE' If the file is a Data Pump export dump file, then enter the following: 'DUMPSET' If the file is a Data Pump export log file, then enter the following: 'DATAPUMPLOG' If the file type is not one of the reserved file types, then enter a text description of the file type. If NULL , then the procedure does not change the file type. See Also: " Constants " for more information about the reserved file types. |
| remove_file_type | VARCHAR2 | IN | If Y , then the procedure removes the file type. If Y and the new_file_type parameter is non- NULL , then the procedure raises an error. If N , then the procedure does not remove the file type. |
| new_comments | VARCHAR2 | IN | New comments about the file being altered. If non- NULL , then the procedure replaces the existing comments with the specified comments. If NULL , then the procedure does not change the existing comments. |
| remove_comments | VARCHAR2 | IN | If Y , then the procedure removes the comments for the file. If Y and the new_comments parameter is non- NULL , then the procedure raises an error. If N , then the procedure does not change the existing comments. |

## Usage Notes

Syntax DBMS_FILE_GROUP.ALTER_FILE( file_group_name IN VARCHAR2, file_name IN VARCHAR2, version_name IN VARCHAR2 DEFAULT NULL, new_file_name IN VARCHAR2 DEFAULT NULL, new_file_directory IN VARCHAR2 DEFAULT NULL, new_file_type IN VARCHAR2 DEFAULT NULL, remove_file_type IN VARCHAR2 DEFAULT 'N', new_comments IN VARCHAR2 DEFAULT NULL, remove_comments IN VARCHAR2 DEFAULT 'N'); Parameters Table 70-4 ALTER_FILE Procedure Parameters Parameter Description file_group_name The name of the file group that contains the version, specified as [schema_name.]file_group_name . For example, if the schema is hq_dba and the file group name is sales_tbs , then specify hq_dba.sales_tbs . If the schema is not specified, then the current user is the default. file_name The name of the file being altered in the version version_name The name of the version that contains the file being altered. If a positive integer is specified as a VARCHAR2 value, then the integer is interpreted as a version number. For example, if '1' is specified, then the file in version 1 of the file group is altered. If NULL , then the procedure uses the version with the latest creation time for the file group. new_file_name The new name of the file if the file name is being changed. Each file name in a version must be unique. If NULL , then the procedure does not change the file name. Note: When a non- NULL new file name is specified, this procedure changes the metadata for the file name in the data dictionary, but it does not change the file name on the hard disk. new_file_directory The new name of the directory object that corresponds to the directory containing the file, if the directory object is being changed. If NULL , then the procedure does not change the directory object name. Note: When a non- NULL new file directory is specified, this procedure changes the metadata for the file directory in the data dictionary, but it does not change the file directory on the hard disk. new_file_type The file type. The following are reserved file types: If the file is a datafile, then enter the following: 'DATAFILE' If the file is a Data Pump export dump file, then enter the following: 'DUMPSET' If the file is a Data Pump export log file, then enter the following: 'DATAPUMPLOG' If the file type is not one of the reserved file types, then enter a text description of the file type. If NULL , then the procedure does not change the file type. See Also: " Constants " for more information about the reserved file types. remove_file_type If Y , then the procedure removes the file type. If Y and the new_file_type parameter is non- NULL , then the procedure raises an error. If N , then the procedure does not remove the file type. new_comments New comments about the file being altered. If non- NULL , then the procedure replaces the existing comments with the specified comments. If NULL , then the procedure does not change the existing comments. remove_comments If Y , then the procedure removes the comments for the file. If Y and the new_comments parameter is non- NULL , then the procedure raises an error. If N , then the procedure does not change the existing comments. Usage Notes If the file type is changed to DBMS_FILE_GROUP.EXPORT_DUMP_FILE or 'DUMPSET' , then Data Pump metadata for the file is populated. If the file type is changed from DBMS_FILE_GROUP.EXPORT_DUMP_FILE or 'DUMPSET' , then Data Pump metadata for the file is purged. To run this procedure with DBMS_FILE_GROUP.EXPORT_DUMP_FILE or 'DUMPSET' specified for the new_file_type parameter, a user must meet the following requirements: Have the appropriate privileges to import the Data Pump export dump file Have READ privilege on the directory object that contains the Data Pump export dump file See Also: Oracle Database Utilities for more information about Data Pump privileges See Also: Oracle Database Utilities for more information about Data Pump privileges