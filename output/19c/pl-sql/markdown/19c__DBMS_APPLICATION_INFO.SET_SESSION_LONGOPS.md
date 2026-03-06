---
id: 19c__DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS
name: DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLICATION_INFO
tags: [dbms_application_info]
source_file: DBMS_APPLICATION_INFO.html
---

# DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS

This procedure sets a row in the V$SESSION_LONGOPS view. This is a view that is used to indicate the on-going progress of a long running operation. Some Oracle functions, such as parallel execution and Server Managed Recovery, use rows in this view to indicate the status of, for example, a database backup.

## Syntax

```sql
DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS (
   rindex      IN OUT BINARY_INTEGER,
   slno        IN OUT BINARY_INTEGER,
   op_name     IN     VARCHAR2       DEFAULT NULL,
   target      IN     BINARY_INTEGER DEFAULT 0,
   context     IN     BINARY_INTEGER DEFAULT 0,
   sofar       IN     NUMBER         DEFAULT 0,
   totalwork   IN     NUMBER         DEFAULT 0,
   target_desc IN     VARCHAR2       DEFAULT 'unknown target',
   units       IN     VARCHAR2       DEFAULT NULL)  

set_session_longops_nohint constant BINARY_INTEGER := -1;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rindex | BINARY_INTEGER | IN OUT | A token which represents the v$session_longops row to update. Set this to set_session_longops_nohint to start a new row. Use the returned value from the prior call to reuse a row. |
| slno | BINARY_INTEGER | IN OUT | Saves information across calls to set_session_longops : It is for internal use and should not be modified by the caller. |
| op_name | VARCHAR2 | IN | Specifies the name of the long running task. It appears as the OPNAME column of v$session_longops . The maximum length is 64 bytes. |
| target | BINARY_INTEGER | IN | Specifies the object that is being worked on during the long running operation. For example, it could be a table ID that is being sorted. It appears as the TARGET column of v$session_longops . |
| context | BINARY_INTEGER | IN | Any number the client wants to store. It appears in the CONTEXT column of v$session_longops . |
| sofar | NUMBER | IN | Any number the client wants to store. It appears in the SOFAR column of v$session_longops . This is typically the amount of work which has been done so far. |
| totalwork | NUMBER | IN | Any number the client wants to store. It appears in the TOTALWORK column of v$session_longops . This is typically an estimate of the total amount of work needed to be done in this long running operation. |
| target_desc | VARCHAR2 | IN | Specifies the description of the object being manipulated in this long operation. This provides a caption for the target parameter. This value appears in the TARGET_DESC field of v$session_longops . The maximum length is 32 bytes. |
| units | VARCHAR2 | IN | Specifies the units in which sofar and totalwork are being represented. It appears as the UNITS field of v$session_longops . The maximum length is 32 bytes. |

## Usage Notes

Applications may use the SET_SESSION_LONGOPS procedure to advertise information on the progress of application specific long running tasks so that the progress can be monitored by way of the V$SESSION_LONGOPS view. Syntax DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS ( rindex IN OUT BINARY_INTEGER, slno IN OUT BINARY_INTEGER, op_name IN VARCHAR2 DEFAULT NULL, target IN BINARY_INTEGER DEFAULT 0, context IN BINARY_INTEGER DEFAULT 0, sofar IN NUMBER DEFAULT 0, totalwork IN NUMBER DEFAULT 0, target_desc IN VARCHAR2 DEFAULT 'unknown target', units IN VARCHAR2 DEFAULT NULL) set_session_longops_nohint constant BINARY_INTEGER := -1; Parameters Table 20-7 SET_SESSION_LONGOPS Procedure Parameters Parameter Description rindex A token which represents the v$session_longops row to update. Set this to set_session_longops_nohint to start a new row. Use the returned value from the prior call to reuse a row. slno Saves information across calls to set_session_longops : It is for internal use and should not be modified by the caller. op_name Specifies the name of the long running task. It appears as the OPNAME column of v$session_longops . The maximum length is 64 bytes. target Specifies the object that is being worked on during the long running operation. For example, it could be a table ID that is being sorted. It appears as the TARGET column of v$session_longops . context Any number the client wants to store. It appears in the CONTEXT column of v$session_longops . sofar Any number the client wants to store. It appears in the SOFAR column of v$session_longops . This is typically the amount of work which has been done so far. totalwork Any number the client wants to store. It appears in the TOTALWORK column of v$session_longops . This is typically an estimate of the total amount of work needed to be done in this long running operation. target_desc Specifies the description of the object being manipulated in this long operation. This provides a caption for the target parameter. This value appears in the TARGET_DESC field of v$session_longops . The maximum length is 32 bytes. units Specifies the units in which sofar and totalwork are being represented. It appears as the UNITS field of v$session_longops . The maximum length is 32 bytes. Example This example performs a task on 10 objects in a loop. As the example completes each object, Oracle updates V$SESSION_LONGOPS on the procedure's progress. DECLARE rindex BINARY_INTEGER; slno BINARY_INTEGER; totalwork number; sofar number; obj BINARY_INTEGER; BEGIN rindex := dbms_application_info.set_session_longops_nohint; sofar := 0; totalwork := 10; WHILE sofar < 10 LOOP -- update obj based on sofar -- perform task on object target sofar := sofar + 1; dbms_application_info.set_session_longops(rindex, slno, "Operation X", obj, 0, sofar, totalwork, "table", "tables"); END LOOP; END;