---
id: 19c__V$NONLOGGED_BLOCK
name: V$NONLOGGED_BLOCK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-NONLOGGED_BLOCK.html
---

# V$NONLOGGED_BLOCK

V$NONLOGGED_BLOCK displays ranges of nonlogged datafile blocks recorded in the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| BLOCKS | NUMBER |  |
| NONLOGGED_START_CHANGE# | NUMBER |  |
| NONLOGGED_START_TIME | DATE |  |
| NONLOGGED_END_CHANGE# | NUMBER |  |
| NONLOGGED_END_TIME | DATE |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| OBJECT# | VARCHAR2(40) |  |
| REASON | VARCHAR2(9) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Prior to Oracle Database 12 c , the presence of any nonlogged blocks in a data file was recorded in the file header via the FIRST_NONLOGGED_SCN column of the V$DATAFILE view. Now with 12 c , in addition to the file header data, the ranges themselves are recorded in the control file. A control file range is a superset of the actual nonlogged blocks, meaning that small ranges can be merged to form larger ranges, even when there are some valid blocks between the smaller ranges. The information in the view is maintained by RMAN VALIDATE , RMAN RESTORE , RMAN RECOVER , and Flashback Database and Media Recovery. A non RMAN-based restore will cause the data to become invalid, and it will be purged the next time any of those tasks are invoked and involve the file. As a result of space reuse, it is possible for ranges to no longer contain any nonlogged blocks. An RMAN VALIDATE command can be used to synchronize the ranges with the actual nonlogged blocks found from a scan of the data file.