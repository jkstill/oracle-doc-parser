---
id: 19c__DBMS_RESULT_CACHE.INVALIDATE
name: DBMS_RESULT_CACHE.INVALIDATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESULT_CACHE
tags: [dbms_result_cache]
source_file: DBMS_RESULT_CACHE.html
---

# DBMS_RESULT_CACHE.INVALIDATE

This function and procedure invalidates all the result-set objects that dependent upon the specified dependency object.

## Syntax

```sql
DBMS_RESULT_CACHE.INVALIDATE (
   owner        IN  VARCHAR2, 
   name         IN  VARCHAR2) 
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Schema name |
| name | VARCHAR2) | IN | Object name |
| object_id |  |  | Dictionary object number |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_RESULT_CACHE.INVALIDATE ( owner IN VARCHAR2, name IN VARCHAR2) RETURN NUMBER; DBMS_RESULT_CACHE.INVALIDATE ( owner IN VARCHAR2, name IN VARCHAR2); DBMS_RESULT_CACHE.INVALIDATE ( object_id IN BINARY_INTEGER) RETURN NUMBER; DBMS_RESULT_CACHE.INVALIDATE ( object_id IN BINARY_INTEGER); Parameters Table 144-8 INVALIDATE Function & Procedure Parameters Parameter Description owner Schema name name Object name object_id Dictionary object number Return Values The number of objects invalidated.