---
id: 19c__DBMS_LOCK.RELEASE
name: DBMS_LOCK.RELEASE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOCK
tags: [dbms_lock]
source_file: DBMS_LOCK.html
---

# DBMS_LOCK.RELEASE

This function explicitly releases a lock previously acquired using the REQUEST function.

## Syntax

```sql
DBMS_LOCK.RELEASE (
   id         IN INTEGER)
  RETURN INTEGER;

DBMS_LOCK.RELEASE (
   lockhandle IN VARCHAR2)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| id or lockhandle |  |  | User assigned lock identifier, from 0 to 1073741823, or the lock handle, returned by ALLOCATE_UNIQUE , of the lock mode you want to change |

**Returns:** `INTEGER`

## Usage Notes

Locks are automatically released at the end of a session. RELEASE is an overloaded function that accepts either a user-defined lock identifier, or the lock handle returned by the ALLOCATE_UNIQUE procedure. Syntax DBMS_LOCK.RELEASE ( id IN INTEGER) RETURN INTEGER; DBMS_LOCK.RELEASE ( lockhandle IN VARCHAR2) RETURN INTEGER; Parameters Table 100-8 RELEASE Function Parameter Parameter Description id or lockhandle User assigned lock identifier, from 0 to 1073741823, or the lock handle, returned by ALLOCATE_UNIQUE , of the lock mode you want to change Return Values Table 100-9 RELEASE Function Return Values Return Value Description 0 Success 3 Parameter error 4 Do not own lock specified by id or lockhandle 5 Illegal lock handle