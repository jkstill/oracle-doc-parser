---
id: 19c__DBMS_SCHEDULER.DROP_DATABASE_DESTINATION
name: DBMS_SCHEDULER.DROP_DATABASE_DESTINATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_DATABASE_DESTINATION

This procedure drops one or more database destinations.

## Syntax

```sql
DBMS_SCHEDULER.DROP_DATABASE_DESTINATION (
   destination_name        IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| destination_name | VARCHAR2) | IN | The name of the destination to drop. Can be a comma-separated list of database destinations to drop. Each database destination can optionally be prefixed with a schema name. The procedure stops processing if it encounters a database destination that does not exist. All database destinations processed before the error are dropped. Cannot be NULL . |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_DATABASE_DESTINATION ( destination_name IN VARCHAR2); Parameters Table 151-48 DROP_DATABASE_DESTINATION Procedure Parameters Parameter Description destination_name The name of the destination to drop. Can be a comma-separated list of database destinations to drop. Each database destination can optionally be prefixed with a schema name. The procedure stops processing if it encounters a database destination that does not exist. All database destinations processed before the error are dropped. Cannot be NULL . Usage Notes Only the owner or a user with the CREATE ANY JOB system privilege may drop the database destination. When a database destination is dropped: All job instances that refer to the destination in the *_SCHEDULER_JOB_DESTS views are also dropped. Jobs running against the destination are stopped. Members of database destination groups that refer to the destination are removed from the group. See Also: CREATE_DATABASE_DESTINATION Procedure See Also: CREATE_DATABASE_DESTINATION Procedure