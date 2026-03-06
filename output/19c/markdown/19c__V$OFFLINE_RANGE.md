---
id: 19c__V$OFFLINE_RANGE
name: V$OFFLINE_RANGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-OFFLINE_RANGE.html
---

# V$OFFLINE_RANGE

V$OFFLINE_RANGE displays datafile offline information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| FILE# | NUMBER |  |
| OFFLINE_CHANGE# | NUMBER |  |
| ONLINE_CHANGE# | NUMBER |  |
| ONLINE_TIME | DATE |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note that the last offline range of each datafile is kept in the DATAFILE record. An offline range is created for a datafile when its tablespace is first altered to be OFFLINE NORMAL or READ ONLY , and then subsequently altered to be ONLINE or read/write. Note that no offline range is created if the datafile itself is altered to be OFFLINE or if the tablespace is altered to be OFFLINE IMMEDIATE . See Also: " V$DATAFILE " See Also: " V$DATAFILE "