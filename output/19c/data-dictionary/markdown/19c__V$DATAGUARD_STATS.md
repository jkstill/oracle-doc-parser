---
id: 19c__V$DATAGUARD_STATS
name: V$DATAGUARD_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-DATAGUARD_STATS.html
---

# V$DATAGUARD_STATS

V$DATAGUARD_STATS displays information about Oracle Data Guard metrics when queried on a standby database. No rows are returned when queried on a primary database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_DBID | NUMBER |  |
| SOURCE_DB_UNIQUE_NAME | VARCHAR2(32) |  |
| NAME | VARCHAR2(32) |  |
| VALUE | VARCHAR2(64) |  |
| UNIT | VARCHAR2(30) |  |
| TIME_COMPUTED | VARCHAR2(30) |  |
| DATUM_TIME | VARCHAR2(30) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content