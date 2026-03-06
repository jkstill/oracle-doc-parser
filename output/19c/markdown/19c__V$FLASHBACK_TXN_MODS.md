---
id: 19c__V$FLASHBACK_TXN_MODS
name: V$FLASHBACK_TXN_MODS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FLASHBACK_TXN_MODS.html
---

# V$FLASHBACK_TXN_MODS

V$FLASHBACK_TXN_MODS displays the individual modifications of all the transactions in memory.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPENSATING_XID | RAW(8) |  |
| COMPENSATING_TXN_NAME | VARCHAR2(255) |  |
| XID | RAW(8) |  |
| TXN_NAME | VARCHAR2(255) |  |
| PARENT_XID | RAW(8) |  |
| INTERESTING | NUMBER |  |
| ORIGINAL | NUMBER |  |
| BACKOUT_SEQ | NUMBER |  |
| UNDO_SQL | VARCHAR2(4000) |  |
| UNDO_SQL_SQN | NUMBER |  |
| UNDO_SQL_SUB_SQN | NUMBER |  |
| BACKOUT_SQL_ID | NUMBER |  |
| OPERATION | VARCHAR2(128) |  |
| BACKEDOUT | NUMBER |  |
| CONFLICT_MOD | NUMBER |  |
| MODS_PER_LCR | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

This view is relevant AFTER a compensating transaction has been started through the DBMS_FLASHBACK.TRANSACTION_BACKOUT() set of functions, and is no longer relevant once the compensating transaction is either committed or rolled back. It also provides a tabular representation of the undo SQL that is not available through the CLOB XML construct in the DBA_FLASHBACK_TXN_REPORT view. See Also: " DBA_FLASHBACK_TXN_REPORT " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_FLASHBACK.TRANSACTION_BACKOUT procedures See Also: " DBA_FLASHBACK_TXN_REPORT " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_FLASHBACK.TRANSACTION_BACKOUT procedures