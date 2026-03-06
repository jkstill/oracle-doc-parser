---
id: 19c__DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT
name: DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT

This function and procedure create a remote snapshot using the Remote Management Framework (RMF). The function returns the snapshot ID.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT(
   node_id     IN NUMBER,
   flush_level IN VARCHAR2 DEFAULT 'BESTFIT');

DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT(
   node_id     IN NUMBER,
   flush_level IN VARCHAR2 DEFAULT 'BESTFIT')
 RETURN NUMBER;

DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT(
   node_name      IN VARCHAR2,
   topology_name  IN VARCHAR2 DEFAULT NULL,
   flush_level    IN VARCHAR2 DEFAULT 'BESTFIT');

DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT(
   node_name      IN VARCHAR2,
   topology_name  IN VARCHAR2 DEFAULT NULL,
   flush_level    IN VARCHAR2 DEFAULT 'BESTFIT')
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| node_id | NUMBER | IN | RMF node identifier of the database for which the snapshot needs to be created. |
| node_name | VARCHAR2 | IN | RMF node name of the database for which the snapshot needs to be created. |
| topology_name | VARCHAR2 | IN | RMF topology name of the database for which the snapshot needs to be created. |
| flush_level | VARCHAR2 | IN | The flush level can be one of the following: BESTFIT : Uses the default value depending on the type of snapshot being taken. LITE : Lightweight snapshot. Only the most important statistics are collected. This is default for a pluggable database (PDB) and application container. TYPICAL : Regular snapshot. Most of the statistics are collected. This is default for a container database root (CDB root) and non-CDB database. ALL : Heavyweight snapshot. All the possible statistics are collected. This consumes a considerable amount of disk space and takes a long time to create. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT( node_id IN NUMBER, flush_level IN VARCHAR2 DEFAULT 'BESTFIT'); DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT( node_id IN NUMBER, flush_level IN VARCHAR2 DEFAULT 'BESTFIT') RETURN NUMBER; DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT( node_name IN VARCHAR2, topology_name IN VARCHAR2 DEFAULT NULL, flush_level IN VARCHAR2 DEFAULT 'BESTFIT'); DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT( node_name IN VARCHAR2, topology_name IN VARCHAR2 DEFAULT NULL, flush_level IN VARCHAR2 DEFAULT 'BESTFIT') RETURN NUMBER; Parameters Table 192-29 CREATE_REMOTE_SNAPSHOT Parameters Parameter Description node_id RMF node identifier of the database for which the snapshot needs to be created. node_name RMF node name of the database for which the snapshot needs to be created. topology_name RMF topology name of the database for which the snapshot needs to be created. flush_level The flush level can be one of the following: BESTFIT : Uses the default value depending on the type of snapshot being taken. LITE : Lightweight snapshot. Only the most important statistics are collected. This is default for a pluggable database (PDB) and application container. TYPICAL : Regular snapshot. Most of the statistics are collected. This is default for a container database root (CDB root) and non-CDB database. ALL : Heavyweight snapshot. All the possible statistics are collected. This consumes a considerable amount of disk space and takes a long time to create. Examples This example creates a remote snapshot of the database having the RMF node identifier of 10 : EXECUTE DBMS_WORKLOAD_REPOSITORY.CREATE_REMOTE_SNAPSHOT(10); If you query the DBA_HIST_SNAPSHOT view after executing the above procedure, you will see a new snapshot record added to the Automatic Workload Repository (AWR).