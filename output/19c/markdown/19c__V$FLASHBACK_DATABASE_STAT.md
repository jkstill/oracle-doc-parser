---
id: 19c__V$FLASHBACK_DATABASE_STAT
name: V$FLASHBACK_DATABASE_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-FLASHBACK_DATABASE_STAT.html
---

# V$FLASHBACK_DATABASE_STAT

V$FLASHBACK_DATABASE_STAT displays statistics for monitoring the I/O overhead of logging flashback data. This view also displays the estimated flashback space needed based on previous workloads.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| FLASHBACK_DATA | NUMBER |  |
| DB_DATA | NUMBER |  |
| REDO_DATA | NUMBER |  |
| ESTIMATED_FLASHBACK_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |