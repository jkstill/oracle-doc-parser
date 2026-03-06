---
id: 19c__DBMS_STORAGE_MAP.DROP_ELEMENT
name: DBMS_STORAGE_MAP.DROP_ELEMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.DROP_ELEMENT

This function drops the mapping information for the element defined by elemname .

## Syntax

```sql
DBMS_STORAGE_MAP.DROP_ELEMENT(
   elemname          IN VARCHAR2,
   cascade           IN BOOLEAN,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elemname | VARCHAR2 | IN | The element for which mapping information is dropped. |
| cascade | BOOLEAN | IN | If TRUE , then DROP_ELEMENT is invoked recursively on all elements of the DAG defined by elemname, if possible. |
| dictionary_update | BOOLEAN | IN | If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_STORAGE_MAP.DROP_ELEMENT( elemname IN VARCHAR2, cascade IN BOOLEAN, dictionary_update IN BOOLEAN DEFAULT TRUE); Parameters Table 172-3 DROP_ELEMENT Function Parameters Parameter Description elemname The element for which mapping information is dropped. cascade If TRUE , then DROP_ELEMENT is invoked recursively on all elements of the DAG defined by elemname, if possible. dictionary_update If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument.