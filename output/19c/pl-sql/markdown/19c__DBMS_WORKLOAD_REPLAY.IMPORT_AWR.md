---
id: 19c__DBMS_WORKLOAD_REPLAY.IMPORT_AWR
name: DBMS_WORKLOAD_REPLAY.IMPORT_AWR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.IMPORT_AWR

This procedure imports the AWR snapshots from a given replay.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.IMPORT_AWR (
   replay_id       IN   NUMBER,
   staging_schema  IN   VARCHAR2)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_id | NUMBER | IN | (Mandatory) ID of the replay whose AWR snapshots must be imported |
| staging_schema | VARCHAR2) | IN | (Mandatory) Name of a valid schema in the current database which can be used as a staging area while importing the AWR snapshots from the replay directory to the SYS AWR schema. The SYS schema is not a valid input. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.IMPORT_AWR ( replay_id IN NUMBER, staging_schema IN VARCHAR2) RETURN NUMBER; Parameters Table 191-19 IMPORT_AWR Function Parameters Parameter Description replay_id (Mandatory) ID of the replay whose AWR snapshots must be imported staging_schema (Mandatory) Name of a valid schema in the current database which can be used as a staging area while importing the AWR snapshots from the replay directory to the SYS AWR schema. The SYS schema is not a valid input. Return Values Returns the new randomly generated database ID that was used to import the AWR snapshots. The same value can be found in the AWR_DBID column in the DBA_WORKLOAD_REPLAYS view. Usage Notes This procedure will work provided those AWR snapshots were exported earlier from the original replay system using the EXPORT_AWR Procedure . IMPORT_AWR will fail if the staging_schema provided as input contains any tables with the same name as any of the AWR tables, such as WRM$_SNAPSHOT or WRH$_PARAMETER . Drop any such tables in the staging_schema before invoking IMPORT_AWR .