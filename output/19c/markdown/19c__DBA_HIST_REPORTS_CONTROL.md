---
id: 19c__DBA_HIST_REPORTS_CONTROL
name: DBA_HIST_REPORTS_CONTROL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_REPORTS_CONTROL.html
---

# DBA_HIST_REPORTS_CONTROL

DBA_HIST_REPORTS_CONTROL contains control information about the report capture mechanism that automatically captures XML reports to Automatic Workload Repository (AWR).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID of the current database for the report |
| EXECUTION_MODE | VARCHAR2(12) | Mode of execution of automatic report capture. Possible values: REGULAR : Regular per-minute report capture subject to DBTIME budget FULL_CAPTURE : Report capture will be run per minute without the DBTIME budget constraints and is provided to capture a more comprehensive set of reports NOTE : The FULL_CAPTURE mode can be started and ended respectively by executing the START_REPORT_CAPTURE and FINISH_REPORT_CAPTURE APIs in the DBMS_AUTO_REPORT package. At all other times, the execution mode should be REGULAR . |

## Usage Notes

Reports are captured automatically for components like SQL Monitor and Real-Time Automatic Database Diagnostic Monitor (Real-Time ADDM). See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUTO_REPORT package See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUTO_REPORT package