---
id: 19c__DBA_APPLY_SPILL_TXN
name: DBA_APPLY_SPILL_TXN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_APPLY_SPILL_TXN.html
---

# DBA_APPLY_SPILL_TXN

DBA_APPLY_SPILL_TXN displays information about the transactions spilled from memory to hard disk by all apply processes in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLY_NAME | VARCHAR2(128) | Name of the apply process that spilled one or more transactions |
| XIDUSN | NUMBER | Transaction ID undo segment number |
| XIDSLT | NUMBER | Transaction ID slot number |
| XIDSQN | NUMBER | Transaction ID sequence number |
| PDB_ID | NUMBER | PDB ID number |
| FIRST_SCN | NUMBER | SCN of the first message in the transaction |
| MESSAGE_COUNT | NUMBER | Number of messages spilled for the transaction |
| FIRST_MESSAGE_CREATE_TIME | DATE | Source creation time of the first message in the transaction |
| SPILL_CREATION_TIME | DATE | Time the first message was spilled |
| FIRST_POSITION | RAW(64) | Position of the first message in this transaction. This column is populated only for an XStream inbound server. |
| TRANSACTION_ID | VARCHAR2(128) | Transaction ID of the spilled transaction |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content