---
id: 19c__V$LATCHNAME
name: V$LATCHNAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LATCHNAME.html
---

# V$LATCHNAME

V$LATCHNAME displays information about decoded latch names for the latches shown in V$LATCH .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LATCH# | NUMBER |  |
| NAME | VARCHAR2(64) |  |
| DISPLAY_NAME | VARCHAR2(64) |  |
| HASH | NUMBER |  |
| TYPE | VARCHAR2(4) |  |
| CON_ID | NUMBER |  |

## Usage Notes

The rows of V$LATCHNAME have a one-to-one correspondence to the rows of V$LATCH . See Also: " V$LATCH " See Also: " V$LATCH "