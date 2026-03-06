---
id: 19c__DBMS_STORAGE_MAP.MAP_ELEMENT
name: DBMS_STORAGE_MAP.MAP_ELEMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STORAGE_MAP
tags: [dbms_storage_map]
source_file: DBMS_STORAGE_MAP.html
---

# DBMS_STORAGE_MAP.MAP_ELEMENT

This function builds mapping information for the element identified by elemname . It may not obtain the latest mapping information if the element being mapped, or any one of the elements within its I/O stack (if cascade is TRUE ), is owned by a library that must be explicitly synchronized.

## Syntax

```sql
DBMS_STORAGE_MAP.MAP_ELEMENT(
   elemname          IN VARCHAR2,
   cascade           IN BOOLEAN,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elemname | VARCHAR2 | IN | The element for which mapping information is built. |
| cascade | BOOLEAN | IN | If TRUE , all elements within the elemname I/O stack DAG are mapped. |
| dictionary_update | BOOLEAN | IN | If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_STORAGE_MAP.MAP_ELEMENT( elemname IN VARCHAR2, cascade IN BOOLEAN, dictionary_update IN BOOLEAN DEFAULT TRUE); Parameters Table 172-6 MAP_ELEMENT Function Parameters Parameter Description elemname The element for which mapping information is built. cascade If TRUE , all elements within the elemname I/O stack DAG are mapped. dictionary_update If TRUE , mapping information in the data dictionary is updated to reflect the changes. The default value is TRUE ; dictionary_update is an overloaded argument.