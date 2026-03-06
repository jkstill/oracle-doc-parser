---
id: 19c__DBMS_STORAGE_MAP.MAP_OBJECT
name: DBMS_STORAGE_MAP.MAP_OBJECT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.MAP_OBJECT

This function builds the mapping information for the Oracle object identified by the object name, owner, and type.

## Syntax

```sql
DBMS_STORAGE_MAP.MAP_OBJECT(
   objname  IN  VARCHAR2,
   owner    IN  VARCHAR2,
   objtype  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| objname | VARCHAR2 | IN | The name of the object. |
| owner | VARCHAR2 | IN | The owner of the object. |
| objtype | VARCHAR2) | IN | The type of the object. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_STORAGE_MAP.MAP_OBJECT( objname IN VARCHAR2, owner IN VARCHAR2, objtype IN VARCHAR2); Parameters Table 172-8 MAP_OBJECT Function Parameters Parameter Description objname The name of the object. owner The owner of the object. objtype The type of the object.