---
id: 19c__DBMS_HEAT_MAP.OBJECT_HEAT_MAP
name: DBMS_HEAT_MAP.OBJECT_HEAT_MAP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HEAT_MAP
tags: [dbms_heat_map]
source_file: DBMS_HEAT_MAP.html
---

# DBMS_HEAT_MAP.OBJECT_HEAT_MAP

This table function returns the minimum, maximum and average access times for all the segments belonging to the object.

## Syntax

```sql
DBMS_HEAT_MAP.OBJECT_HEAT_MAP (
   object_owner      IN VARCHAR2,
   object_name       IN VARCHAR2) 
 RETURN hm_object_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_owner | VARCHAR2 | IN | Tablespace containing the segment |
| object_name | VARCHAR2) | IN | Segment header relative file number |

**Returns:** `hm_object_table`

## Usage Notes

The object must be a table. The table function raises an error if called on object tables other than table. Syntax DBMS_HEAT_MAP.OBJECT_HEAT_MAP ( object_owner IN VARCHAR2, object_name IN VARCHAR2) RETURN hm_object_table PIPELINED; Parameters Table 80-6 OBJECT_HEAT_MAP Function Parameters Parameter Description object_owner Tablespace containing the segment object_name Segment header relative file number Return Values Table 80-7 OBJECT_HEAT_MAP Function Return Values (Output Parameters ) Parameter Description segment_name Name of the top level segment partition_name Name of the partition tablespace_name Name of the tablespace segment_type Type of segment as in DBA_SEGMENTS.SEGMENT_TYPE segment_size Segment size in bytes min_writetime Oldest write time for the segment max_writetime Latest write time for the segment avg_writetime Average write time for the segment min_readtime Oldest read time for the segment max_readtime Latest read time for the segment avg_writetime Average write time for the segment min_lookuptime Oldest index lookup time for the segment max_lookuptime Latest index lookup time for the segment avg_lookuptime Average index lookup time for the segment min_ftstime Oldest full table scan time for the segment max_ftstime Latest full table scan time for the segment avg_ftstime Average full table scan time for the segment