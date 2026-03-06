---
id: 19c__DBMS_LOGSTDBY.PREPARE_FOR_NEW_PRIMARY
name: DBMS_LOGSTDBY.PREPARE_FOR_NEW_PRIMARY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.PREPARE_FOR_NEW_PRIMARY

The PREPARE_FOR_NEW_PRIMARY procedure must be invoked at a logical standby database following a failover, if that standby database was not the target of the failover operation.

## Syntax

```sql
DBMS_LOGSTDBY.PREPARE_FOR_NEW_PRIMARY (
           FORMER_STANDBY_TYPE         IN VARCHAR2,
           DBLINK                      IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| FORMER_STANDBY_TYPE | VARCHAR2 | IN | The type of standby database that was the target of the failover operation to become the new primary database. Valid values are ' PHYSICAL ' if the new primary was formerly a physical standby, and ' LOGICAL ' if the new primary database was formerly a logical standby database. |
| DBLINK | VARCHAR2) | IN | The name of a database link to the new primary database |

## Usage Notes

Such a standby database must process the exact same set of redo logs processed at the new primary database. This routine ensures that the local logical standby database has not processed more redo than the new primary database and reports the set of archive logs that must be replaced to ensure consistency. The set of replacement logs will be reported in the alert.log. These logs must be copied to the logical standby and registered using the ALTER DATABASE REGISTER LOGICAL LOGFILE statement. In a CDB, the PREPARE_FOR_NEW_PRIMARY procedure must be called from the root database. Syntax DBMS_LOGSTDBY.PREPARE_FOR_NEW_PRIMARY ( FORMER_STANDBY_TYPE IN VARCHAR2, DBLINK IN VARCHAR2); Parameters Table 102-9 PREPARE_FOR_NEW_PRIMARY Procedure Parameters Parameter Description FORMER_STANDBY_TYPE The type of standby database that was the target of the failover operation to become the new primary database. Valid values are ' PHYSICAL ' if the new primary was formerly a physical standby, and ' LOGICAL ' if the new primary database was formerly a logical standby database. DBLINK The name of a database link to the new primary database Exceptions Table 102-10 PREPARE_FOR_NEW_PRIMARY Procedure Exceptions Exception Description ORA-16104 Invalid Logical Standby option. ORA-16109 Failed to apply log data from previous primary. Usage Notes This routine is intended only for logical standby systems.This routine will fail if the new primary database was formerly a logical standby database and the LogMiner dictionary build has not completed successfully.Log files displayed in the alert log will be referred to as terminal logs . Users should keep in mind that file paths are relative to the new primary database and may not resolve locally.Upon manual registration of the terminal logs, users should complete the process by calling either START LOGICAL STANDBY APPLY if the new primary database was formerly a physical standby database or START LOGICAL STANDBY APPLY NEW PRIMARY if the new primary database was formerly a logical standby database.See the alert log for more details regarding the reasons for any exception.