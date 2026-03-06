---
id: 19c__DBMS_SPACE.OBJECT_DEPENDENT_SEGMENTS
name: DBMS_SPACE.OBJECT_DEPENDENT_SEGMENTS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.OBJECT_DEPENDENT_SEGMENTS

This table function, given an object, returns the list of segments that are associated with the object.

## Syntax

```sql
DBMS_SPACE.OBJECT_DEPENDENT_SEGMENTS(
   objowner    IN     VARCHAR2,
   objname     IN     VARCHAR2,
   partname    IN     VARCHAR2,
   objtype     IN     NUMBER) 
  RETURN dependent_segments_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| objowner | VARCHAR2 | IN | The schema containing the object |
| objname | VARCHAR2 | IN | The name of the object |
| partname | VARCHAR2 | IN | The name of the partition |
| objtype | NUMBER) | IN | Type of the object: OBJECT_TYPE_TABLE constant positive := 1; OBJECT_TYPE_NESTED_TABLE constant positive := 2; OBJECT_TYPE_INDEX constant positive := 3; OBJECT_TYPE_CLUSTER constant positive := 4; OBJECT_TYPE_TABLE_PARTITION constant positive := 7; OBJECT_TYPE_INDEX_PARTITION constant positive := 8; OBJECT_TYPE_TABLE_SUBPARTITION constant positive := 9; OBJECT_TYPE_INDEX_SUBPARTITION constant positive := 10; OBJECT_TYPE_MV constant positive := 13; OBJECT_TYPE_MVLOG constant positive := 14; |

**Returns:** `dependent_segments_table`

## Usage Notes

Syntax DBMS_SPACE.OBJECT_DEPENDENT_SEGMENTS( objowner IN VARCHAR2, objname IN VARCHAR2, partname IN VARCHAR2, objtype IN NUMBER) RETURN dependent_segments_table PIPELINED; Parameters Table 158-10 OBJECT_DEPENDENT_SEGMENTS Function Parameters Parameter Description objowner The schema containing the object objname The name of the object partname The name of the partition objtype Type of the object: OBJECT_TYPE_TABLE constant positive := 1; OBJECT_TYPE_NESTED_TABLE constant positive := 2; OBJECT_TYPE_INDEX constant positive := 3; OBJECT_TYPE_CLUSTER constant positive := 4; OBJECT_TYPE_TABLE_PARTITION constant positive := 7; OBJECT_TYPE_INDEX_PARTITION constant positive := 8; OBJECT_TYPE_TABLE_SUBPARTITION constant positive := 9; OBJECT_TYPE_INDEX_SUBPARTITION constant positive := 10; OBJECT_TYPE_MV constant positive := 13; OBJECT_TYPE_MVLOG constant positive := 14; Return Values The content of one row of a dependent_segments_table: TYPE object_dependent_segment IS RECORD ( segment_owner VARCHAR2(100), segment_name VARCHAR2(100), segment_type VARCHAR2(100), tablespace_name VARCHAR2(100), partition_name VARCHAR2(100), lob_column_name VARCHAR2(100)); Table 158-11 OBJECT_DEPENDENT_SEGMENT Type Parameters Parameter Description segment_owner The schema containing the segment segment_name The name of the segment segment_type The type of the segment, such as table, index or LOB tablespace_name The name of the tablespace partition_name The name of the partition, if any lob_column_name The name of the LOB column, if any