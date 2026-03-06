---
id: 19c__DBA_HEATMAP_TOP_OBJECTS
name: DBA_HEATMAP_TOP_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_HEATMAP_TOP_OBJECTS.html
---

# DBA_HEATMAP_TOP_OBJECTS

DBA_HEATMAP_TOP_OBJECTS displays heat map information for the top 10000 objects by default.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Object owner |
| OBJECT_NAME | VARCHAR2(128) | Object name |
| OBJECT_TYPE | VARCHAR2(18) | Object type |
| TABLESPACE_NAME | VARCHAR2(30) | Tablespace name |
| SEGMENT_COUNT | NUMBER | Segments in the tablespace |
| OBJECT_SIZE | NUMBER | Size of the object in MB |
| MIN_WRITETIME | DATE | Oldest modification time for a set of blocks |
| MAX_WRITETIME | DATE | Latest modification time for a set of blocks |
| AVG_WRITETIME | DATE | Average of the modification times for a set of blocks |
| MIN_READTIME | DATE | Oldest read time for a set of blocks |
| MAX_READTIME | DATE | Latest read time for a set of blocks |
| AVG_READTIME | DATE | Average of the read times for a set of blocks |
| MIN_FTSTIME | DATE | Minimum full table scan time of the object |
| MAX_FTSTIME | DATE | Maximum full table scan time of the object |
| AVG_FTSTIME | DATE | Average full table scan time of the object |
| MIN_LOOKUPTIME | DATE | Minimum lookup time of the object |
| MAX_LOOKUPTIME | DATE | Maximum lookup time of the object |
| AVG_LOOKUPTIME | DATE | Average lookup time of the object |

## Usage Notes

If the database contains fewer than 10000 objects, then fewer than 10000 objects are returned by the view.