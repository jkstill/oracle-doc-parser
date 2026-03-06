---
id: 19c__DBMS_REPAIR.ONLINE_INDEX_CLEAN
name: DBMS_REPAIR.ONLINE_INDEX_CLEAN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR.ONLINE_INDEX_CLEAN

This function performs a manual cleanup of failed or interrupted online index builds or rebuilds.

## Syntax

```sql
DBMS_REPAIR.ONLINE_INDEX_CLEAN (
   object_id      IN BINARY_INTEGER DEFAULT ALL_INDEX_ID,
   wait_for_lock  IN BINARY_INTEGER DEFAULT LOCK_WAIT)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_id | BINARY_INTEGER | IN | Object id of index to be cleaned up. The default cleans up all object ids that qualify. |
| wait_for_lock | BINARY_INTEGER | IN | This parameter specifies whether to try getting DML locks on underlying table [[sub]partition] object. The default retries up to an internal retry limit, after which the lock get will give up. If LOCK_NOWAIT is specified, then the lock get does not retry. |

**Returns:** `BOOLEAN`

## Usage Notes

This action is also performed periodically by SMON, regardless of user-initiated cleanup. This function returns TRUE if all indexes specified were cleaned up and FALSE if one or more indexes could not be cleaned up. Syntax DBMS_REPAIR.ONLINE_INDEX_CLEAN ( object_id IN BINARY_INTEGER DEFAULT ALL_INDEX_ID, wait_for_lock IN BINARY_INTEGER DEFAULT LOCK_WAIT) RETURN BOOLEAN; Parameters Table 140-8 ONLINE_INDEX_CLEAN Function Parameters Parameter Description object_id Object id of index to be cleaned up. The default cleans up all object ids that qualify. wait_for_lock This parameter specifies whether to try getting DML locks on underlying table [[sub]partition] object. The default retries up to an internal retry limit, after which the lock get will give up. If LOCK_NOWAIT is specified, then the lock get does not retry.