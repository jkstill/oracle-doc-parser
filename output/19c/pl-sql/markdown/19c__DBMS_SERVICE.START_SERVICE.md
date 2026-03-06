---
id: 19c__DBMS_SERVICE.START_SERVICE
name: DBMS_SERVICE.START_SERVICE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SERVICE
tags: [dbms_service]
source_file: DBMS_SERVICE.html
---

# DBMS_SERVICE.START_SERVICE

This procedure starts a service. In Oracle RAC, implementing this option acts on the instance specified.

## Syntax

```sql
DBMS_SERVICE.START_SERVICE(
   service_name  IN VARCHAR2, 
   instance_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2 | IN | Name of the service limited to 64 characters in the Data Dictionary |
| instance_name | VARCHAR2) | IN | Name of the instance where the service must be activated (optional). NULL results in starting of the service on the local instance. In single instance, this can only be the current instance or NULL . Specify DBMS_SERVICE . ALL_INSTANCES to start the service on all configured instances. |

## Usage Notes

Note: You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle Global Data Services. Note: You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle Global Data Services. Syntax DBMS_SERVICE.START_SERVICE( service_name IN VARCHAR2, instance_name IN VARCHAR2); Parameters Table 153-10 START_SERVICE Procedure Parameters Parameter Description service_name Name of the service limited to 64 characters in the Data Dictionary instance_name Name of the instance where the service must be activated (optional). NULL results in starting of the service on the local instance. In single instance, this can only be the current instance or NULL . Specify DBMS_SERVICE . ALL_INSTANCES to start the service on all configured instances. Examples DBMS_SERVICE.START_SERVICE('ernie.example.com');