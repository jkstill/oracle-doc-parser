---
id: 19c__DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE
name: DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE

This procedure removes all the statistics, metadata, partitions, and so on of a remote database from the Automatic Workload Repository (AWR). After executing this procedure, the remote database cannot be used for any AWR operations, such as creating remote snapshots.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE(
   node_id        IN NUMBER,
   remote_check   IN BOOLEAN  DEFAULT TRUE);

DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE(
   node_name      IN VARCHAR2,
   topology_name  IN VARCHAR2 DEFAULT NULL,
   remote_check   IN BOOLEAN  DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| node_id | NUMBER | IN | Identifier of the remote database whose data needs to be removed from the AWR. |
| node_name | VARCHAR2 | IN | Name of the remote database whose data needs to be removed from the AWR. |
| topology_name | VARCHAR2 | IN | RMF topology name of the remote database. |
| remote_check | BOOLEAN | IN | If set to TRUE , the remote database’s metadata is validated before removing its data from the AWR. This option requires the remote database to be available. If set to FALSE , the remote database’s data is removed from the AWR without validating its metadata. This option must be selected to unregister a remote database that is not available (it is offline or there is a network outage). |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE( node_id IN NUMBER, remote_check IN BOOLEAN DEFAULT TRUE); DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE( node_name IN VARCHAR2, topology_name IN VARCHAR2 DEFAULT NULL, remote_check IN BOOLEAN DEFAULT TRUE); Parameters Table 192-42 UNREGISTER_REMOTE_DATABASE Parameters Parameter Description node_id Identifier of the remote database whose data needs to be removed from the AWR. node_name Name of the remote database whose data needs to be removed from the AWR. topology_name RMF topology name of the remote database. remote_check If set to TRUE , the remote database’s metadata is validated before removing its data from the AWR. This option requires the remote database to be available. If set to FALSE , the remote database’s data is removed from the AWR without validating its metadata. This option must be selected to unregister a remote database that is not available (it is offline or there is a network outage). Examples This example removes the AWR data related to the remote database having the database identifier of 10 : EXECUTE DBMS_WORKLOAD_REPOSITORY.UNREGISTER_REMOTE_DATABASE(10);