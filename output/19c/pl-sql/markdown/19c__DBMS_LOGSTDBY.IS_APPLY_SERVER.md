---
id: 19c__DBMS_LOGSTDBY.IS_APPLY_SERVER
name: DBMS_LOGSTDBY.IS_APPLY_SERVER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.IS_APPLY_SERVER

This function returns TRUE if it is executed from PL/SQL in the context of a logical standby apply server process.

## Syntax

```sql
DBMS_LOGSTDBY.IS_APPLY_SERVER
RETURN BOOLEAN;
```

**Returns:** `BOOLEAN`

## Usage Notes

This function is used in conjunction with triggers that have the fire_once parameter in the DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY subprogram set to FALSE (the default is TRUE ). Such triggers are executed when the relevant target is updated by an apply process. This function can be used within the body of the trigger to ensure that the trigger takes different (or no) actions on the primary or on the standby. Syntax DBMS_LOGSTDBY.IS_APPLY_SERVER RETURN BOOLEAN;