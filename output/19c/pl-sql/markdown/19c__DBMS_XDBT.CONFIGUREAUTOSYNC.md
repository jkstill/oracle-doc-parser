---
id: 19c__DBMS_XDBT.CONFIGUREAUTOSYNC
name: DBMS_XDBT.CONFIGUREAUTOSYNC
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CONFIGUREAUTOSYNC

This procedure sets up jobs for automatic SYNCs of the CONTEXT index.

## Syntax

```sql
DBMS_XDBT.CONFIGUREAUTOSYNC;
```

## Usage Notes

Syntax DBMS_XDBT.CONFIGUREAUTOSYNC; Usage Notes The system must be configured for job queues for automatic synchronization. The jobs can be viewed using the USER_JOBS catalog views The configuration parameter AutoSyncPolicy can be set to choose an appropriate synchronization policy. The synchronization can be based on one of the following: Sync Basis Description SYNC_BY_PENDING_COUNT The SYNC is triggered when the number of documents in the pending queue is greater than a threshold (See the MaxPendingCount configuration setting). The pending queue is polled at regular intervals (See the CheckPendingCountInterval configuration parameter) to determine if the number of documents exceeds the threshold. SYNC_BY_TIME The SYNC is triggered at regular intervals. (See the SyncInterval configuration parameter). SYNC_BY_PENDING_COUNT_AND_TIME A combination of both of the preceding options.