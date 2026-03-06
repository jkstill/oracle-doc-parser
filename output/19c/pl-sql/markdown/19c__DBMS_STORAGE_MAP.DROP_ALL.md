---
id: 19c__DBMS_STORAGE_MAP.DROP_ALL
name: DBMS_STORAGE_MAP.DROP_ALL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.DROP_ALL

This function drops all mapping information in the shared memory of the instance.

## Syntax

```sql
DBMS_STORAGE_MAP.DROP_ALL(
      dictionary_update IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dictionary_update | BOOLEAN | IN | If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_STORAGE_MAP.DROP_ALL( dictionary_update IN BOOLEAN DEFAULT TRUE); Parameters Table 172-2 DROP_ALL Function Parameters Parameter Description dictionary_update If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument.