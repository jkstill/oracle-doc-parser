---
id: 19c__DBA_TABLESPACE_USAGE_METRICS
name: DBA_TABLESPACE_USAGE_METRICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dba]
source_file: DBA_TABLESPACE_USAGE_METRICS.html
---

# DBA_TABLESPACE_USAGE_METRICS

DBA_TABLESPACE_USAGE_METRICS describes tablespace usage metrics for all types of tablespaces, including permanent, temporary, and undo tablespaces.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) | Tablespace name |
| USED_SPACE | NUMBER | Total space consumed by all objects created in the tablespace, expressed as number of data blocks For undo tablespaces, the value of this column includes space consumed by both expired and unexpired undo segments. |
| TABLESPACE_SIZE | NUMBER | The maximum size of the tablespace, expressed as number of data blocks If the tablespace contains any datafiles with autoextend enabled, then this column displays the maximum size to which the tablespace can grow. Underlying storage free space, such as Oracle ASM or file system storage, is also taken into account when computing this value. For example: If a tablespace has a current size of 5 GB, the combined maximum size of its datafiles is 32 GB, and its underlying storage has 20 GB of free space, then this column will have a value of approximately 25 GB. If a tablespace has a current size of 10 GB, the combined maximum size its datafiles is 20 GB, and its underlying storage has 25 GB of free space, then this column will have a value of approximately 20 GB. If the tablespace contains only datafiles with autoextend disabled, then this column displays the combined size of all datafiles in the tablespace. |
| USED_PERCENT | NUMBER | Percentage of used space, as a function of the maximum possible tablespace size |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content