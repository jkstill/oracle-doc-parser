---
id: 19c__DBMS_AUTO_TASK_ADMIN.ENABLE
name: DBMS_AUTO_TASK_ADMIN.ENABLE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_TASK_ADMIN
tags: [dbms_auto_task_admin]
source_file: DBMS_AUTO_TASK_ADMIN.html
---

# DBMS_AUTO_TASK_ADMIN.ENABLE

This procedure allows a previously disabled client, operation, target type, or individual target to be enabled under AUTOTASK control.

## Syntax

```sql
DBMS_AUTO_TASK_ADMIN.ENABLE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_name |  |  | Name of the client, as found in DBA_AUTOTASK_CLIENT View |
| operation |  |  | Name of the operation as specified in DBA_AUTOTASK_OPERATION View |
| window_name |  |  | Optional name of the window in which client is to be enabled |

## Usage Notes

Specifying the DEFERRED option postpones the effect of the call until the start of the next maintenance window. If IMMEDIATE option is specified the effect of this call is immediate – as long as there is a currently open maintenance window. Syntax Re-enabling AUTOTASK . This version enables the specified client. Note that any explicitly disabled tasks or operations must be re-enabled individually. DBMS_AUTO_TASK_ADMIN.ENABLE; Re-enabling a client or operation.Note that any explicitly disabled tasks or operations must be re-enabled individually. DBMS_AUTO_TASK_ADMIN.ENABLE ( client_name IN VARCHAR2, operation IN VARCHAR2, window_name IN VARCHAR2); Parameters Table 32-4 ENABLE Procedure Parameters Parameter Description client_name Name of the client, as found in DBA_AUTOTASK_CLIENT View operation Name of the operation as specified in DBA_AUTOTASK_OPERATION View window_name Optional name of the window in which client is to be enabled Usage Notes If operation and window_name are both NULL , the client is enabled. If operation is not NULL , window_name is ignored and the specified operation is enabled If operation is NULL and window_name is not NULL , the client is enabled in the specified window.