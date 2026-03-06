---
id: 19c__DBMS_SERVICE.DISCONNECT_SESSION
name: DBMS_SERVICE.DISCONNECT_SESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SERVICE
tags: [dbms_service]
source_file: DBMS_SERVICE.html
---

# DBMS_SERVICE.DISCONNECT_SESSION

This procedure disconnects sessions with the named service at the current instance.

## Syntax

```sql
DBMS_SERVICE.DISCONNECT_SESSION(
   service_name         IN VARCHAR2,
   disconnect_option    IN NUMBER DEFAULT POST_TRANSACTION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2 | IN | Name of the service, limited to 64 characters in the Data Dictionary |
| disconnect_option | NUMBER | IN | The options, package constants, are expressed as NUMBER : POST_TRANSACTION = 0 : session disconnects after the current transaction commits or rolls back IMMEDIATE = 1 : session disconnects immediately NOREPLAY = 2 : session disconnects immediately and be flagged to not be replayed by application continuity, that is IMMEDIATE and NOREPLAY together Note : IMMEDIATE or POST_TRANSACTION and NOREPLAY is automatically translated as 1 or 0 or 2 respectively. However, passing a string literal (quoted using either the ' or " characters, such as "IMMEDIATE" or 'POST_TRANSACTION' or 'NOREPLAY' ) raises an error. |

## Usage Notes

Syntax DBMS_SERVICE.DISCONNECT_SESSION( service_name IN VARCHAR2, disconnect_option IN NUMBER DEFAULT POST_TRANSACTION; Parameters Table 153-8 DISCONNECT_SESSION Procedure Parameters Parameter Description service_name Name of the service, limited to 64 characters in the Data Dictionary disconnect_option The options, package constants, are expressed as NUMBER : POST_TRANSACTION = 0 : session disconnects after the current transaction commits or rolls back IMMEDIATE = 1 : session disconnects immediately NOREPLAY = 2 : session disconnects immediately and be flagged to not be replayed by application continuity, that is IMMEDIATE and NOREPLAY together Note : IMMEDIATE or POST_TRANSACTION and NOREPLAY is automatically translated as 1 or 0 or 2 respectively. However, passing a string literal (quoted using either the ' or " characters, such as "IMMEDIATE" or 'POST_TRANSACTION' or 'NOREPLAY' ) raises an error. Usage Notes This procedure can be used in the context of a single instance as well as with Oracle Real Application Clusters. This subprogram does not return until all corresponding sessions are disconnected. Therefore, use the DBMS_JOB package or put the SQL session in background if the caller does not want to wait for all corresponding sessions to be disconnected. Examples This disconnects sessions with service_name 'ernie.example.com' . DBMS_SERVICE.DISCONNECT_SESSION('ernie.example.com'); If a service is using application continuity, and you do not want the sessions replayed but simply terminated, use the following: EXECUTE DBMS_SERVICE.DISCONNECT_SESSION(' service name ', DBMS_SERVICE.NOREPLAY);