---
id: 19c__DBA_FLASHBACK_TXN_REPORT
name: DBA_FLASHBACK_TXN_REPORT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_FLASHBACK_TXN_REPORT.html
---

# DBA_FLASHBACK_TXN_REPORT

DBA_FLASHBACK_TXN_REPORT displays information about all compensating transactions that have been committed in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPENSATING_XID | RAW(8) | Transaction responsible for backout |
| COMPENSATING_TXN_NAME | VARCHAR2(256) | Name of the compensating transaction |
| COMMIT_TIME | DATE | Timestamp when the compensating transaction committed |
| XID_REPORT | CLOB | An XML report describing the details of the transactions backed out by the compensating transaction |
| USERNAME | VARCHAR2(128) | User who is executing the compensating transaction |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Each row in this view is associated with one compensating transaction. Related View USER_FLASHBACK_TXN_REPORT displays information about the compensating transactions owned by the current user that have been committed in the database. This view does not display the USERNAME column. See Also: " USER_FLASHBACK_TXN_REPORT "