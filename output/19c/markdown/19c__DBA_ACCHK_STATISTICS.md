---
id: 19c__DBA_ACCHK_STATISTICS
name: DBA_ACCHK_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_ACCHK_STATISTICS.html
---

# DBA_ACCHK_STATISTICS

DBA_ACCHK_STATISTICS displays Application Continuity protection statistics for each session that executed during an Application Continuity Protection Check (ACCHK) workload run.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER | Identifier for the instance for the session |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |
| TIMESTAMP | TIMESTAMP(3) WITH TIME ZONE | Time at which the session was terminated and the statistics were reported |
| SESSION_ID | NUMBER | ID of the session |
| SERIAL# | NUMBER | Serial number of the session |
| STAT_TYPE | VARCHAR2(32) | Type of statistic The value of this column is always SESSION_STATISTICS . |
| SERVICE_NAME | VARCHAR2(64) | Service name of the session |
| FAILOVER_TYPE | VARCHAR2(16) | Indicates the FAILOVER_TYPE service setting for the session. Possible values: AUTO - Transparent Application Continuity (TAC) was enabled for the session TRANSACTION - Application Continuity (AC) was enabled for the session NONE - Failover was disabled for the session |
| FAILOVER_RESTORE | VARCHAR2(16) | Indicates the FAILOVER_RESTORE service setting for the session. Possible values: AUTO - Transparent Application Continuity LEVEL1 - Application Continuity NONE - Session state was not restored at failover |
| RESET_STATE | VARCHAR2(16) | Indicates the RESET_STATE service setting for the session. Possible values: LEVEL1 - The session state was cleaned at the end of a request NONE - The session state was not cleaned at the end of a request |
| PROGRAM | VARCHAR2(84) | Name of the operating system program |
| BEGIN_REQUESTS | NUMBER | Number of begin requests received for the session |
| END_REQUESTS | NUMBER | Number of end requests received for the session |
| USER_CALLS_IN_REQUESTS | NUMBER | Number of user calls received from the application within requests (between begin request and end request) |
| PROTECTED_CALLS_IN_REQUESTS | NUMBER | Number of user calls protected by Application Continuity (between begin request and end request) |
| TIME_IN_REQUESTS | NUMBER | Time in microseconds spent in user calls within requests (between begin request and end request) |
| TIME_PROTECTED_IN_REQUESTS | NUMBER | Time in microseconds for user calls protected by Application Continuity within requests (between begin request and end request) |

## Usage Notes

ACCHK should be used on a running workload. Sessions that are aborted are not included in this view. The ACCHK_READ role allows users with no administrative privileges to query this view. Column Datatype NULL Description INST_ID NUMBER Identifier for the instance for the session CON_ID NUMBER The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data TIMESTAMP TIMESTAMP(3) WITH TIME ZONE Time at which the session was terminated and the statistics were reported SESSION_ID NUMBER ID of the session SERIAL# NUMBER Serial number of the session STAT_TYPE VARCHAR2(32) Type of statistic The value of this column is always SESSION_STATISTICS . SERVICE_NAME VARCHAR2(64) Service name of the session FAILOVER_TYPE VARCHAR2(16) Indicates the FAILOVER_TYPE service setting for the session. Possible values: AUTO - Transparent Application Continuity (TAC) was enabled for the session TRANSACTION - Application Continuity (AC) was enabled for the session NONE - Failover was disabled for the session FAILOVER_RESTORE VARCHAR2(16) Indicates the FAILOVER_RESTORE service setting for the session. Possible values: AUTO - Transparent Application Continuity LEVEL1 - Application Continuity NONE - Session state was not restored at failover RESET_STATE VARCHAR2(16) Indicates the RESET_STATE service setting for the session. Possible values: LEVEL1 - The session state was cleaned at the end of a request NONE - The session state was not cleaned at the end of a request PROGRAM VARCHAR2(84) Name of the operating system program BEGIN_REQUESTS NUMBER Number of begin requests received for the session END_REQUESTS NUMBER Number of end requests received for the session USER_CALLS_IN_REQUESTS NUMBER Number of user calls received from the application within requests (between begin request and end request) PROTECTED_CALLS_IN_REQUESTS NUMBER Number of user calls protected by Application Continuity (between begin request and end request) TIME_IN_REQUESTS NUMBER Time in microseconds spent in user calls within requests (between begin request and end request) TIME_PROTECTED_IN_REQUESTS NUMBER Time in microseconds for user calls protected by Application Continuity within requests (between begin request and end request) Note: This view is available starting with Oracle Database release 19c, version 19.11. However, it is not created by default in Oracle Database release 19c. To create this view, you must run the DBMS_APP_CONT_ADMIN.ACCHK_VIEWS( ) procedure. See Oracle Database PL/SQL Packages and Types Reference for more information. Note: This view is available starting with Oracle Database release 19c, version 19.11. However, it is not created by default in Oracle Database release 19c. To create this view, you must run the DBMS_APP_CONT_ADMIN.ACCHK_VIEWS( ) procedure. See Oracle Database PL/SQL Packages and Types Reference for more information.