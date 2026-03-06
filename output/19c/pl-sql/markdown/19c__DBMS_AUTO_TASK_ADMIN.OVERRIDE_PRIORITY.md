---
id: 19c__DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY
name: DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_TASK_ADMIN
tags: [dbms_auto_task_admin]
source_file: DBMS_AUTO_TASK_ADMIN.html
---

# DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY

This deprecated procedure is used to manually override task priority.

## Syntax

```sql
DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY (
   client_name       IN    VARCHAR2,
   priority          IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_name | VARCHAR2 | IN | Name of the client, as found in DBA_AUTOTASK_CLIENT View |
| priority | VARCHAR2) | IN | URGENT , HIGH , MEDIUM or LOW |
| operation |  |  | Name of the operation as specified in DBA_AUTOTASK_OPERATION View |
| task_target_type |  |  | Type of target to be affected, as found in V$ AUTOTASK_TARGET_TYPE View |
| task_target_name |  |  | Name of the specific target to be affected |

## Usage Notes

Note: This subprogram is deprecated and becomes nonoperative with Oracle Database 12 c . This can be done at the client, operation or individual task level. This priority assignment is honored during the next maintenance window in which the named client is active. Specifically, setting the priority to URGENT causes a high priority job to be generated at the start of the maintenance window. Setting priority to CLEAR removes the override. Note: This subprogram is deprecated and becomes nonoperative with Oracle Database 12 c . Syntax Override Priority for a Client. DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY ( client_name IN VARCHAR2, priority IN VARCHAR2); Override Priority for an Operation. DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY ( client_name IN VARCHAR2, operation IN VARCHAR2, priority IN VARCHAR2); Override Priority for a Task. DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY ( client_name IN VARCHAR2, operation IN VARCHAR2, task_target_type IN VARCHAR2, task_target_name IN VARCHAR2, priority IN VARCHAR2); Parameters Table 32-7 OVERRIDE_PRIORITY Procedure Parameters Parameter Description client_name Name of the client, as found in DBA_AUTOTASK_CLIENT View priority URGENT , HIGH , MEDIUM or LOW operation Name of the operation as specified in DBA_AUTOTASK_OPERATION View task_target_type Type of target to be affected, as found in V$ AUTOTASK_TARGET_TYPE View task_target_name Name of the specific target to be affected