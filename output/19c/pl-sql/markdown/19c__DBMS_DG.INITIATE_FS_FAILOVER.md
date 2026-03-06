---
id: 19c__DBMS_DG.INITIATE_FS_FAILOVER
name: DBMS_DG.INITIATE_FS_FAILOVER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DG
tags: [dbms_dg]
source_file: DBMS_DG.html
---

# DBMS_DG.INITIATE_FS_FAILOVER

Use this procedure to specify a condition string that, when encountered by an application, allows the application to request that a fast-start failover be invoked.

## Syntax

```sql
DBMS_DG.INITIATE_FS_FAILOVER (
     condstr          IN VARCHAR2)
RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| condstr | VARCHAR2) | IN | Specifies the condition string for which a fast-start failover should be requested. If no condition string argument is supplied, the default string of "Application Failover Requested" will be logged in the broker log file and in the database alert log of the database on which the procedure was called. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DG.INITIATE_FS_FAILOVER ( condstr IN VARCHAR2) RETURN BINARY_INTEGER; Parameters Table 61-2 INITIATE_FS_FAILOVER Procedure Parameters Parameter Description condstr Specifies the condition string for which a fast-start failover should be requested. If no condition string argument is supplied, the default string of "Application Failover Requested" will be logged in the broker log file and in the database alert log of the database on which the procedure was called. Usage Notes This procedure returns a binary integer. Query the V$FS_FAILOVER_STATS view to see the time of the last fast-start failover and the reason it was performed. This procedure can only be called while connected to a primary database or a fast-start failover standby database. Errors Table 61-3 INITIATE_FS_FAILOVER Procedure Errors Error Description ORA-00000: normal, successful completion The request to initiate a fast-start failover has been posted to the observer. ORA-16646: fast-start failover is disabled Either a broker configuration does not exist or fast-start failover has not been enabled. ORA-16666: unable to initiate fast-start failover on a bystander standby database DBMS_DG.INITIATE_FS_FAILOVER was invoked on a bystander standby database. That is, it was not invoked on the primary or on the fast-start failover target standby database. ORA-16817: unsynchronized fast-start failover configuration DBMS_DG.INITIATE_FS_FAILOVER was invoked in a maximum available fast-start failover configuration when the configuration was not synchronized. ORA-16819: fast-start failover observer not started DBMS_DG.INITIATE_FS_FAILOVER was invoked but an observer had not yet been started. ORA-16820: fast-start failover observer is no longer observing this database DBMS_DG.INITIATE_FS_FAILOVER was invoked but the configuration detects that the observer may not be running. ORA-16829: lagging fast-start failover configuration DBMS_DG.INITIATE_FS_FAILOVER was invoked in a maximum performance fast-start failover configuration when the configuration was not in the user-specified redo lag limit. Example In this example, the program attempts to initiate a fast-start failover when fast-start failover is disabled. To use this example, connect as user SYS with SYDDBA privileges. set serveroutput on declare status integer; begin status := dbms_dg.initiate_fs_failover(''Failover Requested''); dbms_output.put_line(''Fast-Start Failover is disabled: Expected status = ORA-16646''); dbms_output.put_line('' Actual Status = ORA-'' || status); end; / exit;