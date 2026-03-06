---
id: 19c__DBMS_LOGMNR_D.SET_TABLESPACE
name: DBMS_LOGMNR_D.SET_TABLESPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGMNR_D
tags: [dbms_logmnr_d]
source_file: DBMS_LOGMNR_D.html
---

# DBMS_LOGMNR_D.SET_TABLESPACE

This procedure moves LogMiner tables from the default SYSAUX tablespace to an alternate tablespace.

## Syntax

```sql
DBMS_LOGMNR_D.SET_TABLESPACE (
     new_tablespace        IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| new_tablespace | VARCHAR2) | IN | A string naming a preexisting tablespace. To move all LogMiner tables to employ this tablespace, supply this parameter. |

## Usage Notes

By default, all LogMiner tables are created to use the SYSAUX tablespace. However, it may be desirable to have LogMiner tables use an alternate tablespace. Use this procedure to move LogMiner tables to this alternate tablespace In a CDB, only the LogMiner metadata in the local container is moved to the requested tablespace. Syntax DBMS_LOGMNR_D.SET_TABLESPACE ( new_tablespace IN VARCHAR2); Parameters Table 103-4 SET_TABLESPACE Parameter Parameter Description new_tablespace A string naming a preexisting tablespace. To move all LogMiner tables to employ this tablespace, supply this parameter. Usage Notes Users upgrading from earlier versions of Oracle Database may find LogMiner tables in the SYSTEM tablespace. Oracle encourages such users to consider using the SET_TABLESPACE procedure to move the tables to the SYSAUX tablespace once they are confident that they will not be downgrading to an earlier version of Oracle Database. Users of this routine must supply an existing tablespace. Example: Using the DBMS_LOGMNR_D.SET_TABLESPACE Procedure The following example shows the creation of an alternate tablespace and execution of the DBMS_LOGMNR_D . SET_TABLESPACE procedure. SQL> CREATE TABLESPACE logmnrts$ datafile '/usr/oracle/dbs/logmnrts.f' SIZE 25 M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED; SQL> EXECUTE dbms_logmnr_d.set_tablespace('logmnrts$');