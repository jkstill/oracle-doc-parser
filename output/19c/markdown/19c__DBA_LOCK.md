---
id: 19c__DBA_LOCK
name: DBA_LOCK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_LOCK.html
---

# DBA_LOCK

DBA_LOCK lists all locks or latches held in the database, and all outstanding requests for a lock or latch.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER | Session holding or acquiring the lock |
| LOCK_TYPE | VARCHAR2(26) | Lock type See Also: For a listing of lock types, see Oracle Enqueue Names |
| MODE HELD | VARCHAR2(40) | Lock mode |
| MODE REQUESTED | VARCHAR2(40) | Lock mode requested |
| LOCK_ID1 | VARCHAR2(40) | Type-specific lock identifier, part 1 |
| LOCK_ID2 | VARCHAR2(40) | Type-specific lock identifier, part 2 |
| LAST_CONVERT | NUMBER | The last convert |
| BLOCKING_OTHERS | VARCHAR2(40) | Whether the lock is currently blocking others |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |