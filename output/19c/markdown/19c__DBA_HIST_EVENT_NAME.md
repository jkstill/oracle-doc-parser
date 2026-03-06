---
id: 19c__DBA_HIST_EVENT_NAME
name: DBA_HIST_EVENT_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_EVENT_NAME.html
---

# DBA_HIST_EVENT_NAME

DBA_HIST_EVENT_NAME displays information about wait events.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| EVENT_ID | NUMBER | Identifier of the wait event |
| EVENT_NAME | VARCHAR2(64) | Name of the wait event |
| PARAMETER1 | VARCHAR2(64) | Description of the first parameter for the wait event |
| PARAMETER2 | VARCHAR2(64) | Description of the second parameter for the wait event |
| PARAMETER3 | VARCHAR2(64) | Description of the third parameter for the wait event |
| WAIT_CLASS_ID | NUMBER | Identifier of the class of the wait event |
| WAIT_CLASS | VARCHAR2(64) | Name of the class of the wait event |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains a snapshot of V$EVENT_NAME . See Also: " V$EVENT_NAME " See Also: " V$EVENT_NAME "