---
id: 19c__V$TEMPSTAT
name: V$TEMPSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-TEMPSTAT.html
---

# V$TEMPSTAT

V$TEMPSTAT displays information about file read/write statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| PHYRDS | NUMBER |  |
| PHYWRTS | NUMBER |  |
| PHYBLKRD | NUMBER |  |
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

See Also: " TIMED_STATISTICS " See Also: " TIMED_STATISTICS "