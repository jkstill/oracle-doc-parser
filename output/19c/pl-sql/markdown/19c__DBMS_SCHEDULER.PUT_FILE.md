---
id: 19c__DBMS_SCHEDULER.PUT_FILE
name: DBMS_SCHEDULER.PUT_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.PUT_FILE

This procedure saves a file to the operating system file system of a specified remote host or of the local computer.

## Syntax

```sql
DBMS_SCHEDULER.PUT_FILE (
   destination_file         IN VARCHAR2,
   destination_host         IN VARCHAR2,
   credential_name          IN VARCHAR2,
   file_contents            IN {BLOB|CLOB},
   destination_permissions  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| destination_file | VARCHAR2 | IN | Fully qualified path name of the file to save to the operating system file system. The file name is case-sensitive. If the file name starts with a question mark (' ? '), the question mark is replaced by the path to the Oracle home if saving to the local host, or to the Scheduler agent home if saving to a remote host. |
| destination_host | VARCHAR2 | IN | If NULL or set to ' localhost ', the file is saved to the file system of the local computer. To save to a remote host, this parameter must be a valid external destination name. (An external destination is created when you register a remote Scheduler agent with the database. You can view external destination names in the views *_SCHEDULER_EXTERNAL_DESTS .) |
| credential_name | VARCHAR2 | IN | The name of the credential to use for accessing the destination file system. |
| file_contents | IN | IN | The variable from which the file contents is read. |
| source_file_name |  |  | The file from which the file contents is written |
| source_directory_object |  |  | The directory object that specifies the path to the source file, when source_file_name is used. The caller must have the necessary privileges on the directory object. |
| destination_permissions | VARCHAR2 | IN | Reserved for future use |

## Usage Notes

It differs from the equivalent UTL_FILE procedure in that it uses a credential and can save files to a remote host that has only a Scheduler agent (and not an Oracle Database) installed. Syntax DBMS_SCHEDULER.PUT_FILE ( destination_file IN VARCHAR2, destination_host IN VARCHAR2, credential_name IN VARCHAR2, file_contents IN {BLOB|CLOB}, destination_permissions IN VARCHAR2 DEFAULT NULL); DBMS_SCHEDULER.PUT_FILE ( destination_file IN VARCHAR2, destination_host IN VARCHAR2, credential_name IN VARCHAR2, source_file_name IN VARCHAR2, source_directory_object IN VARCHAR2, destination_permissions IN VARCHAR2 DEFAULT NULL); Parameters Table 151-72 PUT_FILE Procedure Parameters Parameter Description destination_file Fully qualified path name of the file to save to the operating system file system. The file name is case-sensitive. If the file name starts with a question mark (' ? '), the question mark is replaced by the path to the Oracle home if saving to the local host, or to the Scheduler agent home if saving to a remote host. destination_host If NULL or set to ' localhost ', the file is saved to the file system of the local computer. To save to a remote host, this parameter must be a valid external destination name. (An external destination is created when you register a remote Scheduler agent with the database. You can view external destination names in the views *_SCHEDULER_EXTERNAL_DESTS .) credential_name The name of the credential to use for accessing the destination file system. file_contents The variable from which the file contents is read. source_file_name The file from which the file contents is written source_directory_object The directory object that specifies the path to the source file, when source_file_name is used. The caller must have the necessary privileges on the directory object. destination_permissions Reserved for future use Usage Notes The caller must have the CREATE EXTERNAL JOB system privilege and have EXECUTE privileges on the credential.