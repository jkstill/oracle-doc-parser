---
id: 19c__DBMS_MGWMSG.NVARRAY_GET
name: DBMS_MGWMSG.NVARRAY_GET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.NVARRAY_GET

This function gets the name-value element of the name you specify in p_name from a name-value array.

## Syntax

```sql
DBMS_MGWMSG.NVARRAY_GET (
   p_array    IN SYS.MGW_NAME_VALUE_ARRAY_T,
   p_name     IN VARCHAR2,
   p_compare  IN BINARY_INTEGER DEFAULT CASE_SENSITIVE )
RETURN SYS.MGW_NAME_VALUE_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_array | SYS.MGW_NAME_VALUE_ARRAY_T | IN | The name-value array |
| p_name | VARCHAR2 | IN | The value name |
| p_compare | BINARY_INTEGER | IN | Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . |

**Returns:** `SYS.MGW_NAME_VALUE_T`

## Usage Notes

Syntax DBMS_MGWMSG.NVARRAY_GET ( p_array IN SYS.MGW_NAME_VALUE_ARRAY_T, p_name IN VARCHAR2, p_compare IN BINARY_INTEGER DEFAULT CASE_SENSITIVE ) RETURN SYS.MGW_NAME_VALUE_T; Parameters Table 111-26 NVARRAY_GET Function Parameters Parameter Description p_array The name-value array p_name The value name p_compare Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . Return Values Returns the matching element, or NULL if the specified name is not found.