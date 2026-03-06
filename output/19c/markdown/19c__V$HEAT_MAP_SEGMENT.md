---
id: 19c__V$HEAT_MAP_SEGMENT
name: V$HEAT_MAP_SEGMENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-HEAT_MAP_SEGMENT.html
---

# V$HEAT_MAP_SEGMENT

V$HEAT_MAP_SEGMENT displays real-time segment access information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_NAME | VARCHAR2(128) |  |
| SUBOBJECT_NAME | VARCHAR2(128) |  |
| OBJ# | NUMBER |  |
| DATAOBJ# | NUMBER |  |
| TS# | NUMBER |  |
| TRACK_TIME | DATE |  |
| SEGMENT_WRITE | VARCHAR2(3) |  |
| SEGMENT_READ | VARCHAR2(3) |  |
| FULL_SCAN | VARCHAR2(3) |  |
| LOOKUP_SCAN | VARCHAR2(3) |  |
| N_SEGMENT_WRITE | NUMBER |  |
| N_FULL_SCAN | NUMBER |  |
| N_LOOKUP_SCAN | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " ALL_HEAT_MAP_SEGMENT " See Also: " ALL_HEAT_MAP_SEGMENT "