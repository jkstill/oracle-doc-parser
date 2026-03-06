---
id: 19c__DBMS_FILE_TRANSFER.COPY_FILE
name: DBMS_FILE_TRANSFER.COPY_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_TRANSFER
tags: [dbms_file_transfer]
source_file: DBMS_FILE_TRANSFER.html
---

# DBMS_FILE_TRANSFER.COPY_FILE

This procedure reads a file from a source directory and creates a copy of it in a destination directory. The source and destination directories can both be in a local file system, or both be in an Automatic Storage Management (ASM) disk group, or between local file system and ASM with copying in either direction.

## Syntax

```sql
DBMS_FILE_TRANSFER.COPY_FILE(
   source_directory_object       IN  VARCHAR2,
   source_file_name              IN  VARCHAR2,
   destination_directory_object  IN  VARCHAR2,
   destination_file_name         IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| source_directory_object | VARCHAR2 | IN | The directory object that designates the source directory. The directory object must already exist. (You create directory objects with the CREATE DIRECTORY command). |
| source_file_name | VARCHAR2 | IN | The name of the file to copy. This file must exist in the source directory. |
| destination_directory_object | VARCHAR2 | IN | The directory object that designates the destination directory. The directory object must already exist. If the destination is ASM, the directory object must designate either a disk group name (for example, + diskgroup1 ) or a directory created for alias names. In the case of a directory, the full path to the directory must be specified (for example: +diskgroup1/dbs/control ). |
| destination_file_name | VARCHAR2) | IN | The name to assign to the file in the destination directory. A file with the same name must not exist in the destination directory. If the destination is ASM: The file is given a fully qualified ASM filename and created in the appropriate directory (depending on the database name and file type) The file type tag assigned to the file is COPY_FILE The value of the destination_file_name argument becomes the file's alias name in the designated destination directory The file name can be followed by an ASM template name in parentheses. The file is then given the attributes specified by the template. |

## Usage Notes

You can copy any type of file to and from a local file system. However, you can copy only database files (such as datafiles, tempfiles, controlfiles, and so on) to and from an ASM disk group. The destination file is not closed until the procedure completes successfully. Syntax DBMS_FILE_TRANSFER.COPY_FILE( source_directory_object IN VARCHAR2, source_file_name IN VARCHAR2, destination_directory_object IN VARCHAR2, destination_file_name IN VARCHAR2); Parameters Table 71-2 COPY_FILE Procedure Parameters Parameter Description source_directory_object The directory object that designates the source directory. The directory object must already exist. (You create directory objects with the CREATE DIRECTORY command). source_file_name The name of the file to copy. This file must exist in the source directory. destination_directory_object The directory object that designates the destination directory. The directory object must already exist. If the destination is ASM, the directory object must designate either a disk group name (for example, + diskgroup1 ) or a directory created for alias names. In the case of a directory, the full path to the directory must be specified (for example: +diskgroup1/dbs/control ). destination_file_name The name to assign to the file in the destination directory. A file with the same name must not exist in the destination directory. If the destination is ASM: The file is given a fully qualified ASM filename and created in the appropriate directory (depending on the database name and file type) The file type tag assigned to the file is COPY_FILE The value of the destination_file_name argument becomes the file's alias name in the designated destination directory The file name can be followed by an ASM template name in parentheses. The file is then given the attributes specified by the template. Usage Notes To run this procedure successfully, the current user must have the following privileges: READ privilege on the directory object specified in the source_directory_object parameter WRITE privilege on directory object specified in the destination_directory_object parameter This procedure converts directory object parameters to uppercase unless they are surrounded by double quotation marks, but this procedure does not convert file names to uppercase. Also, the copied file must meet the following requirements: The size of the copied file must be a multiple of 512 bytes. The size of the copied file must be less than or equal to two terabytes. The source_file_name parameter must specify a file that is in the directory specified by the source_directory_object parameter before running the procedure, and the destination_file_name parameter must specify the new name of the file in the new location specified in the destination_directory_object parameter. Relative paths and symbolic links are not allowed in the directory objects for the source_directory_object and destination_directory_object parameters. Transferring the file is not transactional. To monitor the progress of a long file copy, query the V$SESSION_LONGOPS dynamic performance view. See Also: Oracle Automatic Storage Management Administrator's Guide for instructions about using file transfer See Also: Oracle Automatic Storage Management Administrator's Guide for instructions about using file transfer