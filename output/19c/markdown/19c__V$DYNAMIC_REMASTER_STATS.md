---
id: 19c__V$DYNAMIC_REMASTER_STATS
name: V$DYNAMIC_REMASTER_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-DYNAMIC_REMASTER_STATS.html
---

# V$DYNAMIC_REMASTER_STATS

V$DYNAMIC_REMASTER_STATS displays statistical information about the dynamic remastering process of object affinity and read-mostly. All times are given in hundredths of a second, and total values reflect what has been collected since instance startup.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REMASTER_TYPE | VARCHAR2(11) |  |
| REMASTER_OPS | NUMBER |  |
| REMASTER_TIME | NUMBER |  |
| REMASTERED_OBJECTS | NUMBER |  |
| PERSISTENT_OBJECTS Foot 1 | NUMBER |  |
| QUIESCE_TIME | NUMBER |  |
| FREEZE_TIME | NUMBER |  |
| CLEANUP_TIME | NUMBER |  |
| REPLAY_TIME | NUMBER |  |
| FIXWRITE_TIME | NUMBER |  |
| SYNC_TIME | NUMBER |  |
| RESOURCES_CLEANED | NUMBER |  |
| REPLAYED_LOCKS_SENT | NUMBER |  |
| REPLAYED_LOCKS_RECEIVED | NUMBER |  |
| CURRENT_OBJECTS | NUMBER |  |
| CON_ID | NUMBER |  |