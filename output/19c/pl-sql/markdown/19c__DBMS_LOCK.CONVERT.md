---
id: 19c__DBMS_LOCK.CONVERT
name: DBMS_LOCK.CONVERT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOCK
tags: [dbms_lock]
source_file: DBMS_LOCK.html
---

# DBMS_LOCK.CONVERT

This function converts a lock from one mode to another. CONVERT is an overloaded function that accepts either a user-defined lock identifier, or the lock handle returned by the ALLOCATE_UNIQUE procedure.

## Syntax

```sql
DBMS_LOCK.CONVERT(
   id         IN INTEGER || 
   lockhandle IN VARCHAR2,
   lockmode   IN INTEGER,
   timeout    IN NUMBER DEFAULT MAXWAIT)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| id or lockhandle |  |  | User assigned lock identifier, from 0 to 1073741823, or the lock handle, returned by ALLOCATE_UNIQUE , of the lock mode you want to change |
| lockmode | INTEGER | IN | New mode that you want to assign to the specified lock. For the available modes and their associated integer identifiers, see Constants . |
| timeout | NUMBER | IN | Number of seconds to continue trying to change the lock mode. If the lock cannot be converted within this time period, then the call returns a value of 1 (timeout). |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOCK.CONVERT( id IN INTEGER || lockhandle IN VARCHAR2, lockmode IN INTEGER, timeout IN NUMBER DEFAULT MAXWAIT) RETURN INTEGER; Parameters Table 100-6 CONVERT Function Parameters Parameter Description id or lockhandle User assigned lock identifier, from 0 to 1073741823, or the lock handle, returned by ALLOCATE_UNIQUE , of the lock mode you want to change lockmode New mode that you want to assign to the specified lock. For the available modes and their associated integer identifiers, see Constants . timeout Number of seconds to continue trying to change the lock mode. If the lock cannot be converted within this time period, then the call returns a value of 1 (timeout). Return Values Table 100-7 CONVERT Function Return Values Return Value Description 0 Success 1 Timeout 2 Deadlock 3 Parameter error 4 Don't own lock specified by id or lockhandle 5 Illegal lock handle