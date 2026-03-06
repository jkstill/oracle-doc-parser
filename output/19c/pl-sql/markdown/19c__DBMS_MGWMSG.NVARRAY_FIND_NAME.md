---
id: 19c__DBMS_MGWMSG.NVARRAY_FIND_NAME
name: DBMS_MGWMSG.NVARRAY_FIND_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.NVARRAY_FIND_NAME

This function searches a name-value array for the element with the name you specify in p_name .

## Syntax

```sql
DBMS_MGWMSG.NVARRAY_FIND_NAME (
   p_array    IN SYS.MGW_NAME_VALUE_ARRAY_T,
   p_name     IN VARCHAR2,
   p_compare  IN BINARY_INTEGER DEFAULT CASE_SENSITIVE )
RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_MGWMSG.NVARRAY_FIND_NAME ( p_array IN SYS.MGW_NAME_VALUE_ARRAY_T, p_name IN VARCHAR2, p_compare IN BINARY_INTEGER DEFAULT CASE_SENSITIVE ) RETURN BINARY_INTEGER; Parameters Table 111-24 NVARRAY_FIND_NAME Function Parameters Parameters Description p_array The name-value array to search p_name The name to find p_compare Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . Return Values Returns a positive integer that is the array index of the matching element or zero ( 0) if the specified name is not found.