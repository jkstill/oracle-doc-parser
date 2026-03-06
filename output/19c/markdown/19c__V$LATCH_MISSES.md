---
id: 19c__V$LATCH_MISSES
name: V$LATCH_MISSES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LATCH_MISSES.html
---

# V$LATCH_MISSES

V$LATCH_MISSES displays statistics about missed attempts to acquire a latch.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PARENT_NAME | VARCHAR2(64) |  |
| WHERE | VARCHAR2(80) |  |
| NWFAIL_COUNT | NUMBER |  |
| SLEEP_COUNT | NUMBER |  |
| WTR_SLP_COUNT | NUMBER |  |
| LONGHOLD_COUNT | NUMBER |  |
| LOCATION | VARCHAR2(80) |  |
| CON_ID | NUMBER |  |