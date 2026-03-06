---
id: 19c__DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE
name: DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE

This procedure registers a remote database in the Automatic Workload Repository (AWR) using the Remote Management Framework (RMF).

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE(
   node_id  IN NUMBER);

DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE(
   node_name      IN VARCHAR2,
   topology_name  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| node_id | NUMBER) | IN | RMF node identifier of the database that needs to be registered in the AWR. |
| node_name | VARCHAR2 | IN | RMF node name of the database that needs to be registered in the AWR. |
| topology_name | VARCHAR2 | IN | RMF topology name of the database that needs to be registered in the AWR. |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE( node_id IN NUMBER); DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE( node_name IN VARCHAR2, topology_name IN VARCHAR2 DEFAULT NULL); Parameters Table 192-37 REGISTER_REMOTE_DATABASE Parameters Parameter Description node_id RMF node identifier of the database that needs to be registered in the AWR. node_name RMF node name of the database that needs to be registered in the AWR. topology_name RMF topology name of the database that needs to be registered in the AWR. Examples This example registers the remote database having the RMF node identifier of 10 in the AWR: EXECUTE DBMS_WORKLOAD_REPOSITORY.REGISTER_REMOTE_DATABASE(10);