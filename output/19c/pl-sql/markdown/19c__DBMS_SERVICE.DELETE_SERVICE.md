---
id: 19c__DBMS_SERVICE.DELETE_SERVICE
name: DBMS_SERVICE.DELETE_SERVICE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SERVICE
tags: [dbms_service]
source_file: DBMS_SERVICE.html
---

# DBMS_SERVICE.DELETE_SERVICE

This procedure deletes a service from the data dictionary.

## Syntax

```sql
DBMS_SERVICE.DELETE_SERVICE(
   service_name   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2) | IN | Name of the service, limited to 64 characters in the Data Dictionary |

## Usage Notes

Note: Starting with Oracle Database 19c, customer use of the SERVICE_NAME parameter is deprecated. It can be desupported in a future release. It must not be used for high availability (HA) deployments. It is not supported to use service name parameter for any HA operations. This restriction includes FAN, load balancing, FAILOVER_TYPE , FAILOVER_RESTORE , SESSION_STATE_CONSISTENCY , and any other uses. You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart, or Oracle Global Data Services. Note: Starting with Oracle Database 19c, customer use of the SERVICE_NAME parameter is deprecated. It can be desupported in a future release. It must not be used for high availability (HA) deployments. It is not supported to use service name parameter for any HA operations. This restriction includes FAN, load balancing, FAILOVER_TYPE , FAILOVER_RESTORE , SESSION_STATE_CONSISTENCY , and any other uses. You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart, or Oracle Global Data Services. Syntax DBMS_SERVICE.DELETE_SERVICE( service_name IN VARCHAR2); Parameters Table 153-7 DELETE_SERVICE Procedure Parameters Parameter Description service_name Name of the service, limited to 64 characters in the Data Dictionary Examples DBMS_SERVICE.DELETE_SERVICE('ernie.example.com');