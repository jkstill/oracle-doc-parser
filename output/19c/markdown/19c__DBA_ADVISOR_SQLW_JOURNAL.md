---
id: 19c__DBA_ADVISOR_SQLW_JOURNAL
name: DBA_ADVISOR_SQLW_JOURNAL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_ADVISOR_SQLW_JOURNAL.html
---

# DBA_ADVISOR_SQLW_JOURNAL

DBA_ADVISOR_SQLW_JOURNAL displays the journal entries for all workload objects in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the workload |
| WORKLOAD_ID | NUMBER | Identifier number of the workload object |
| WORKLOAD_NAME | VARCHAR2(128) | Name of the workload object |
| JOURNAL_ENTRY_SEQ | NUMBER | Sequence number of the journal entry (unique for each workload). The sequence number is used to order the data. |
| JOURNAL_ENTRY_TYPE | VARCHAR2(12) | Type of the task: FATAL ERROR WARNING INFORMATION INFORMATION[2 | 3 | 4 | 5 | 6] |
| JOURNAL_ENTRY | VARCHAR2(4000) | Entry in the journal |

## Usage Notes

Related View USER_ADVISOR_SQLW_JOURNAL displays the journal entries for the workload objects owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLW_JOURNAL " See Also: " USER_ADVISOR_SQLW_JOURNAL "