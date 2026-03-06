---
id: 19c__DBA_ADVISOR_USAGE
name: DBA_ADVISOR_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_USAGE.html
---

# DBA_ADVISOR_USAGE

DBA_ADVISOR_USAGE displays the usage information for each type of advisor in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADVISOR_ID | NUMBER | Type of the advisor |
| ADVISOR_NAME | VARCHAR2(128) | Name of the advisor |
| LAST_EXEC_TIME | DATE | Date of the last execution |
| NUM_EXECS | NUMBER | Cumulative number of executions |
| NUM_DB_REPORTS | NUMBER | Cumulative number of reports |
| FIRST_REPORT_TIME | DATE | Time of the first report |
| LAST_REPORT_TIME | DATE | Time of the last report |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content