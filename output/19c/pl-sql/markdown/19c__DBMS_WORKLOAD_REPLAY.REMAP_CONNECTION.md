---
id: 19c__DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION
name: DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION

This procedure remaps the captured connection to a new one so that the user sessions can connect to the database in a desired way during workload replay.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION (
   connection_id         IN  NUMBER,
   replay_connection     IN  VARCHAR2);

DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION (
   capture_number        IN  VARCHAR2,
   connection_id         IN  NUMBER,
   replay_connection     IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_number | VARCHAR2 | IN | Pointing to a capture of the current replay schedule |
| connection_id | NUMBER | IN | ID of the connection to be remapped. Corresponds to DBA_WORKLOAD_CONNECTION_MAP . CONN_ID . |
| replay_connection | VARCHAR2) | IN | New connection string to be used during replay |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION ( connection_id IN NUMBER, replay_connection IN VARCHAR2); DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION ( capture_number IN VARCHAR2, connection_id IN NUMBER, replay_connection IN VARCHAR2); Parameters Table 191-27 REMAP_CONNECTION Procedure Parameters Parameter Description capture_number Pointing to a capture of the current replay schedule connection_id ID of the connection to be remapped. Corresponds to DBA_WORKLOAD_CONNECTION_MAP . CONN_ID . replay_connection New connection string to be used during replay Usage Notes Prior to calling REMAP_CONNECTION all replay connection strings are set to NULL by default. If a replay_connection is NULL , then the replay sessions will connect as determined by the replay client's runtime environment. For example, if the environment variable TNS_ADMIN is defined and the user does not call the REMAP_CONNECTION Procedure , then the wrc executable will connect to the server specified in the tnsnames.ora file pointed to by TNS_ADMIN . A valid replay_connection must specify a connect identifier or a service point. See the Oracle Database Net Services Reference for ways to specify connect identifiers (such as net service names, database service names, and net service aliases) and naming methods that can be used to resolve a connect identifier to a connect descriptor. An error is returned if no row matches the given connection_id . Use the DBA_WORKLOAD_CONNECTION_MAP view to review all the connection strings that are used by the subsequent workload replay, and also to examine connection string remappings used for previous workload replays.