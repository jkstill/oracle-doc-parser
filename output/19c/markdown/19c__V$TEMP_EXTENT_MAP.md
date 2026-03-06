---
id: 19c__V$TEMP_EXTENT_MAP
name: V$TEMP_EXTENT_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-TEMP_EXTENT_MAP.html
---

# V$TEMP_EXTENT_MAP

V$TEMP_EXTENT_MAP displays the status of each unit for all LOCALLY MANAGED temporary tablespaces.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace this unit belongs to |
| FILE_ID | NUMBER | Absolute file number |
| BLOCK_ID | NUMBER | Begin block number for this unit |
| BYTES | NUMBER | Bytes in the extent |
| BLOCKS | NUMBER | Blocks in the extent |
| OWNER | NUMBER | Instance which owns this unit |
| RELATIVE_FNO | NUMBER | Relative file number |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |