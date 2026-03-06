---
id: 19c__DBA_WORKLOAD_DIV_SUMMARY
name: DBA_WORKLOAD_DIV_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_DIV_SUMMARY.html
---

# DBA_WORKLOAD_DIV_SUMMARY

Starting with Oracle Database 12.2.0.1, the replay report is generated from DBA_WORKLOAD_DIV_SUMMARY instead of from DBA_WORKLOAD_REPLAY_DIVERGENCE , which results in faster generation of the replay report.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPLAY_ID | NUMBER | ID (key) for the workload replay |
| DIVERGENCE_TYPE | NUMBER | Reserved for future use |
| IS_QUERY_DATA_DIVERGENCE | VARCHAR2(1) | Indicates whether the data divergence is from the number of rows fetched by SELECT queries ( Y ) or not ( N ) |
| IS_DML_DATA_DIVERGENCE | VARCHAR2(1) | Indicates whether the divergence is from the number of rows affected by INSERT, UPDATE, or DELETE SQL statements ( Y ) or not ( N ) |
| IS_ERROR_DIVERGENCE | VARCHAR2(1) | Indicates whether the divergence is from errors seen during capture or replay ( Y ) or not ( N ) |
| IS_THREAD_FAILURE | VARCHAR2(1) | Indicates whether the divergence is from sessions that failed during replay ( Y ) or not ( N ) |
| IS_DATA_MASKED | VARCHAR2(1) | Indicates whether the SQL call contains masked bind data ( Y ) or not ( N ). If data masking technology is used at the replay database, the workload capture files need to be masked. Otherwise, SQL statements generated from capture files that contain sensitive bind data will not match the database. When the replay client sends masked bind data to the server, it turns on the IS_DATA_MASKED flag for the current SQL call. |
| STREAM_ID | NUMBER | Stream ID of the session that reported the divergence |
| SQL_ID | VARCHAR2(13) | SQL ID of the SQL that reported the divergence |
| EXPECTED_ERROR# | NUMBER | Error number that was seen during capture ( 0 if the capture ran successfully) |
| EXPECTED_ERROR_MESSAGE | VARCHAR2(4000) | Text of the error message whose number appears in the EXPECTED_ERROR# column |
| OBSERVED_ERROR# | NUMBER | Actual error number seen during replay ( 0 if the replay ran successfully, 15566 (corresponding to ORA-15566) if the captured call could not be replayed) |
| OBSERVED_ERROR_MESSAGE | VARCHAR2(4000) | Text of the error message whose number appears in the OBSERVED_ERROR# column |
| SERVICE | VARCHAR2(64) | Service name of the session that reported the divergence |
| MODULE | VARCHAR2(64) | Module name of the session that reported the divergence |
| OCCURRENCES | NUMBER | Number of times the divergence occurred during replay |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Example The following query prints the top 3 SQL statements that got error divergence during replay. This query shows the captured error number and the actual error number seen during replay. SQL> SELECT * FROM (SELECT occurrences, sql_id, expected_error#, observed_error# FROM dba_workload_div_summary WHERE replay_id = 123 AND is_error_divergence = 'Y' ORDER BY occurrences DESC) WHERE ROWNUM <= 3; OCCURRENCES SQL_ID EXPECTED_ERROR# OBSERVED_ERROR# ----------- ------------- --------------- --------------- 8 0xrm2wjdqv17m 0 1 4 8bzwdnnznspjd 1422 0 3 6d8rwrac8dsk7 1 1400 SQL> See Also: " DBA_WORKLOAD_REPLAY_DIVERGENCE " See Also: " DBA_WORKLOAD_REPLAY_DIVERGENCE "