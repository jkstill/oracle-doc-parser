---
id: 19c__V$LOGMNR_DICTIONARY_LOAD
name: V$LOGMNR_DICTIONARY_LOAD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGMNR_DICTIONARY_LOAD.html
---

# V$LOGMNR_DICTIONARY_LOAD

V$LOGMNR_DICTIONARY_LOAD displays information about LogMiner dictionaries for all active LogMiner sessions on the system.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| LOGMNR_UID | NUMBER |  |
| ACTION# | NUMBER |  |
| OPCODE | NUMBER |  |
| COMMAND | VARCHAR2(161) |  |
| CURRENT_STATE | VARCHAR2(32) |  |
| COMPLETED_ACTIONS | NUMBER |  |
| TOTAL_ACTIONS | NUMBER |  |
| LOADED | VARCHAR2(7) |  |
| PERCENT_DONE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Each query of this view will return one row for each attached LogMiner session. This view will not show valid information for LogMiner adhoc query clients.