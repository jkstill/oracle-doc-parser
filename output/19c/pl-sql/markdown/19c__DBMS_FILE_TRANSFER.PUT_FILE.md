---
id: 19c__DBMS_FILE_TRANSFER.PUT_FILE
name: DBMS_FILE_TRANSFER.PUT_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FILE_TRANSFER
tags: [dbms_file_transfer]
source_file: DBMS_FILE_TRANSFER.html
---

# DBMS_FILE_TRANSFER.PUT_FILE

This procedure reads a local file or ASM and contacts a remote database to create a copy of the file in the remote file system.

## Syntax

```sql
DBMS_FILE_TRANSFER.PUT_FILE(
   source_directory_object       IN  VARCHAR2,   
   source_file_name              IN  VARCHAR2,
   destination_directory_object  IN  VARCHAR2,
   destination_file_name         IN  VARCHAR2,  
   destination_database          IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| source_directory_object | VARCHAR2 | IN | The directory object from which the file is copied at the local source site. This directory object must exist at the source site. |
| source_file_name | VARCHAR2 | IN | The name of the file that is copied from the local file system. This file must exist in the local file system in the directory associated with the source directory object. |
| destination_directory_object | VARCHAR2 | IN | The directory object into which the file is placed at the destination site. This directory object must exist in the remote file system. |
| destination_file_name | VARCHAR2 | IN | The name of the file placed in the remote file system. A file with the same name must not exist in the destination directory in the remote file system. |
| destination_database | VARCHAR2) | IN | The name of a database link to the remote database to which the file is copied. |

## Usage Notes

The file that is copied is the source file, and the new file that results from the copy is the destination file. The destination file is not closed until the procedure completes successfully. Syntax DBMS_FILE_TRANSFER.PUT_FILE( source_directory_object IN VARCHAR2, source_file_name IN VARCHAR2, destination_directory_object IN VARCHAR2, destination_file_name IN VARCHAR2, destination_database IN VARCHAR2); Parameters Table 71-4 PUT_FILE Procedure Parameters Parameter Description source_directory_object The directory object from which the file is copied at the local source site. This directory object must exist at the source site. source_file_name The name of the file that is copied from the local file system. This file must exist in the local file system in the directory associated with the source directory object. destination_directory_object The directory object into which the file is placed at the destination site. This directory object must exist in the remote file system. destination_file_name The name of the file placed in the remote file system. A file with the same name must not exist in the destination directory in the remote file system. destination_database The name of a database link to the remote database to which the file is copied. Usage Notes To run this procedure successfully, the following users must have the following privileges: The current user at the local database must have read privilege on the directory object specified in the source_directory_object parameter. The connected user at the destination database must have write privilege to the directory object specified in the destination_directory_object parameter. This procedure converts directory object parameters to uppercase unless they are surrounded by double quotation marks, but this procedure does not convert file names to uppercase. Also, the copied file must meet the following requirements: The size of the copied file must be a multiple of 512 bytes. The size of the copied file must be less than or equal to two terabytes. Transferring the file is not transactional. To monitor the progress of a long file transfer, query the V$SESSION_LONGOPS dynamic performance view. Examples CREATE OR REPLACE DIRECTORY df AS '+datafile' ; GRANT WRITE ON DIRECTORY df TO "user"; CREATE OR REPLACE DIRECTORY ft1 AS '+datafile/ft1' ; GRANT READ,WRITE ON DIRECTORY ft1 TO "user"; CREATE OR REPLACE DIRECTORY ft1_1 AS '+datafile/ft1/ft1_1' ; CONNECT user; Enter password: password -- - put a1.dat to a4.dat (using dbs2 dblink) -- - level 2 sub dir to parent dir -- - user has read privs on ft1_1 at dbs1 and write on df in dbs2 BEGIN DBMS_FILE_TRANSFER.PUT_FILE ( 'ft1_1' , 'a2.dat' , 'df' , 'a4.dat' , 'dbs2' ) ; END ;