---
id: 19c__DBMS_SERVICE.STOP_SERVICE
name: DBMS_SERVICE.STOP_SERVICE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SERVICE
tags: [dbms_service]
source_file: DBMS_SERVICE.html
---

# DBMS_SERVICE.STOP_SERVICE

This procedure stops a service.

## Syntax

```sql
DBMS_SERVICE.STOP_SERVICE(
   service_name   IN VARCHAR2,
   instance_name  IN VARCHAR2  DEFAULT NULL,
   stop_option    IN VARCHAR2  DEFAULT NULL,
   drain_timeout  IN NUMBER    DEFAULT NULL,
   replay         IN BOOLEAN   DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2 | IN | Name of the service limited to 64 characters in the Data Dictionary |
| instance_name | VARCHAR2 | IN | Name of the instance where the service must be stopped (optional). NULL results in stopping of the service locally. In single instance, this can only be the current instance or NULL . The default in Oracle RAC and exclusive case is NULL . Specify DBMS_SERVICE . ALL_INSTANCES to stop the service on all configured instances. |
| stop_option | VARCHAR2 | IN | To specify how sessions are stopped with draining. The possible values are as follows: IMMEDIATE : sessions are aborted immediately after the time specified in drain_timeout . TRANASCTIONAL : applies for transactions. After the transaction expires, the sessions are immediately terminated. NONE : sessions are not terminated. These values can be overridden on the command line using SRVCTL . |
| drain_timeout | NUMBER | IN | The time in seconds for the session to drain. |
| replay | BOOLEAN | IN | Enable application continuity replay. |

## Usage Notes

Note: You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle Global Data Services. Note: You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle Global Data Services. Syntax DBMS_SERVICE.STOP_SERVICE( service_name IN VARCHAR2, instance_name IN VARCHAR2 DEFAULT NULL, stop_option IN VARCHAR2 DEFAULT NULL, drain_timeout IN NUMBER DEFAULT NULL, replay IN BOOLEAN DEFAULT TRUE); Parameters Table 153-11 STOP_SERVICE Procedure Parameters Parameter Description service_name Name of the service limited to 64 characters in the Data Dictionary instance_name Name of the instance where the service must be stopped (optional). NULL results in stopping of the service locally. In single instance, this can only be the current instance or NULL . The default in Oracle RAC and exclusive case is NULL . Specify DBMS_SERVICE . ALL_INSTANCES to stop the service on all configured instances. stop_option To specify how sessions are stopped with draining. The possible values are as follows: IMMEDIATE : sessions are aborted immediately after the time specified in drain_timeout . TRANASCTIONAL : applies for transactions. After the transaction expires, the sessions are immediately terminated. NONE : sessions are not terminated. These values can be overridden on the command line using SRVCTL . drain_timeout The time in seconds for the session to drain. replay Enable application continuity replay. Examples DBMS_SERVICE.STOP_SERVICE('ernie.example.com');