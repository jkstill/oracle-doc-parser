---
id: 19c__DBMS_MGWMSG.NVARRAY_GET_DATE
name: DBMS_MGWMSG.NVARRAY_GET_DATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG.NVARRAY_GET_DATE

This function gets the value of the name-value array element that you specify in p_name and with the DATE_VALUE value type .

## Syntax

```sql
DBMS_MGWMSG.NVARRAY_GET_DATE (
   p_array    IN SYS.MGW_NAME_VALUE_ARRAY_T,
   p_name     IN VARCHAR2,
   p_compare  IN BINARY_INTEGER DEFAULT CASE_SENSITIVE )
RETURN DATE;
```

**Returns:** `DATE`

## Usage Notes

Syntax DBMS_MGWMSG.NVARRAY_GET_DATE ( p_array IN SYS.MGW_NAME_VALUE_ARRAY_T, p_name IN VARCHAR2, p_compare IN BINARY_INTEGER DEFAULT CASE_SENSITIVE ) RETURN DATE; Parameters Table 111-29 NVARRAY_GET_DATE Function Parameters Parameters Description p_array The name-value array p_name The value name p_compare Name comparison method. Values are CASE_SENSITIVE and CASE_INSENSITIVE . Return Values Returns the value, or NULL if either the specified name is not found or a type mismatch exists.