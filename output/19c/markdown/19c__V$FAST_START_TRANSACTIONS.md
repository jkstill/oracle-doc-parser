---
id: 19c__V$FAST_START_TRANSACTIONS
name: V$FAST_START_TRANSACTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FAST_START_TRANSACTIONS.html
---

# V$FAST_START_TRANSACTIONS

V$FAST_START_TRANSACTIONS displays information about the progress of the transactions that Oracle is recovering.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USN | NUMBER |  |
| SLT | NUMBER |  |
| SEQ | NUMBER |  |
| STATE | VARCHAR2(16) |  |
| UNDOBLOCKSDONE | NUMBER |  |
| UNDOBLOCKSTOTAL | NUMBER |  |
| PID | NUMBER |  |
| CPUTIME | NUMBER |  |
| PARENTUSN | NUMBER |  |
| PARENTSLT | NUMBER |  |
| PARENTSEQ | NUMBER |  |
| XID | RAW(8) |  |
| PXID | RAW(8) |  |
| RCVSERVERS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

This view displays only transactions recovered in parallel. Recovery progress for serial transactions is not displayed.