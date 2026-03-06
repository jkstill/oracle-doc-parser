---
id: 19c__V$FLASHFILESTAT
name: V$FLASHFILESTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-FLASHFILESTAT.html
---

# V$FLASHFILESTAT

V$FLASHFILESTAT displays statistics about Database Smart Flash Cache.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FLASHFILE# | NUMBER |  |
| NAME | VARCHAR2(513) |  |
| BYTES | NUMBER |  |
| ENABLED | NUMBER |  |
| SINGLEBLKRDS | NUMBER |  |
| SINGLEBLKRDTIM_MICRO | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content By taking snapshots of SINGLEBLKRDS and SINGLEBLKRDTIM_MICRO , you can easily calculate the average latency of all the flash files in a given time period See Also: Oracle Database Administrator’s Guide for more information about configuring Database Smart Flash Cache See Also: Oracle Database Administrator’s Guide for more information about configuring Database Smart Flash Cache