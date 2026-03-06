---
id: 19c__DBMS_SCHEDULER.CREATE_FILE_WATCHER
name: DBMS_SCHEDULER.CREATE_FILE_WATCHER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_FILE_WATCHER

This procedure creates a file watcher, which is a Scheduler object that defines the location, name, and other properties of a file whose arrival on a system causes the Scheduler to start a job. After you create a file watcher, you reference it in an event-based job or event schedule.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_FILE_WATCHER (
   file_watcher_name            IN VARCHAR2,
   directory_path               IN VARCHAR2,
   file_name                    IN VARCHAR2,
   credential_name              IN VARCHAR2,
   destination                  IN VARCHAR2  DEFAULT NULL,
   min_file_size                IN PLS_INTEGER DEFAULT 0,
   steady_state_duration        IN INTERVAL DAY TO SECOND DEFAULT NULL,
   comments                     IN VARCHAR2 DEFAULT NULL,
   enabled                      IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_watcher_name | VARCHAR2 | IN | The name to assign to the file watcher. The name must be unique in the SQL namespace. For example, a file watcher cannot have the same name as a table in a schema. This can optionally be prefixed with a schema name. Cannot be NULL . |
| directory_path | VARCHAR2 | IN | Directory in which the file is expected to arrive. The single wildcard '?' at the beginning of the path denotes the Oracle home path. For example, '?/rdbms/log' denotes the rdbms/log subdirectory of the Oracle home directory. |
| file_name | VARCHAR2 | IN | Name of the file to look for. Two wildcards are permitted anywhere in the file name: '?' denotes any single character, and '*' denotes zero or more characters. This attribute cannot be NULL . |
| credential_name | VARCHAR2 | IN | Name of a valid credential object. The file watcher uses the credential to authenticate itself with the host operating system to access the watched-for file. The file watcher owner must have EXECUTE privileges on the credential. Cannot be NULL . |
| destination | VARCHAR2 | IN | Name of an external destination. You create an external destination by registering a remote Scheduler agent with the database. See the view ALL_SCHEDULER_EXTERNAL_DESTS for valid external destination names. If this parameter is NULL , the file watcher is created on the local host. |
| min_file_size | PLS_INTEGER | IN | Minimum size in bytes that the file must be before the file watcher considers the file found. Default is 0. |
| steady_state_duration | INTERVAL | IN | Minimum time interval that the file must remain unchanged before the file watcher considers the file found. Cannot exceed one hour. If NULL , an internal value is used. The minimum value is 10 seconds. Oracle recommends similar steady_state_duration values for all file watchers for efficient file watcher job operation. Also, the repeat interval of the file watcher schedule must be equal or greater than the steady_state_duration value. |
| comments | VARCHAR2 | IN | Optional comment. |
| enabled | BOOLEAN | IN | If TRUE (the default), the file watcher is enabled. |

## Usage Notes

Syntax DBMS_SCHEDULER.CREATE_FILE_WATCHER ( file_watcher_name IN VARCHAR2, directory_path IN VARCHAR2, file_name IN VARCHAR2, credential_name IN VARCHAR2, destination IN VARCHAR2 DEFAULT NULL, min_file_size IN PLS_INTEGER DEFAULT 0, steady_state_duration IN INTERVAL DAY TO SECOND DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL, enabled IN BOOLEAN DEFAULT TRUE); Parameters Table 151-25 CREATE_FILE_WATCHER Parameters Parameter Description file_watcher_name The name to assign to the file watcher. The name must be unique in the SQL namespace. For example, a file watcher cannot have the same name as a table in a schema. This can optionally be prefixed with a schema name. Cannot be NULL . directory_path Directory in which the file is expected to arrive. The single wildcard '?' at the beginning of the path denotes the Oracle home path. For example, '?/rdbms/log' denotes the rdbms/log subdirectory of the Oracle home directory. file_name Name of the file to look for. Two wildcards are permitted anywhere in the file name: '?' denotes any single character, and '*' denotes zero or more characters. This attribute cannot be NULL . credential_name Name of a valid credential object. The file watcher uses the credential to authenticate itself with the host operating system to access the watched-for file. The file watcher owner must have EXECUTE privileges on the credential. Cannot be NULL . destination Name of an external destination. You create an external destination by registering a remote Scheduler agent with the database. See the view ALL_SCHEDULER_EXTERNAL_DESTS for valid external destination names. If this parameter is NULL , the file watcher is created on the local host. min_file_size Minimum size in bytes that the file must be before the file watcher considers the file found. Default is 0. steady_state_duration Minimum time interval that the file must remain unchanged before the file watcher considers the file found. Cannot exceed one hour. If NULL , an internal value is used. The minimum value is 10 seconds. Oracle recommends similar steady_state_duration values for all file watchers for efficient file watcher job operation. Also, the repeat interval of the file watcher schedule must be equal or greater than the steady_state_duration value. comments Optional comment. enabled If TRUE (the default), the file watcher is enabled. Usage Notes You must have the CREATE JOB system privilege to create a file watcher in your own schema. You require the CREATE ANY JOB system privilege to create a file watcher in a schema different from your own (except the SYS schema, which is disallowed).