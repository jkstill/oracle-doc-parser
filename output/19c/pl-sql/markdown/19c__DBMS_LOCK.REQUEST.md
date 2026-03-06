---
id: 19c__DBMS_LOCK.REQUEST
name: DBMS_LOCK.REQUEST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOCK
tags: [dbms_lock]
source_file: DBMS_LOCK.html
---

# DBMS_LOCK.REQUEST

This function requests a lock with a specified mode.

## Syntax

```sql
DBMS_LOCK.REQUEST(
   id                 IN  INTEGER ||
   lockhandle         IN  VARCHAR2,
   lockmode           IN  INTEGER DEFAULT X_MODE,
   timeout            IN  INTEGER DEFAULT MAXWAIT,
   release_on_commit  IN  BOOLEAN DEFAULT FALSE)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| id or lockhandle |  |  | User assigned lock identifier, from 0 to 1073741823, or the lock handle, returned by ALLOCATE_UNIQUE , of the lock mode you want to change |
| lockmode | INTEGER | IN | Mode that you are requesting for the lock. For the available modes and their associated integer identifiers, see Constants . |
| timeout | INTEGER | IN | Number of seconds to continue trying to grant the lock. If the lock cannot be granted within this time period, then the call returns a value of 1 ( timeout ). |
| release_on_commit | BOOLEAN | IN | Set this parameter to TRUE to release the lock on commit or roll-back. Otherwise, the lock is held until it is explicitly released or until the end of the session. |

**Returns:** `INTEGER`

## Usage Notes

REQUEST is an overloaded function that accepts either a user-defined lock identifier, or the lock handle returned by the ALLOCATE_UNIQUE procedure. Syntax DBMS_LOCK.REQUEST( id IN INTEGER || lockhandle IN VARCHAR2, lockmode IN INTEGER DEFAULT X_MODE, timeout IN INTEGER DEFAULT MAXWAIT, release_on_commit IN BOOLEAN DEFAULT FALSE) RETURN INTEGER; The current default values, such as X_MODE and MAXWAIT , are defined in the DBMS_LOCK package specification. Parameters Table 100-10 REQUEST Function Parameters Parameter Description id or lockhandle User assigned lock identifier, from 0 to 1073741823, or the lock handle, returned by ALLOCATE_UNIQUE , of the lock mode you want to change lockmode Mode that you are requesting for the lock. For the available modes and their associated integer identifiers, see Constants . timeout Number of seconds to continue trying to grant the lock. If the lock cannot be granted within this time period, then the call returns a value of 1 ( timeout ). release_on_commit Set this parameter to TRUE to release the lock on commit or roll-back. Otherwise, the lock is held until it is explicitly released or until the end of the session. Return Values Table 100-11 REQUEST Function Return Values Return Value Description 0 Success 1 Timeout 2 Deadlock 3 Parameter error 4 Already own lock specified by id or lockhandle 5 Illegal lock handle