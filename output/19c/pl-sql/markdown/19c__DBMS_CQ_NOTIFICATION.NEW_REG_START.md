---
id: 19c__DBMS_CQ_NOTIFICATION.NEW_REG_START
name: DBMS_CQ_NOTIFICATION.NEW_REG_START
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CQ_NOTIFICATION
tags: [dbms_cq_notification]
source_file: DBMS_CQ_NOTIFICATION.html
---

# DBMS_CQ_NOTIFICATION.NEW_REG_START

This procedure begins a new registration block.

## Syntax

```sql
DBMS_CQ_NOTIFICATION.NEW_REG_START (  
  regds IN sys.chnf$_reg_info)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sys.chnf$_reg_info |  |  | Registration descriptor describing the notification handler and other properties of the registration |

**Returns:** `NUMBER`

## Usage Notes

Any objects referenced by queries executed within the registration block are considered interesting objects and added to the registration. The registration block ends upon calling the REG_END procedure. Syntax DBMS_CQ_NOTIFICATION.NEW_REG_START ( regds IN sys.chnf$_reg_info) RETURN NUMBER; Parameters Table 40-10 NEW_REG_START Function Parameters Parameter Description sys.chnf$_reg_info Registration descriptor describing the notification handler and other properties of the registration Return Values The procedure returns a registration-id which is a unique integer assigned by the database to this registration. The registration-id will be echoed back in every notification received for this registration. Usage Notes The only operations permitted inside a registration block are queries (the ones the user wishes to register). DML and DDL operations are not permitted. The registration block is a session property and implicitly terminates upon exiting the session. While the registration block is a session property, the registration itself is a persistent database entity. Once created, the registration survives until explicitly deregistered by the client application or timed-out or removed by the database for some other reason (such as loss of privileges). The user must have the CHANGE NOTIFICATION system privilege and SELECT or READ privileges on any objects to be registered. The SYS user will not be permitted to create new registrations. Nesting of registration block is not permitted.