---
id: 19c__ALL_XSTREAM_OUTBOUND_PROGRESS
name: ALL_XSTREAM_OUTBOUND_PROGRESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XSTREAM_OUTBOUND_PROGRESS.html
---

# ALL_XSTREAM_OUTBOUND_PROGRESS

ALL_XSTREAM_OUTBOUND_PROGRESS displays information about the progress made by the XStream outbound servers accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVER_NAME | VARCHAR2(128) | Name of the outbound server |
| SOURCE_DATABASE | VARCHAR2(128) | Global name of the database where the transaction originated. For a PDB, this is the global name of the PDB. |
| PROCESSED_LOW_POSITION | RAW(64) | Position of the low-watermark transaction processed by the outbound server |
| PROCESSED_LOW_TIME | DATE | Time when the processed low position was last updated by the outbound server |
| OLDEST_POSITION | RAW(64) | The position of the earliest LCR that is required by the XStream client application |
| SOURCE_ROOT_NAME | VARCHAR2(128) | The global name of the source root database |
| PROCESSED_LOW_SCN | NUMBER | SCN of the processed low transaction |
| OLDEST_SCN | NUMBER | Oldest SCN of the transactions currently being captured |

## Usage Notes

Related View DBA_XSTREAM_OUTBOUND_PROGRESS displays information about the progress made by all XStream outbound servers in the database. See Also: " DBA_XSTREAM_OUTBOUND_PROGRESS " See Also: " DBA_XSTREAM_OUTBOUND_PROGRESS "