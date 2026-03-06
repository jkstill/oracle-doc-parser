---
id: 19c__V$UNDOSTAT
name: V$UNDOSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-UNDOSTAT.html
---

# V$UNDOSTAT

Each row in the view keeps statistics collected in the instance for a 10-minute interval. The rows are in descending order by the BEGIN_TIME column value. Each row belongs to the time interval marked by ( BEGIN_TIME , END_TIME ). Each column represents the data collected for the particular statistic in that time interval. The first row of the view contains statistics for the (partial) current time period. The view contains a total of 576 rows, spanning a 4 day cycle.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| UNDOTSN | NUMBER |  |
| UNDOBLKS | NUMBER |  |
| TXNCOUNT | NUMBER |  |
| MAXQUERYLEN | NUMBER |  |
| MAXQUERYID | VARCHAR2(13) |  |
| MAXCONCURRENCY | NUMBER |  |
| UNXPSTEALCNT | NUMBER |  |
| UNXPBLKRELCNT | NUMBER |  |
| UNXPBLKREUCNT | NUMBER |  |
| EXPSTEALCNT | NUMBER |  |
| EXPBLKRELCNT | NUMBER |  |
| EXPBLKREUCNT | NUMBER |  |
| SSOLDERRCNT | NUMBER |  |
| NOSPACEERRCNT | NUMBER |  |
| ACTIVEBLKS | NUMBER |  |
| UNEXPIREDBLKS | NUMBER |  |
| EXPIREDBLKS | NUMBER |  |
| TUNED_UNDORETENTION | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " UNDO_RETENTION " See Also: " UNDO_RETENTION "