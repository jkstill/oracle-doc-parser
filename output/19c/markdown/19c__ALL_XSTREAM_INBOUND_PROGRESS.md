---
id: 19c__ALL_XSTREAM_INBOUND_PROGRESS
name: ALL_XSTREAM_INBOUND_PROGRESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XSTREAM_INBOUND_PROGRESS.html
---

# ALL_XSTREAM_INBOUND_PROGRESS

ALL_XSTREAM_INBOUND_PROGRESS displays information about the progress made by the XStream inbound servers accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVER_NAME | VARCHAR2(128) | Name of the inbound server |
| PROCESSED_LOW_POSITION | RAW(64) | Position of the processed low transaction |
| APPLIED_LOW_POSITION | RAW(64) | All messages with a commit position less than this value have been applied |
| APPLIED_HIGH_POSITION | RAW(64) | Highest commit position of a transaction that has been applied |
| SPILL_POSITION | RAW(64) | Position of the spill low watermark of the transactions currently being applied |
| OLDEST_POSITION | RAW(64) | Earliest position of the transactions currently being applied |
| OLDEST_MESSAGE_NUMBER | NUMBER | Earliest message number of the transactions currently being applied |
| APPLIED_MESSAGE_NUMBER | NUMBER | Message number up to which all transactions have definitely been applied. This value is the low watermark for the inbound server. That is, messages with a commit message number less than or equal to this message number have definitely been applied, but some messages with a higher commit message number may also have been applied. |
| APPLIED_TIME | DATE | Time at which the message with the message number displayed in the APPLIED_MESSAGE_NUMBER column was applied |
| APPLIED_MESSAGE_CREATE_TIME | DATE | Time at which the message with the message number displayed in the APPLIED_MESSAGE_NUMBER column was created at its source database |
| SPILL_MESSAGE_NUMBER | NUMBER | Spill low watermark. Any message with a lower SCN has either been applied or spilled to disk. The XStream client application does not need to send logical change records (LCRs) with a lower SCN than the spill low watermark. Spilled messages may not have been applied yet. |
| SOURCE_DATABASE | VARCHAR2(128) | Database where the transaction originated |
| SOURCE_ROOT_NAME | VARCHAR2(128) | The global name of the source root database |

## Usage Notes

Related View DBA_XSTREAM_INBOUND_PROGRESS displays information about the progress made by all XStream inbound servers in the database. See Also: " DBA_XSTREAM_INBOUND_PROGRESS " See Also: " DBA_XSTREAM_INBOUND_PROGRESS "