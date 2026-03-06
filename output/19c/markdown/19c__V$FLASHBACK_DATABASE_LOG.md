---
id: 19c__V$FLASHBACK_DATABASE_LOG
name: V$FLASHBACK_DATABASE_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-FLASHBACK_DATABASE_LOG.html
---

# V$FLASHBACK_DATABASE_LOG

V$FLASHBACK_DATABASE_LOG displays information about the flashback data. Use this view to help estimate the amount of flashback space required for the current workload.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OLDEST_FLASHBACK_SCN | NUMBER |  |
| OLDEST_FLASHBACK_TIME | DATE |  |
| RETENTION_TARGET | NUMBER |  |
| FLASHBACK_SIZE | NUMBER |  |
| ESTIMATED_FLASHBACK_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |