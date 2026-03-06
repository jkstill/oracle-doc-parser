---
id: 19c__V$LOGMNR_LATCH
name: V$LOGMNR_LATCH
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGMNR_LATCH.html
---

# V$LOGMNR_LATCH

V$LOGMNR_LATCH can be joined with the V$LATCH and the V$LATCH_CHILDREN views to obtain statistics about different latches used by active LogMiner persistent sessions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| NAME | VARCHAR2(32) |  |
| CHILD_ADDR | RAW(4 | 8) |  |
| STATE | VARCHAR2(6) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating a Replication capture. See Also: " V$LATCH " " V$LATCH_CHILDREN " See Also: " V$LATCH " " V$LATCH_CHILDREN "