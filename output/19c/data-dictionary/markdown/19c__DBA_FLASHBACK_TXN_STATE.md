---
id: 19c__DBA_FLASHBACK_TXN_STATE
name: DBA_FLASHBACK_TXN_STATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_FLASHBACK_TXN_STATE.html
---

# DBA_FLASHBACK_TXN_STATE

DBA_FLASHBACK_TXN_STATE displays information about the compensating status of all transactions in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPENSATING_XID | RAW(8) | Transaction ID of the compensating transaction |
| XID | RAW(8) | A transaction that has been compensated by the compensating transaction |
| DEPENDENT_XID | RAW(8) | A dependent transaction of XID Note: In the case of BACKOUT_MODE = CASCADE , there must be another row with XID = DEPENDENT_XID of this column. |
| BACKOUT_MODE | VARCHAR2(16) | Mode in which XID was backed out: NOCASCADE NOCASCADE_FORCE NONCONFLICT_ONLY CASCADE |
| USERNAME | VARCHAR2(128) | User who is performing the compensating transaction |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content For each compensating transaction, there could be multiple rows, where each row provides the dependency relation between the transactions that have been compensated by the compensating transaction. Related View USER_FLASHBACK_TXN_STATE displays information about the compensating status of the transactions owned by the current user. This view does not display the USERNAME column. See Also: " USER_FLASHBACK_TXN_STATE "