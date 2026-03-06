---
id: 19c__DBA_FREE_SPACE_COALESCED
name: DBA_FREE_SPACE_COALESCED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_FREE_SPACE_COALESCED.html
---

# DBA_FREE_SPACE_COALESCED

DBA_FREE_SPACE_COALESCED describes statistics on coalesced space in all tablespaces in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace |
| TOTAL_EXTENTS | NUMBER | Total number of free extents in the tablespace |
| EXTENTS_COALESCED | NUMBER | Total number of coalesced free extents in the tablespace |
| PERCENT_EXTENTS _COALESCED | NUMBER | Percentage of coalesced free extents in the tablespace |
| TOTAL_BYTES | NUMBER | Total number of free bytes in the tablespace |
| BYTES_COALESCED | NUMBER | Total number of coalesced free bytes in the tablespace |
| TOTAL_BLOCKS | NUMBER | Total number of free Oracle blocks in the tablespace |
| BLOCKS_COALESCED | NUMBER | Total number of coalesced free Oracle blocks in the tablespace |
| PERCENT_BLOCKS _COALESCED | NUMBER | Percentage of coalesced free Oracle blocks in the tablespace |