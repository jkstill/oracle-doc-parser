---
id: 19c__V$SESS_TIME_MODEL
name: V$SESS_TIME_MODEL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SESS_TIME_MODEL.html
---

# V$SESS_TIME_MODEL

The time values are 8-byte integers and can therefore hold approximately 580,000 years of time before wrapping. Background process time is not included in a statistic value unless the statistic is specifically for background processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| STAT_ID | NUMBER |  |
| STAT_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

The relationships between the statistics listed in Table 9-1 form two trees in which all the time reported by a child in the tree is contained within the parent in the tree. The following are the relationship trees; the number is the level in the given tree. 1) background elapsed time 2) background cpu time 3) RMAN cpu time (backup/restore) 1) DB time 2) DB CPU 2) connection management call elapsed time 2) sequence load elapsed time 2) sql execute elapsed time 2) parse time elapsed 3) hard parse elapsed time 4) hard parse (sharing criteria) elapsed time 5) hard parse (bind mismatch) elapsed time 3) failed parse elapsed time 4) failed parse (out of shared memory) elapsed time 2) PL/SQL execution elapsed time 2) inbound PL/SQL rpc elapsed time 2) PL/SQL compilation elapsed time 2) Java execution elapsed time 2) repeated bind elapsed time The relationship between a parent and a child in the tree indicates containment only. Keep the following in mind regarding the tree: Children do not necessarily add up to the parent. Children are not necessarily exclusive (that is, they may overlap). The union of children does not necessarily cover the whole of the parent. See Also: " V$SYS_TIME_MODEL " See Also: " V$SYS_TIME_MODEL "