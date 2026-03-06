---
id: 19c__DBA_HIST_RULE_SET
name: DBA_HIST_RULE_SET
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_RULE_SET.html
---

# DBA_HIST_RULE_SET

DBA_HIST_RULE_SET displays historical information about rule set statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| OWNER | VARCHAR2(128) | Owner of the rule set |
| NAME | VARCHAR2(128) | Name of the rule set |
| STARTUP_TIME | DATE | Startup time of the instance |
| CPU_TIME | NUMBER | Total CPU time (in hundredths of a second) spent in evaluation of the rule set |
| ELAPSED_TIME | NUMBER | Total elapsed time (in hundredths of a second) spent in evaluation of the rule set |
| EVALUATIONS | NUMBER | Number of evaluations on the rule set |
| SQL_FREE_EVALUATIONS | NUMBER | Number of evaluations on the rule set which did not internally issue SQL to evaluate rules |
| SQL_EXECUTIONS | NUMBER | Total number of SQL statements executed during evaluation of the rule set |
| RELOADS | NUMBER | Number of times the rule set object was reloaded in shared memory |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |