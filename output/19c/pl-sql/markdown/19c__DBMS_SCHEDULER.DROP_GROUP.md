---
id: 19c__DBMS_SCHEDULER.DROP_GROUP
name: DBMS_SCHEDULER.DROP_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_GROUP

This procedure drops one or more groups.

## Syntax

```sql
DBMS_SCHEDULER.DROP_GROUP (
   group_name       IN VARCHAR2,
   force            IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| group_name | VARCHAR2 | IN | A group to drop. Can be a comma-separated list of group names. Each group name can optionally be prefixed with a schema name. The procedure stops processing if it encounters a group that does not exist. All groups processed before the error are dropped. Cannot be NULL . |
| force | BOOLEAN | IN | If FALSE , the group must not be referenced by any job, otherwise an error occurs. If TRUE , the group is dropped whether or not there are jobs referencing it. In this case, all jobs referencing the group are disabled and all job instances that reference the group are removed from the *_SCHEDULER_JOB_DESTS views. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_GROUP ( group_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-50 DROP_GROUP Procedure Parameters Parameter Description group_name A group to drop. Can be a comma-separated list of group names. Each group name can optionally be prefixed with a schema name. The procedure stops processing if it encounters a group that does not exist. All groups processed before the error are dropped. Cannot be NULL . force If FALSE , the group must not be referenced by any job, otherwise an error occurs. If TRUE , the group is dropped whether or not there are jobs referencing it. In this case, all jobs referencing the group are disabled and all job instances that reference the group are removed from the *_SCHEDULER_JOB_DESTS views. Usage Notes Only the owner or a user with the CREATE ANY JOB system privilege may drop a group. You must have the MANAGE SCHEDULER privilege to drop a group of type WINDOW . See Also: " CREATE_FILE_WATCHER Procedure " See Also: " CREATE_FILE_WATCHER Procedure "