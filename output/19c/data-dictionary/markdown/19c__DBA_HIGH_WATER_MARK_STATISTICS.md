---
id: 19c__DBA_HIGH_WATER_MARK_STATISTICS
name: DBA_HIGH_WATER_MARK_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIGH_WATER_MARK_STATISTICS.html
---

# DBA_HIGH_WATER_MARK_STATISTICS

DBA_HIGH_WATER_MARK_STATISTICS displays information about database high-watermark statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Identifier of the database for which the high-watermark statistics are tracked |
| NAME | VARCHAR2(64) | Name of the high-watermark statistic (see Table 4-1 ) |
| VERSION | VARCHAR2(17) | Database version in which the high watermarks were tracked |
| HIGHWATER | NUMBER | Highest value of the statistic seen at sampling time |
| LAST_VALUE | NUMBER | Value of the statistic at the last sample time |
| DESCRIPTION | VARCHAR2(128) | Description of the high-watermark statistics (see Table 4-1 ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content