---
id: 19c__DBA_FREE_SPACE
name: DBA_FREE_SPACE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_FREE_SPACE.html
---

# DBA_FREE_SPACE

DBA_FREE_SPACE describes the free extents in all tablespaces in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace containing the extent |
| FILE_ID | NUMBER | Absolute file number of the data file containing the extent |
| BLOCK_ID | NUMBER | Starting block number of the extent |
| BYTES | NUMBER | Size of the extent (in bytes) |
| BLOCKS | NUMBER | Size of the extent (in Oracle blocks) |
| RELATIVE_FNO | NUMBER | Relative file number of the file containing the extent |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note that if a data file (or entire tablespace) is offline in a locally managed tablespace, you will not see any extent information. If an object has extents in an online file of the tablespace, you will see extent information about the offline data file. However, if the object is entirely in the offline file, a query of this view will not return any records. Related View USER_FREE_SPACE describes the free extents in the tablespaces accessible to the current user. See Also: " USER_FREE_SPACE "