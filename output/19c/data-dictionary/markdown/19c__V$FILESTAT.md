---
id: 19c__V$FILESTAT
name: V$FILESTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-FILESTAT.html
---

# V$FILESTAT

V$FILESTAT displays the number of physical reads and writes done and the total number of single-block and multiblock I/Os done at file level.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| PHYRDS | NUMBER |  |
| PHYWRTS | NUMBER |  |
| PHYBLKRD | NUMBER |  |
| OPTIMIZED_PHYBLKRD | NUMBER |  |
| PHYBLKWRT | NUMBER |  |
| SINGLEBLKRDS | NUMBER |  |
| READTIM | NUMBER |  |
| WRITETIM | NUMBER |  |
| SINGLEBLKRDTIM | NUMBER |  |
| AVGIOTIM | NUMBER |  |
| LSTIOTIM | NUMBER |  |
| MINIOTIM | NUMBER |  |
| MAXIORTM | NUMBER |  |
| MAXIOWTM | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content As of Oracle Database 10g Release 2 (10.2), this view also includes reads done by RMAN processes for backup operations.