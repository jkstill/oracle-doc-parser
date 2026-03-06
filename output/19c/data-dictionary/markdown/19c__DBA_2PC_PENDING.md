---
id: 19c__DBA_2PC_PENDING
name: DBA_2PC_PENDING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_2PC_PENDING.html
---

# DBA_2PC_PENDING

DBA_2PC_PENDING describes distributed transactions awaiting recovery.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOCAL_TRAN_ID | VARCHAR2(22) | String of form: n.n.n; n is a number |
| GLOBAL_TRAN_ID | VARCHAR2(169) | Globally unique transaction ID |
| STATE | VARCHAR2(16) | Collecting, prepared, committed, forced commit, or forced rollback |
| MIXED | VARCHAR2(3) | YES indicates part of the transaction committed and part rolled back |
| ADVICE | VARCHAR2(1) | C for commit, R for rollback, else NULL |
| TRAN_COMMENT | VARCHAR2(255) | Text for commit work comment text |
| FAIL_TIME | DATE | Value of SYSDATE when the row was inserted (transaction or system recovery) |
| FORCE_TIME | DATE | Time of manual force decision (null if not forced locally) |
| RETRY_TIME | DATE | Time automatic recovery ( RECO ) last tried to recover the transaction |
| OS_USER | VARCHAR2(64) | Operating system-specific name for the end-user |
| OS_TERMINAL | VARCHAR2(255) | Operating system-specific name for the end-user terminal |
| HOST | VARCHAR2(128) | Name of the host system for the end-user |
| DB_USER | VARCHAR2(128) | Oracle user name of the end-user at the topmost database |
| COMMIT# | VARCHAR2(16) | Global commit number for committed transactions |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content