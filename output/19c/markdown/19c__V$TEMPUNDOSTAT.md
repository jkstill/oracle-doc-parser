---
id: 19c__V$TEMPUNDOSTAT
name: V$TEMPUNDOSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-TEMPUNDOSTAT.html
---

# V$TEMPUNDOSTAT

Identifies the beginning of the time interval

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| UNDOTSN | NUMBER |  |
| TXNCOUNT | NUMBER |  |
| MAXCONCURRENCY | NUMBER |  |
| MAXQUERYLEN | NUMBER |  |
| MAXQUERYID | VARCHAR2(13) |  |
| UNDOBLKCNT | NUMBER |  |
| EXTCNT | NUMBER |  |
| USCOUNT | NUMBER |  |
| SSOLDERRCNT | NUMBER |  |
| NOSPACEERRCNT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$UNDOSTAT " See Also: " V$UNDOSTAT "