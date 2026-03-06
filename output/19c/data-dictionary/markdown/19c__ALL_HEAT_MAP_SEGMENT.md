---
id: 19c__ALL_HEAT_MAP_SEGMENT
name: ALL_HEAT_MAP_SEGMENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [all]
source_file: ALL_HEAT_MAP_SEGMENT.html
---

# ALL_HEAT_MAP_SEGMENT

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Table owner |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| SUBOBJECT_NAME | VARCHAR2(128) | Name of the sub-object |
| SEGMENT_WRITE_TIME | DATE | Latest timestamp on which the segment has write access |
| SEGMENT_READ_TIME | DATE | Latest timestamp on which the segment has read access |
| FULL_SCAN | DATE | Latest timestamp on which the segment has full table scan |
| LOOKUP_SCAN | DATE | Latest timestamp on which the segment has index scan |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_HEAT_MAP_SEGMENT displays the latest segment access time for all segments. USER_HEAT_MAP_SEGMENT displays the latest segment access time for all segments owned by the user. This view does not display the OWNER column. See Also: " DBA_HEAT_MAP_SEGMENT " " USER_HEAT_MAP_SEGMENT " See Also: " DBA_HEAT_MAP_SEGMENT " " USER_HEAT_MAP_SEGMENT "