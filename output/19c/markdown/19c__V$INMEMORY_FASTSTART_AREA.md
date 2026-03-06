---
id: 19c__V$INMEMORY_FASTSTART_AREA
name: V$INMEMORY_FASTSTART_AREA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-INMEMORY_FASTSTART_AREA.html
---

# V$INMEMORY_FASTSTART_AREA

V$INMEMORY_FASTSTART_AREA provides information about the In-Memory FastStart (IM FastStart) area.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_ID | NUMBER |  |
| TABLESPACE_NAME | VARCHAR2(128) |  |
| STATUS | VARCHAR2(10) |  |
| ALLOCATED_SIZE | NUMBER |  |
| USED_SIZE | NUMBER |  |
| LAST_CHECKPOINT_TIME | TIMESTAMP(6) |  |
| LAST_POPULATE_TIME | TIMESTAMP(6) |  |
| NUM_DEFERRED_WRITES | NUMBER |  |