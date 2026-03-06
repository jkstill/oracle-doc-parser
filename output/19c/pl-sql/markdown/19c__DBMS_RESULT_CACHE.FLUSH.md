---
id: 19c__DBMS_RESULT_CACHE.FLUSH
name: DBMS_RESULT_CACHE.FLUSH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESULT_CACHE
tags: [dbms_result_cache]
source_file: DBMS_RESULT_CACHE.html
---

# DBMS_RESULT_CACHE.FLUSH

This function and procedure attempts to remove all the objects from the Result Cache, and depending on the arguments retains or releases the memory and retains or clears the statistics.

## Syntax

```sql
DBMS_RESULT_CACHE.FLUSH (
   retainMem  IN  BOOLEAN DEFAULT FALSE,
   retainSta  IN  BOOLEAN DEFAULT FALSE) 
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| retainMem | BOOLEAN | IN | TRUE => retains the free memory in the cache FALSE (default) => releases the free memory to the system |
| retainSta | BOOLEAN | IN | TRUE => retains the existing cache statistics FALSE (default) => clears the existing cache statistics |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_RESULT_CACHE.FLUSH ( retainMem IN BOOLEAN DEFAULT FALSE, retainSta IN BOOLEAN DEFAULT FALSE) RETURN BOOLEAN; DBMS_RESULT_CACHE.FLUSH ( retainMem IN BOOLEAN DEFAULT FALSE, retainSta IN BOOLEAN DEFAULT FALSE); Parameters Table 144-7 FLUSH Function & Procedure Parameters Parameter Description retainMem TRUE => retains the free memory in the cache FALSE (default) => releases the free memory to the system retainSta TRUE => retains the existing cache statistics FALSE (default) => clears the existing cache statistics Return Values TRUE if successful in removing all the objects.