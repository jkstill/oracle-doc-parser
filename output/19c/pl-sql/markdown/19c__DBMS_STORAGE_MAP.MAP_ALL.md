---
id: 19c__DBMS_STORAGE_MAP.MAP_ALL
name: DBMS_STORAGE_MAP.MAP_ALL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.MAP_ALL

This function builds the entire mapping information for all types of Oracle files (except archive logs), including all directed acyclic graph (DAG) elements. It obtains the latest mapping information because it explicitly synchronizes all mapping libraries.

## Syntax

```sql
DBMS_STORAGE_MAP.MAP_ALL(
   max_num_fileext   IN NUMBER DEFAULT 100,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| max_num_fileext | NUMBER | IN | Defines the maximum number of file extents to be mapped. This limits the amount of memory used when mapping file extents. The default value is 100 ; max_num_fileextent is an overloaded argument. |
| dictionary_update | BOOLEAN | IN | If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_STORAGE_MAP.MAP_ALL( max_num_fileext IN NUMBER DEFAULT 100, dictionary_update IN BOOLEAN DEFAULT TRUE); Parameters Table 172-5 MAP_ALL Function Parameters Parameter Description max_num_fileext Defines the maximum number of file extents to be mapped. This limits the amount of memory used when mapping file extents. The default value is 100 ; max_num_fileextent is an overloaded argument. dictionary_update If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. Usage Notes You must explicitly call MAP_ALL in a cold startup scenario.