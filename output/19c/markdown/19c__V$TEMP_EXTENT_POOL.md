---
id: 19c__V$TEMP_EXTENT_POOL
name: V$TEMP_EXTENT_POOL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-TEMP_EXTENT_POOL.html
---

# V$TEMP_EXTENT_POOL

Name of the tablespace

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace |
| FILE_ID | NUMBER | Absolute file number |
| EXTENTS_CACHED | NUMBER | Number of extents that have been cached |
| EXTENTS_USED | NUMBER | Number of extents that are actually being used |
| BLOCKS_CACHED | NUMBER | Number of blocks that are cached |
| BLOCKS_USED | NUMBER | Number of blocks that are used |
| BYTES_CACHED | NUMBER | Number of bytes that are cached |
| BYTES_USED | NUMBER | Number of bytes that are used |
| RELATIVE_FNO | NUMBER | Relative file number |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |