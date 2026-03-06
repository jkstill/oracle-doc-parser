---
id: 19c__DBA_HIST_REPORTS_DETAILS
name: DBA_HIST_REPORTS_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_REPORTS_DETAILS.html
---

# DBA_HIST_REPORTS_DETAILS

DBA_HIST_REPORTS_DETAILS displays details about each report captured in Automatic Workload Repository (AWR).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | ID of the first AWR snapshot that will be taken after this report is generated |
| DBID | NUMBER | Database ID of the current database for the report |
| INSTANCE_NUMBER | NUMBER | Instance number (for an Oracle RAC system) |
| REPORT_ID | NUMBER | ID of the captured report |
| SESSION_ID | NUMBER | ID of the session corresponding to the captured report (currently used only for SQL Monitor reports) |
| SESSION_SERIAL# | NUMBER | Session serial number relevant to this report (currently used only for SQL Monitor reports) |
| GENERATION_TIME | DATE | Time when this report was generated |
| REPORT_COMPRESSED | BLOB | Actual XML report in compressed form |
| REPORT | CLOB | Full uncompressed report |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Metadata for each report appears in the DBA_HIST_REPORTS view while the actual report is available in the DBA_HIST_REPORTS_DETAILS view. See Also: " DBA_HIST_REPORTS " See Also: " DBA_HIST_REPORTS "