---
id: 19c__DBA_BLOCKERS
name: DBA_BLOCKERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_BLOCKERS.html
---

# DBA_BLOCKERS

DBA_BLOCKERS displays a session if it is not waiting for a locked object but is holding a lock on an object for which another session is waiting.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HOLDING_SESSION | NUMBER | Session holding a lock |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

In an Oracle RAC environment, this only applies if the blocker is on the same instance.