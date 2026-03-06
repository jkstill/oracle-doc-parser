---
id: 19c__DBMS_WORKLOAD_REPOSITORY.CONTROL_RESTRICTED_SNAPSHOT
name: DBMS_WORKLOAD_REPOSITORY.CONTROL_RESTRICTED_SNAPSHOT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.CONTROL_RESTRICTED_SNAPSHOT

This procedure controls the AWR snapshot creation for a database in the restricted session mode. If this procedure is not used, then by default, the AWR snapshots cannot be created for a database in the restricted session mode. This procedure affects the local database on which it is executed.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.CONTROL_RESTRICTED_SNAPSHOT(
   allow IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| allow | BOOLEAN) | IN | This parameter can have one of the following values: TRUE : AWR snapshots can be created for the database in the restricted session mode. FALSE : AWR snapshots cannot be created for the database in the restricted session mode. |

## Usage Notes

Note: To enable AWR snapshot creation for an Oracle RAC in the restricted session mode, this procedure must be executed on every database instance in the Oracle RAC. Note: To enable AWR snapshot creation for an Oracle RAC in the restricted session mode, this procedure must be executed on every database instance in the Oracle RAC. Syntax DBMS_WORKLOAD_REPOSITORY.CONTROL_RESTRICTED_SNAPSHOT( allow IN BOOLEAN); Parameters Table 192-26 CONTROL_RESTRICTED_SNAPSHOT Parameters Parameter Description allow This parameter can have one of the following values: TRUE : AWR snapshots can be created for the database in the restricted session mode. FALSE : AWR snapshots cannot be created for the database in the restricted session mode.