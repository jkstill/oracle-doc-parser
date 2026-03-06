---
id: 19c__DBMS_SCHEDULER.GET_FILE
name: DBMS_SCHEDULER.GET_FILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.GET_FILE

This procedure retrieves a file from the operating system file system of a specified host. The file is copied to a destination, or its contents are returned in a procedure output parameter.

## Syntax

```sql
DBMS_SCHEDULER.GET_FILE (
   source_file                  IN VARCHAR2,
   source_host                  IN VARCHAR2,
   credential_name              IN VARCHAR2,
   file_contents                IN OUT NOCOPY {BLOB|CLOB});
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| source_file | VARCHAR2 | IN | Fully qualified path name of the file to retrieve from the operating system. The file name is case-sensitive and is not converted to uppercase. If the file name starts with a question mark (' ? '), the question mark is replaced by the path to the Oracle home if getting a file from the local host, or to the Scheduler agent home if getting a file from a remote host. If the format of this parameter is external_log_id _stdout , then the stdout from the designated external job run is returned. If the format of this parameter is external_log_id _stderr , the error text from the designated external job run is returned. You obtain the value of external_log_id from the ADDITIONAL_INFO column of the *_SCHEDULER_JOB_RUN_DETAILS views. This column contains a set of name/value pairs in an indeterminate order, so you must parse this column for the external_log_id name/value pair, and then append either " _stdout " or " _stderr " to its value. The external job must have an associated credential. The credential_name parameter of GET_FILE must name the same credential that is used by the job, and the source_host parameter must be the same as the destination attribute of the job. |
| source_host | VARCHAR2 | IN | If the file is to be retrieved from a remote host, then this parameter must be a valid an external destination name. (An external destination is created when you register a remote Scheduler agent with the database. You can view external destination names in the views *_SCHEDULER_EXTERNAL_DESTS .) If source_host is NULL or set to ' localhost ', then the file is retrieved from the file system of the local host. To determine the port number of a Scheduler agent, view the schagent.conf file, which is located in the Scheduler agent home directory on the remote host. |
| credential_name | VARCHAR2 | IN | The name of the credential to use for accessing the file system. |
| file_contents | NOCOPY | IN OUT | The variable into which the file contents is read. |
| destination_file_name |  |  | The file to which the file contents is written. |
| destination_directory_object |  |  | The directory object that specifies the path to the destination file, when destination_file_name is used. The caller must have the necessary privileges on the directory object. |
| destination_permissions |  |  | Reserved for future use |

## Usage Notes

You can also use this procedure to retrieve the standard output or error text for a run of an external job that has an associated credential. This procedures differs from the equivalent UTL_FILE procedure in that it uses a credential and can retrieve files from remote hosts that have only a Scheduler agent (and not an Oracle database) installed. Syntax DBMS_SCHEDULER.GET_FILE ( source_file IN VARCHAR2, source_host IN VARCHAR2, credential_name IN VARCHAR2, file_contents IN OUT NOCOPY {BLOB|CLOB}); DBMS_SCHEDULER.GET_FILE ( source_file IN VARCHAR2, source_host IN VARCHAR2, credential_name IN VARCHAR2, destination_file_name IN VARCHAR2, destination_directory_object IN VARCHAR2, destination_permissions IN VARCHAR2 DEFAULT NULL); Parameters Table 151-67 GET_FILE Procedure Parameters Parameter Description source_file Fully qualified path name of the file to retrieve from the operating system. The file name is case-sensitive and is not converted to uppercase. If the file name starts with a question mark (' ? '), the question mark is replaced by the path to the Oracle home if getting a file from the local host, or to the Scheduler agent home if getting a file from a remote host. If the format of this parameter is external_log_id _stdout , then the stdout from the designated external job run is returned. If the format of this parameter is external_log_id _stderr , the error text from the designated external job run is returned. You obtain the value of external_log_id from the ADDITIONAL_INFO column of the *_SCHEDULER_JOB_RUN_DETAILS views. This column contains a set of name/value pairs in an indeterminate order, so you must parse this column for the external_log_id name/value pair, and then append either " _stdout " or " _stderr " to its value. The external job must have an associated credential. The credential_name parameter of GET_FILE must name the same credential that is used by the job, and the source_host parameter must be the same as the destination attribute of the job. source_host If the file is to be retrieved from a remote host, then this parameter must be a valid an external destination name. (An external destination is created when you register a remote Scheduler agent with the database. You can view external destination names in the views *_SCHEDULER_EXTERNAL_DESTS .) If source_host is NULL or set to ' localhost ', then the file is retrieved from the file system of the local host. To determine the port number of a Scheduler agent, view the schagent.conf file, which is located in the Scheduler agent home directory on the remote host. credential_name The name of the credential to use for accessing the file system. file_contents The variable into which the file contents is read. destination_file_name The file to which the file contents is written. destination_directory_object The directory object that specifies the path to the destination file, when destination_file_name is used. The caller must have the necessary privileges on the directory object. destination_permissions Reserved for future use Usage Notes The caller must have the CREATE EXTERNAL JOB system privilege and have EXECUTE privileges on the credential.