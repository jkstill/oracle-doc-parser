---
id: 19c__ALL_GG_INBOUND_PROGRESS
name: ALL_GG_INBOUND_PROGRESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_GG_INBOUND_PROGRESS.html
---

# ALL_GG_INBOUND_PROGRESS

ALL_GG_INBOUND_PROGRESS displays information about the progress made by the GoldenGate inbound servers accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVER_NAME | VARCHAR2(128) | Name of the inbound server |
| PROCESSED_LOW_POSITION | VARCHAR2(4000) | Position of the processed low transaction |
| APPLIED_LOW_POSITION | VARCHAR2(4000) | All messages with commit position less than this value have been applied. This column should be used to view the progress of the GoldenGate apply. This column will hold an Oracle SCN numeric value in text format for an Oracle source database. For a non-Oracle source database, this column will hold the apply low position in GoldenGate CSN text format for that specific source database. |
| APPLIED_HIGH_POSITION | VARCHAR2(4000) | Highest commit position of a transaction that has been applied |
| SPILL_POSITION | VARCHAR2(4000) | Position of the spill low watermark of the transactions currently being applied |
| OLDEST_POSITION | VARCHAR2(4000) | Earliest position of the transactions currently being applied |
| APPLIED_LOW_SCN | NUMBER | All SCN below or equal to this number have been successfully applied. This column is not applicable for GoldenGate replication since the source database may be non-Oracle. |
| APPLIED_TIME | DATE | Time at which the APPLIED_MESSAGE_NUMBER message was applied |
| APPLIED_MESSAGE_CREATE_TIME | DATE | Time at which the APPLIED_MESSAGE_NUMBER message was created |
| SOURCE_DATABASE | VARCHAR2(128) | Database where the transaction originated |
| SOURCE_ROOT_NAME | VARCHAR2(128) | The global name of the source root database where all transactions originated |
| LOGBSN | VARCHAR2(4000) | Log BSN value from the GoldenGate trail file |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_GG_INBOUND_PROGRESS displays information about the progress made by all GoldenGate inbound servers in the database. See Also: " DBA_GG_INBOUND_PROGRESS " See Also: " DBA_GG_INBOUND_PROGRESS "