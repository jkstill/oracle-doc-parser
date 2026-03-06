---
id: 19c__DBMS_SCHEDULER.DROP_FILE_WATCHER
name: DBMS_SCHEDULER.DROP_FILE_WATCHER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_FILE_WATCHER

This procedure drops one or more file watchers.

## Syntax

```sql
DBMS_SCHEDULER.DROP_FILE_WATCHER (
   file_watcher_name       IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_watcher_name | VARCHAR2 | IN | The file watcher to drop. Can be a comma-separated list of file watchers. Each file watcher name can optionally be prefixed with a schema name. Cannot be NULL . |
| force | BOOLEAN | IN | If set to FALSE , the file watcher must not be referenced by any job, or an error occurs. If set to TRUE , the file watcher is dropped whether or not there are jobs referencing it. In this case, jobs that reference the dropped file watcher are disabled. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_FILE_WATCHER ( file_watcher_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-49 DROP_FILE_WATCHER Procedure Parameters Parameter Description file_watcher_name The file watcher to drop. Can be a comma-separated list of file watchers. Each file watcher name can optionally be prefixed with a schema name. Cannot be NULL . force If set to FALSE , the file watcher must not be referenced by any job, or an error occurs. If set to TRUE , the file watcher is dropped whether or not there are jobs referencing it. In this case, jobs that reference the dropped file watcher are disabled. Usage Notes Only the owner of a file watcher or a user with the CREATE ANY JOB system privilege may drop the file watcher. Running jobs that point to the file watcher are not affected by this procedure and are allowed to continue. See Also: " CREATE_FILE_WATCHER Procedure " See Also: " CREATE_FILE_WATCHER Procedure "