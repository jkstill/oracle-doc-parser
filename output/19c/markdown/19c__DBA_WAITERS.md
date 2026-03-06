---
id: 19c__DBA_WAITERS
name: DBA_WAITERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_WAITERS.html
---

# DBA_WAITERS

DBA_WAITERS shows all the sessions that are waiting for a lock. In an Oracle RAC environment, this only applies if the waiter is on the same instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WAITING_SESSION | NUMBER | The waiting session |
| WAITING_CON_ID | NUMBER | The container ID ( CON_ID ) of the waiting session |
| HOLDING_SESSION | NUMBER | The holding session |
| HOLDING_CON_ID | NUMBER | The container ID ( CON_ID ) of the holding session. |
| LOCK_TYPE | VARCHAR2(26) | The lock type |
| MODE_HELD | VARCHAR2(40) | The mode held |
| MODE_REQUESTED | VARCHAR2(40) | The mode requested |
| LOCK_ID1 | NUMBER | Lock ID 1 |
| LOCK_ID2 | NUMBER | Lock ID 2 |