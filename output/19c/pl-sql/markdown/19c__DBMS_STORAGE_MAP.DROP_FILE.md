---
id: 19c__DBMS_STORAGE_MAP.DROP_FILE
name: DBMS_STORAGE_MAP.DROP_FILE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.DROP_FILE

This function drops the file mapping information defined by filename .

## Syntax

```sql
DBMS_STORAGE_MAP.DROP_FILE(
   filename          IN VARCHAR2,
   cascade           IN BOOLEAN,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| filename | VARCHAR2 | IN | The file for which file mapping information is dropped. |
| cascade | BOOLEAN | IN | If TRUE , then the mapping DAGs for the elements where the file resides are also dropped, if possible. |
| dictionary_update | BOOLEAN | IN | If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_STORAGE_MAP.DROP_FILE( filename IN VARCHAR2, cascade IN BOOLEAN, dictionary_update IN BOOLEAN DEFAULT TRUE); Parameters Table 172-4 DROP_FILE Function Parameters Parameter Description filename The file for which file mapping information is dropped. cascade If TRUE , then the mapping DAGs for the elements where the file resides are also dropped, if possible. dictionary_update If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument.