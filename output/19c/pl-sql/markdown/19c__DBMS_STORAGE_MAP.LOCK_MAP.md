---
id: 19c__DBMS_STORAGE_MAP.LOCK_MAP
name: DBMS_STORAGE_MAP.LOCK_MAP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.LOCK_MAP

This procedure locks the mapping information in the shared memory of the instance.

## Syntax

```sql
DBMS_STORAGE_MAP.LOCK_MAP;
```

## Usage Notes

This is useful when you need a consistent snapshot of the V$MAP tables. Without locking the mapping information, V$MAP_ELEMENT and V$MAP_SUBELEMENT , for example, may be inconsistent. Syntax DBMS_STORAGE_MAP.LOCK_MAP;