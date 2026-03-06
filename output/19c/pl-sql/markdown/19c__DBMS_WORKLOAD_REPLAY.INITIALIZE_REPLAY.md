---
id: 19c__DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY
name: DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY

This procedure puts the database state in INIT for REPLAY mode, and loads data into the replay system that is required before preparing for the replay (by executing the PAUSE_REPLAY Procedure).

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY (
   replay_name     IN  VARCHAR2,
   replay_dir      IN  VARCHAR2,
   plsql_mode      IN  VARCHAR2 DEFAULT 'TOP_LEVEL',
   rac_inst_list   IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_name | VARCHAR2 | IN | (Mandatory) Name of the workload replay. Every replay of a processed workload capture can be given a name. |
| replay_dir | VARCHAR2 | IN | Name of the directory object that points to the OS directory (case sensitive) that contains processed capture data |
| plsql_mode | VARCHAR2 | IN | Specifies the replay options for PL/SQL calls: TOP_LEVEL — only top-level PL/SQL calls are replayed EXTENDED — SQL executed from PL/SQL or top-level SQL PL/SQL if there is no SQL recorded inside the PL/SQL are replayed. All captures must have been done in ‘EXTENDED’ PL/SQL mode. |
| rac_inst_list | VARCHAR2 | IN | Specifies a list of Oracle Real Application Clusters (Oracle RAC) instances that will be used for replay. The parameter is a string of instance numbers that are separated by commas. For example: rac_inst_list='1,3,5' |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY ( replay_name IN VARCHAR2, replay_dir IN VARCHAR2, plsql_mode IN VARCHAR2 DEFAULT 'TOP_LEVEL', rac_inst_list IN VARCHAR2 DEFAULT NULL); Parameters Table 191-21 INITIALIZE_REPLAY Procedure Parameters Parameter Description replay_name (Mandatory) Name of the workload replay. Every replay of a processed workload capture can be given a name. replay_dir Name of the directory object that points to the OS directory (case sensitive) that contains processed capture data plsql_mode Specifies the replay options for PL/SQL calls: TOP_LEVEL — only top-level PL/SQL calls are replayed EXTENDED — SQL executed from PL/SQL or top-level SQL PL/SQL if there is no SQL recorded inside the PL/SQL are replayed. All captures must have been done in ‘EXTENDED’ PL/SQL mode. rac_inst_list Specifies a list of Oracle Real Application Clusters (Oracle RAC) instances that will be used for replay. The parameter is a string of instance numbers that are separated by commas. For example: rac_inst_list='1,3,5' Usage Notes Prerequisites: Workload capture was already processed using the PROCESS_CAPTURE Procedure in the same database version. Database state has been logically restored to what it was at the beginning of the original workload capture. The subprogram loads data into the replay system that is required before preparing for the replay by calling the PAUSE_REPLAY Procedure. For instance, during capture the user may record the connection string each session used to connect to the server. The INITIALIZE_REPLAY Procedure loads this data and allows the user to re-map the recorded connection string to new connection strings or service points. Elaborating on the example described in the PROCESS_CAPTURE Procedure, the user could invoke the following: DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY('replay foo #1', 'rec_dir'); This command will load up the connection map and by default will set all replay time connection strings to be equal to NULL . A NULL replay time connection string means that the workload replay clients (WRCs) will connect to the default host as determined by the replay client's runtime environment settings. The user can change a particular connection string to a new one (or a new service point) for replay by using the REMAP_CONNECTION Procedure. For encrypted capture, the INITIALIZE_REPLAY Procedure relies on Oracle wallet. The identifier is oracle.rat.database_replay.encryption (case-sensitive).