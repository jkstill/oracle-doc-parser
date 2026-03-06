---
id: 19c__DBMS_FILE_TRANSFER.GET_FILE
name: DBMS_FILE_TRANSFER.GET_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_TRANSFER
tags: [dbms_file_transfer]
source_file: DBMS_FILE_TRANSFER.html
---

# DBMS_FILE_TRANSFER.GET_FILE

This procedure contacts a remote database to read a remote file and then creates a copy of the file in the local file system or ASM. The file that is copied is the source file, and the new file that results from the copy is the destination file. The destination file is not closed until the procedure completes successfully.

## Syntax

```sql
DBMS_FILE_TRANSFER.GET_FILE
   source_directory_object      IN  VARCHAR2,    
   source_file_name             IN  VARCHAR2,  
   source_database              IN  VARCHAR2,  
   destination_directory_object IN  VARCHAR2,
   destination_file_name        IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| source_directory_object | VARCHAR2 | IN | The directory object from which the file is copied at the source site. This directory object must exist at the source site. |
| source_file_name | VARCHAR2 | IN | The name of the file that is copied in the remote file system. This file must exist in the remote file system in the directory associated with the source directory object. |
| source_database | VARCHAR2 | IN | The name of a database link to the remote database where the file is located. |
| destination_directory_object | VARCHAR2 | IN | The directory object into which the file is placed at the destination site. This directory object must exist in the local file system. |
| destination_file_name | VARCHAR2) | IN | The name of the file copied to the local file system. A file with the same name must not exist in the destination directory in the local file system. |

## Usage Notes

Syntax DBMS_FILE_TRANSFER.GET_FILE source_directory_object IN VARCHAR2, source_file_name IN VARCHAR2, source_database IN VARCHAR2, destination_directory_object IN VARCHAR2, destination_file_name IN VARCHAR2); Parameters Table 71-3 GET_FILE Procedure Parameters Parameter Description source_directory_object The directory object from which the file is copied at the source site. This directory object must exist at the source site. source_file_name The name of the file that is copied in the remote file system. This file must exist in the remote file system in the directory associated with the source directory object. source_database The name of a database link to the remote database where the file is located. destination_directory_object The directory object into which the file is placed at the destination site. This directory object must exist in the local file system. destination_file_name The name of the file copied to the local file system. A file with the same name must not exist in the destination directory in the local file system. Usage Notes To run this procedure successfully, the following users must have the following privileges: The connected user at the source database must have read privilege on the directory object specified in the source_directory_object parameter. The current user at the local database must have write privilege on the directory object specified in the destination_directory_object parameter. This procedure converts directory object parameters to uppercase unless they are surrounded by double quotation marks, but this procedure does not convert file names to uppercase. Also, the copied file must meet the following requirements: The size of the copied file must be a multiple of 512 bytes. The size of the copied file must be less than or equal to two terabytes. Transferring the file is not transactional. To monitor the progress of a long file transfer, query the V$SESSION_LONGOPS dynamic performance view. Examples CREATE OR REPLACE DIRECTORY df AS '+datafile' ; GRANT WRITE ON DIRECTORY df TO "user"; CREATE DIRECTORY DSK_FILES AS ''^t_work^''; GRANT WRITE ON DIRECTORY dsk_files TO "user"; -- asumes that dbs2 link has been created and we are connected to the instance. -- dbs2 could be a loopback or point to another instance. BEGIN -- asm file to an os file -- get an asm file from dbs1.asm/a1 to dbs2.^t_work^/oa5.dat DBMS_FILE_TRANSFER.GET_FILE ( 'df' , 'a1' , 'dbs1', 'dsk_files' , 'oa5.dat' ); -- os file to an os file -- get an os file from dbs1.^t_work^/a2.dat to dbs2.^t_work^/a2back.dat DBMS_FILE_TRANSFER.GET_FILE ( 'dsk_files' , 'a2.dat' , 'dbs1', 'dsk_files' , 'a2back.dat' ); END ; /