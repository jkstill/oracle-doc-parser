---
id: 19c__V$LOGSTDBY_PROGRESS
name: V$LOGSTDBY_PROGRESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGSTDBY_PROGRESS.html
---

# V$LOGSTDBY_PROGRESS

V$LOGSTDBY_PROGRESS displays the progress of log apply services on the logical standby database. This view is for logical standby databases only.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLIED_SCN | NUMBER |  |
| APPLIED_TIME | DATE |  |
| RESTART_SCN | NUMBER |  |
| RESTART_TIME | DATE |  |
| LATEST_SCN | NUMBER |  |
| LATEST_TIME | DATE |  |
| MINING_SCN | NUMBER |  |
| MINING_TIME | DATE |  |
| RESETLOGS_ID | NUMBER |  |
| CON_ID | NUMBER |  |