---
id: 19c__V$ARCHIVE_GAP
name: V$ARCHIVE_GAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-ARCHIVE_GAP.html
---

# V$ARCHIVE_GAP

V$ARCHIVE_GAP displays information about archive gaps on a standby database. This view can be used to find out the current archive gap that is blocking recovery for the current recovery incarnation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| THREAD# | NUMBER |  |
| LOW_SEQUENCE# | NUMBER |  |
| HIGH_SEQUENCE# | NUMBER |  |
| CON_ID | NUMBER |  |