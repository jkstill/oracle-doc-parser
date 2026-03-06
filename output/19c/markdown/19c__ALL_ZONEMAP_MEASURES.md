---
id: 19c__ALL_ZONEMAP_MEASURES
name: ALL_ZONEMAP_MEASURES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ZONEMAP_MEASURES.html
---

# ALL_ZONEMAP_MEASURES

ALL_ZONEMAP_MEASURES describes the measures for all zone maps accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the zone map |
| ZONEMAP_NAME | VARCHAR2(128) | Name of the zone map |
| MEASURE | LONG | Column whose MIN/ MAX value is computed |
| POSITION_IN_SELECT | NUMBER | Original position of the mesaure aggregate on the SELECT list of zone map defining query |
| AGG_FUNCTION | VARCHAR2(13) | Name of aggregate in zone map table |
| AGG_COLUMN_NAME | VARCHAR2(128) | Name of the column whose MIN /MAX per zone maintained |

## Usage Notes

Related Views DBA_ZONEMAP_MEASURES describes the measures for all the zone maps in the database. USER_ZONEMAP_MEASURES describes the measures for all the zone maps owned by the user. Note: This view is intended for use with Oracle Exadata release 12.1.2.1.1 or later. See Also: " DBA_ZONEMAP_MEASURES " " USER_ZONEMAP_MEASURES " Oracle Database Data Warehousing Guide for more information about zone maps Note: This view is intended for use with Oracle Exadata release 12.1.2.1.1 or later. See Also: " DBA_ZONEMAP_MEASURES " " USER_ZONEMAP_MEASURES " Oracle Database Data Warehousing Guide for more information about zone maps