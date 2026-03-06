---
id: 19c__DBA_PENDING_TRANSACTIONS
name: DBA_PENDING_TRANSACTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_PENDING_TRANSACTIONS.html
---

# DBA_PENDING_TRANSACTIONS

DBA_PENDING_TRANSACTIONS describes unresolved transactions (either due to failure or if the coordinator has not sent a commit/rollback).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FORMATID | NUMBER | The format identifier of the transaction identifier |
| GLOBALID | RAW(64) | The global part (gtrid) of the transaction identifier |
| BRANCHID | RAW(64) | The branch qualifier (bqual) of the transaction identifier |