---
id: 19c__DBA_EXTENTS
name: DBA_EXTENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dba]
source_file: DBA_EXTENTS.html
---

# DBA_EXTENTS

DBA_EXTENTS describes the extents comprising the segments in all tablespaces in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the segment associated with the extent |
| SEGMENT_NAME | VARCHAR2(128) | Name of the segment associated with the extent |
| PARTITION_NAME | VARCHAR2(128) | Object Partition Name (Set to NULL for nonpartitioned objects) |
| SEGMENT_TYPE | VARCHAR2(18) | Type of the segment: INDEX PARTITION, TABLE PARTITION |
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace containing the extent |
| EXTENT_ID | NUMBER | Extent number in the segment |
| FILE_ID | NUMBER | Absolute file number of the data file containing the extent |
| BLOCK_ID | NUMBER | Starting block number of the extent |
| BYTES | NUMBER | Size of the extent in bytes |
| BLOCKS | NUMBER | Size of the extent in Oracle blocks |
| RELATIVE_FNO | NUMBER | Relative file number of the first extent block |

## Usage Notes

Note that if a data file (or entire tablespace) is offline in a locally managed tablespace, you will not see any extent information. If an object has extents in an online file of the tablespace, you will see extent information about the offline data file. However, if the object is entirely in the offline file, a query of this view will not return any records. Related View USER_EXTENTS describes the extents comprising the segments owned by the current user's objects. This view does not display the OWNER , FILE_ID , BLOCK_ID , or RELATIVE_FNO columns. See Also: " USER_EXTENTS " See Also: " USER_EXTENTS "