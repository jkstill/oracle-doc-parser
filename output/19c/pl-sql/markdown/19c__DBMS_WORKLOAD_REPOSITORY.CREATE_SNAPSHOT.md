---
id: 19c__DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT
name: DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT

This function and procedure create a snapshot. The function returns the snapshot ID. If both, the database ID and the database name are not specified in this subprogram, then the snapshot is created for the local database on which the subprogram is executed.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT(
   flush_level IN VARCHAR2 DEFAULT 'BESTFIT',
   dbid        IN NUMBER   DEFAULT NULL,
   source_name IN VARCHAR2 DEFAULT NULL);

DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT(
   flush_level IN VARCHAR2 DEFAULT 'BESTFIT',
   dbid        IN NUMBER   DEFAULT NULL,
   source_name IN VARCHAR2 DEFAULT NULL)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| flush_level | VARCHAR2 | IN | The flush level can be one of the following: BESTFIT : Uses the default value depending on the type of snapshot being taken. LITE : Lightweight snapshot. Only the most important statistics are collected. This is default for a pluggable database (PDB) and application container. TYPICAL : Regular snapshot. Most of the statistics are collected. This is default for a container database root (CDB root) and non-CDB database. ALL : Heavyweight snapshot. All the possible statistics are collected. This consumes a considerable amount of disk space and takes a long time to create. |
| dbid | NUMBER | IN | Database ID of the database for which the snapshot needs to be created. |
| source_name | VARCHAR2 | IN | Name of the database for which the snapshot needs to be created. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT( flush_level IN VARCHAR2 DEFAULT 'BESTFIT', dbid IN NUMBER DEFAULT NULL, source_name IN VARCHAR2 DEFAULT NULL); DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT( flush_level IN VARCHAR2 DEFAULT 'BESTFIT', dbid IN NUMBER DEFAULT NULL, source_name IN VARCHAR2 DEFAULT NULL) RETURN NUMBER; Parameters Table 192-30 CREATE_SNAPSHOT Parameters Parameter Description flush_level The flush level can be one of the following: BESTFIT : Uses the default value depending on the type of snapshot being taken. LITE : Lightweight snapshot. Only the most important statistics are collected. This is default for a pluggable database (PDB) and application container. TYPICAL : Regular snapshot. Most of the statistics are collected. This is default for a container database root (CDB root) and non-CDB database. ALL : Heavyweight snapshot. All the possible statistics are collected. This consumes a considerable amount of disk space and takes a long time to create. dbid Database ID of the database for which the snapshot needs to be created. source_name Name of the database for which the snapshot needs to be created. Examples This example creates a snapshot of the local database with the flush level of ALL : EXECUTE DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT('ALL'); If you query the DBA_HIST_SNAPSHOT view after executing the above procedure, you will see a new snapshot record added to the Automatic Workload Repository (AWR).