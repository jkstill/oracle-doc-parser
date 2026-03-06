---
id: 19c__V$LOGSTDBY_TRANSACTION
name: V$LOGSTDBY_TRANSACTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGSTDBY_TRANSACTION.html
---

# V$LOGSTDBY_TRANSACTION

V$LOGSTDBY_TRANSACTION displays all transactions that are actively being processed by SQL Apply.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PRIMARY_XIDUSN | NUMBER |  |
| PRIMARY_XIDSLT | NUMBER |  |
| PRIMARY_XIDSQN | NUMBER |  |
| PRIMARY_XID | RAW(8) |  |
| PRIMARY_START_SCN | NUMBER |  |
| PRIMARY_START_TIME | DATE |  |
| PRIMARY_PARENT_XIDUSN | NUMBER |  |
| PRIMARY_PARENT_XIDSLT | NUMBER |  |
| PRIMARY_PARENT_XIDSQN | NUMBER |  |
| PRIMARY_PARENT_XID | RAW(8) |  |
| TYPE | VARCHAR2(32) |  |
| MINING_STATUS | VARCHAR2(32) |  |
| SRC_CON_ID | NUMBER |  |
| APPLY_STATUS | VARCHAR2(6) |  |
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The transaction identifiers shown in this view are those mined from the redo stream and correspond to transaction identifiers assigned at the primary database, and do not correspond to the transactions that are active at the logical standby database. For information regarding transactions active in the logical standby database, including those created as part of SQL Apply, query the V$TRANSACTION view at the logical standby database. See Also: " V$TRANSACTION " See Also: " V$TRANSACTION "