---
id: 19c__V$WAIT_CHAINS
name: V$WAIT_CHAINS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-WAIT_CHAINS.html
---

# V$WAIT_CHAINS

CHAIN_ID

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CHAIN_ID | NUMBER |  |
| CHAIN_IS_CYCLE | VARCHAR2(5) |  |
| CHAIN_SIGNATURE | VARCHAR2(801) |  |
| CHAIN_SIGNATURE_HASH | NUMBER |  |
| INSTANCE | NUMBER |  |
| OSID | VARCHAR2(25) |  |
| PID | NUMBER |  |
| SID | NUMBER |  |
| SESS_SERIAL# | NUMBER |  |
| PDB_ID | NUMBER |  |
| PDB_NAME | VARCHAR2(31) |  |
| BLOCKER_IS_VALID | VARCHAR2(5) |  |
| BLOCKER_INSTANCE | NUMBER |  |
| BLOCKER_OSID | VARCHAR2(25) |  |
| BLOCKER_PID | NUMBER |  |
| BLOCKER_SID | NUMBER |  |
| BLOCKER_SESS_SERIAL# | NUMBER |  |
| BLOCKER_PDB_ID | NUMBER |  |
| BLOCKER_PDB_NAME | VARCHAR2(31) |  |
| BLOCKER_CHAIN_ID | NUMBER |  |
| IN_WAIT | VARCHAR2(5) |  |
| TIME_SINCE_LAST_WAIT_SECS | NUMBER |  |
| WAIT_ID | NUMBER |  |
| WAIT_EVENT | NUMBER |  |
| WAIT_EVENT_TEXT | VARCHAR2(64) |  |
| P1 | NUMBER |  |
| P1_TEXT | VARCHAR2(64) |  |
| P2 | NUMBER |  |
| P2_TEXT | VARCHAR2(64) |  |
| P3 | NUMBER |  |
| P3_TEXT | VARCHAR2(64) |  |
| IN_WAIT_SECS | NUMBER |  |
| TIME_REMAINING_SECS | NUMBER |  |
| NUM_WAITERS | NUMBER |  |
| ROW_WAIT_OBJ# | NUMBER |  |
| ROW_WAIT_FILE# | NUMBER |  |
| ROW_WAIT_BLOCK# | NUMBER |  |
| ROW_WAIT_ROW# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content