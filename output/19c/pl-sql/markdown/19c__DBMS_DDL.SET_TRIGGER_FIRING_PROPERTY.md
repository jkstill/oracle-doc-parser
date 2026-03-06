---
id: 19c__DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY
name: DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DDL
tags: [dbms_ddl]
source_file: DBMS_DDL.html
---

# DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY

This procedure sets the specified DML or DDL trigger's firing property whether or not the property is set for the trigger.

## Syntax

```sql
DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY (
   trig_owner         IN  VARCHAR2,
   trig_name          IN  VARCHAR2,
   fire_once          IN  BOOLEAN);

DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY (
   trig_owner         IN  VARCHAR2,
   trig_name          IN  VARCHAR2,
   property           IN INTEGER,
   setting            IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| trig_owner | VARCHAR2 | IN | Schema of the trigger to set |
| trig_name | VARCHAR2 | IN | Name of the trigger to set |
| fire_once | BOOLEAN) | IN | If TRUE , the trigger is set to fire once. By default, the fire_once parameter is set to TRUE for DML and DDL triggers. If FALSE , the trigger is set to always fire unless apply_server_only property is set to TRUE , which overrides fire_once property setting. |
| property | INTEGER | IN | DBMS_DDL . fire_once to set the fire_once property of the trigger DBMS_DDL . apply_server_only to indicate whether trigger fires only in the context of SQL apply processes maintaining a logical standby database or Streams apply processes |
| setting | BOOLEAN) | IN | Value of property being set |

## Usage Notes

Use this procedure to control a DML or DDL trigger's firing property for changes: Applied by a Streams apply process Made by executing one or more Streams apply errors using the EXECUTE_ERROR or EXECUTE_ALL_ERRORS procedure in the DBMS_APPLY_ADM package. Applied by a Logical Standby apply process Syntax DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY ( trig_owner IN VARCHAR2, trig_name IN VARCHAR2, fire_once IN BOOLEAN); DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY ( trig_owner IN VARCHAR2, trig_name IN VARCHAR2, property IN INTEGER, setting IN BOOLEAN); Parameters Table 56-8 SET_TRIGGER_FIRING_PROPERTY Procedure Parameters Parameter Description trig_owner Schema of the trigger to set trig_name Name of the trigger to set fire_once If TRUE , the trigger is set to fire once. By default, the fire_once parameter is set to TRUE for DML and DDL triggers. If FALSE , the trigger is set to always fire unless apply_server_only property is set to TRUE , which overrides fire_once property setting. property DBMS_DDL . fire_once to set the fire_once property of the trigger DBMS_DDL . apply_server_only to indicate whether trigger fires only in the context of SQL apply processes maintaining a logical standby database or Streams apply processes setting Value of property being set Usage Notes DML triggers created on a table have their fire-once property set to TRUE . In this case, the triggers only fire when the table is modified by an user process, and they are automatically disabled inside Oracle processes maintaining either a logical standby database (SQL Apply) or Oracle processes doing replication (Streams Apply) processes, and thus do not fire when a SQL Apply or a Streams Apply process modifies the table. There are two ways for a user to fire a trigger as a result of SQL Apply or a Streams Apply process making a change to a maintained table: (a) setting the fire-once property of a trigger to FALSE , which allows it fire both in the context of a user process or a SQL or Streams Apply process, or (b) by setting the apply-server-only property to TRUE and thus making the trigger fire only in the context of a SQL Apply or a Streams Apply process and not in the context of a user process. FIRE_ONCE = TRUE , APPLY_SERVER_ONLY = FALSE This is the default property setting for a DML trigger. The trigger only fires when user process modifies the base table. FIRE_ONCE = TRUE or FALSE , APPLY_SERVER_ONLY = TRUE The trigger only fires when SQL Apply or Streams Apply process modifies the base table. The trigger does not fire when a user process modifies the base table.Thus the apply-server-only property overrides the fire-once property of a trigger. Note: If you dequeue an error transaction from the error queue and execute it without using the DBMS_APPLY_ADM package, then relevant changes resulting from this execution cause a trigger to fire, regardless of the trigger firing property. Only DML and DDL triggers can be fire once. All other types of triggers always fire. Note: If you dequeue an error transaction from the error queue and execute it without using the DBMS_APPLY_ADM package, then relevant changes resulting from this execution cause a trigger to fire, regardless of the trigger firing property. Only DML and DDL triggers can be fire once. All other types of triggers always fire.