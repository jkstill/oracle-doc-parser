---
id: 19c__DBMS_APPLICATION_INFO.SET_ACTION
name: DBMS_APPLICATION_INFO.SET_ACTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLICATION_INFO
tags: [dbms_application_info]
source_file: DBMS_APPLICATION_INFO.html
---

# DBMS_APPLICATION_INFO.SET_ACTION

This procedure sets the name of the current action within the current module.

## Syntax

```sql
DBMS_APPLICATION_INFO.SET_ACTION (
   action_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| action_name | VARCHAR2) | IN | The name of the current action within the current module. When the current action terminates, call this procedure with the name of the next action if there is one, or NULL if there is not. Names longer than 32 bytes are truncated. |

## Usage Notes

Syntax DBMS_APPLICATION_INFO.SET_ACTION ( action_name IN VARCHAR2); Parameters Table 20-4 SET_ACTION Procedure Parameters Parameter Description action_name The name of the current action within the current module. When the current action terminates, call this procedure with the name of the next action if there is one, or NULL if there is not. Names longer than 32 bytes are truncated. Usage Notes The action name should be descriptive text about the current action being performed. You should probably set the action name before the start of every transaction. Set the transaction name to NULL after the transaction completes, so that subsequent transactions are logged correctly. If you do not set the transaction name to NULL , subsequent transactions may be logged with the previous transaction's name. Example The following is an example of a transaction that uses the registration procedure: CREATE OR REPLACE PROCEDURE bal_tran (amt IN NUMBER(7,2)) AS BEGIN -- balance transfer transaction DBMS_APPLICATION_INFO.SET_ACTION( action_name => 'transfer from chk to sav'); UPDATE chk SET bal = bal + :amt WHERE acct# = :acct; UPDATE sav SET bal = bal - :amt WHERE acct# = :acct; COMMIT; DBMS_APPLICATION_INFO.SET_ACTION(null); END;