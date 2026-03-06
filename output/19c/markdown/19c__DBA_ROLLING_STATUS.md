---
id: 19c__DBA_ROLLING_STATUS
name: DBA_ROLLING_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_ROLLING_STATUS.html
---

# DBA_ROLLING_STATUS

DBA_ROLLING_STATUS displays the overall status of the rolling operation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REVISION | NUMBER | Revision number of the current upgrade plan |
| STATUS | VARCHAR2(12) | Readiness of the facility to begin or resume the rolling operation |
| PHASE | VARCHAR2(14) | Current phase of the plan |
| NEXT_INSTRUCTION | NUMBER | Instruction ID of the next pending instruction |
| REMAINING_INSTRUCTIONS | NUMBER | Number of remaining instructions to execute in the plan |
| COORDINATOR_INSTANCE | NUMBER | Instance number from which the rolling operation is being coordinated |
| COORDINATOR_PID | NUMBER | Process PID in which the rolling operation is being coordinated |
| ORIGINAL_PRIMARY | VARCHAR2(128) | Database unique name of the original primary |
| FUTURE_PRIMARY | VARCHAR2(128) | Database unique name of the future primary |
| TOTAL_DATABASES | NUMBER | Number of total databases eligible to participate in the rolling operation |
| PARTICIPATING_DATABASES | NUMBER | Number of databases configured to participate in the rolling operation |
| INIT_TIME | TIMESTAMP(6) | Time of the last call to DBMS_ROLLING . INIT_PLAN |
| BUILD_TIME | TIMESTAMP(6) | Time of the last call to DBMS_ROLLING . BUILD |
| START_TIME | TIMESTAMP(6) | Time of the last call to DBMS_ROLLING . START_UPGRADE |
| SWITCH_TIME | TIMESTAMP(6) | Time of the last call to DBMS_ROLLING . SWITCHOVER |
| FINISH_TIME | TIMESTAMP(6) | Time of the last call to DBMS_ROLLING . FINISH |

## Usage Notes

See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ROLLING package