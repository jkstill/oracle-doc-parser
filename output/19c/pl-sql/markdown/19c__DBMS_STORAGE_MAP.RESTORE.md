---
id: 19c__DBMS_STORAGE_MAP.RESTORE
name: DBMS_STORAGE_MAP.RESTORE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.RESTORE

This function loads the entire mapping information from the data dictionary into the shared memory of the instance.

## Syntax

```sql
DBMS_STORAGE_MAP.RESTORE;
```

**Returns:** `UNKNOWN`

## Usage Notes

You can invoke RESTORE only after a SAVE operation. You must explicitly call RESTORE in a warm startup scenario. Syntax DBMS_STORAGE_MAP.RESTORE;