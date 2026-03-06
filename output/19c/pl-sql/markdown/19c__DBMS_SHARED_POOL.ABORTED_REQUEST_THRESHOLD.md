---
id: 19c__DBMS_SHARED_POOL.ABORTED_REQUEST_THRESHOLD
name: DBMS_SHARED_POOL.ABORTED_REQUEST_THRESHOLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SHARED_POOL
tags: [dbms_shared_pool]
source_file: DBMS_SHARED_POOL.html
---

# DBMS_SHARED_POOL.ABORTED_REQUEST_THRESHOLD

This procedure sets the aborted request threshold for the shared pool.

## Syntax

```sql
DBMS_SHARED_POOL.ABORTED_REQUEST_THRESHOLD (
   threshold_size NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| threshold_size | NUMBER) | IN | Size, in bytes, of a request which does not try to free unpinned (not "unkeep-ed") memory within the shared pool. The range of threshold_size is 5000 to ~2 GB inclusive. |

## Usage Notes

Syntax DBMS_SHARED_POOL.ABORTED_REQUEST_THRESHOLD ( threshold_size NUMBER); Parameters Table 157-2 ABORTED_REQUEST_THRESHOLD Procedure Parameters Parameter Description threshold_size Size, in bytes, of a request which does not try to free unpinned (not "unkeep-ed") memory within the shared pool. The range of threshold_size is 5000 to ~2 GB inclusive. Exceptions An exception is raised if the threshold is not in the valid range. Usage Notes Usually, if a request cannot be satisfied on the free list, then the RDBMS tries to reclaim memory by freeing objects from the LRU list and checking periodically to see if the request can be fulfilled. After finishing this step, the RDBMS has performed a near equivalent of an ' ALTER SYSTEM FLUSH SHARED_POOL '. Because this impacts all users on the system, this procedure "localizes" the impact to the process failing to find a piece of shared pool memory of size greater than thresh_hold size. This user gets the 'out of memory' error without attempting to search the LRU list.