---
id: 19c__DBMS_SHARED_POOL.SIZES
name: DBMS_SHARED_POOL.SIZES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SHARED_POOL
tags: [dbms_shared_pool]
source_file: DBMS_SHARED_POOL.html
---

# DBMS_SHARED_POOL.SIZES

This procedure shows objects in the shared_pool that are larger than the specified size. The name of the object is also given, which can be used as an argument to either the KEEP or UNKEEP calls.

## Syntax

```sql
DBMS_SHARED_POOL.SIZES ( 
   minsize NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| minsize | NUMBER) | IN | Size, in kilobytes, over which an object must be occupying in the shared pool, in order for it to be displayed. |

## Usage Notes

Syntax DBMS_SHARED_POOL.SIZES ( minsize NUMBER); Parameters Table 157-6 SIZES Procedure Parameters Parameter Description minsize Size, in kilobytes, over which an object must be occupying in the shared pool, in order for it to be displayed. Usage Notes Issue the SQLDBA or SQLPLUS 'SET SERVEROUTPUT ON SIZE XXXXX' command prior to using this procedure so that the results are displayed.