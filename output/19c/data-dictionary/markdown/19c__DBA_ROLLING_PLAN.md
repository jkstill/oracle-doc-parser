---
id: 19c__DBA_ROLLING_PLAN
name: DBA_ROLLING_PLAN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ROLLING_PLAN.html
---

# DBA_ROLLING_PLAN

DBA_ROLLING_PLAN displays the instructions which constitute the active upgrade plan.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REVISION | NUMBER | Plan revision number associated with an instruction |
| BATCHID | NUMBER | Identifier for a batch of instructions which are requested together |
| INSTID | NUMBER | Identifier for a single instruction |
| SOURCE | VARCHAR2(128) | Database unique name where an instruction executes |
| TARGET | VARCHAR2(128) | The site where a given instruction will execute |
| PHASE | VARCHAR2(14) | rolling operation phase in which an instruction executes |
| STATUS | VARCHAR2(7) | Scheduling status of the instruction |
| PROGRESS | VARCHAR2(10) | Execution progress of the instruction |
| DESCRIPTION | VARCHAR2(256) | Description of the instruction |
| EXEC_STATUS | NUMBER | Status code returned from instruction execution |
| EXEC_INFO | VARCHAR2(256) | Supplemental information obtained during instruction execution |
| EXEC_TIME | TIMESTAMP(6) | Time of instruction execution |
| FINISH_TIME | TIMESTAMP(6) | Time of instruction completion |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Each row in DBA_ROLLING_PLAN identifies a specific instruction scheduled to execute at a specific database. Instructions are created as a result of successful calls to the DBMS_ROLLING.BUILD_PLAN procedure. During execution, groups of instructions are scheduled in batches to execute at remote databases. Groups of instructions are guaranteed to complete in BATCHID order. See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package