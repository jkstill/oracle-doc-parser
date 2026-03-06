---
id: 19c__ALL_SUMDELTA
name: ALL_SUMDELTA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SUMDELTA.html
---

# ALL_SUMDELTA

ALL_SUMDELTA lists direct path load entries accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLEOBJ# | NUMBER | Object number of the table |
| PARTITIONOBJ# | NUMBER | Object number of table partitions (if the table is partitioned) |
| DMLOPERATION | VARCHAR2(1) | Type of DML operation applied to the table |
| SCN | NUMBER | SCN when the bulk DML occurred |
| TIMESTAMP | DATE | Timestamp of the log entry |
| LOWROWID | ROWID | Start ROWID in the loaded rowid range |
| HIGHROWID | ROWID | End ROWID in the loaded rowid range |
| SEQUENCE | NUMBER | Sequence number of the direct load |
| XID | NUMBER | Transaction ID |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content