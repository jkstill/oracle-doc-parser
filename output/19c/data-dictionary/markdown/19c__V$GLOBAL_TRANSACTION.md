---
id: 19c__V$GLOBAL_TRANSACTION
name: V$GLOBAL_TRANSACTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GLOBAL_TRANSACTION.html
---

# V$GLOBAL_TRANSACTION

V$GLOBAL_TRANSACTION displays information on the currently active global transactions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FORMATID | NUMBER |  |
| GLOBALID | RAW(64) |  |
| BRANCHID | RAW(64) |  |
| BRANCHES | NUMBER |  |
| REFCOUNT | NUMBER |  |
| PREPARECOUNT | NUMBER |  |
| STATE | VARCHAR2(38) |  |
| FLAGS | NUMBER |  |
| COUPLING | VARCHAR2(15) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content