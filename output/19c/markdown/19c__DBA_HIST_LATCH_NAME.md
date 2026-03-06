---
id: 19c__DBA_HIST_LATCH_NAME
name: DBA_HIST_LATCH_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_LATCH_NAME.html
---

# DBA_HIST_LATCH_NAME

DBA_HIST_LATCH_NAME displays information about decoded latch names for the latches shown in DBA_HIST_LATCH .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| LATCH_HASH | NUMBER | Latch hash |
| LATCH_NAME | VARCHAR2(64) | Latch name |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains a snapshot of V$LATCHNAME . See Also: " DBA_HIST_LATCH " " V$LATCHNAME " See Also: " DBA_HIST_LATCH " " V$LATCHNAME "