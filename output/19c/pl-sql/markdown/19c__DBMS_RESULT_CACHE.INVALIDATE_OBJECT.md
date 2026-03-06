---
id: 19c__DBMS_RESULT_CACHE.INVALIDATE_OBJECT
name: DBMS_RESULT_CACHE.INVALIDATE_OBJECT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESULT_CACHE
tags: [dbms_result_cache]
source_file: DBMS_RESULT_CACHE.html
---

# DBMS_RESULT_CACHE.INVALIDATE_OBJECT

This function and procedure invalidates the specified result-set object(s).

## Syntax

```sql
DBMS_RESULT_CACHE.INVALIDATE_OBJECT (
   id          IN  BINARY_INTEGER) 
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| id | BINARY_INTEGER) | IN | Address of the cache object in the Result Cache |
| cache_id |  |  | Result cache identifier of a SQL cursor or PL/SQL function. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_RESULT_CACHE.INVALIDATE_OBJECT ( id IN BINARY_INTEGER) RETURN NUMBER; DBMS_RESULT_CACHE.INVALIDATE_OBJECT ( id IN BINARY_INTEGER); DBMS_RESULT_CACHE.INVALIDATE_OBJECT ( cache_id IN VARCHAR2) RETURN NUMBER; DBMS_RESULT_CACHE.INVALIDATE_OBJECT ( cache_id IN VARCHAR2); Parameters Table 144-9 INVALIDATE_OBJECT Function & Procedure Parameters Parameter Description id Address of the cache object in the Result Cache cache_id Result cache identifier of a SQL cursor or PL/SQL function. Return Values The number of objects invalidated.