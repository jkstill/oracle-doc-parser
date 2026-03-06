---
id: 19c__DBMS_WARNING.GET_WARNING_SETTING_STRING
name: DBMS_WARNING.GET_WARNING_SETTING_STRING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WARNING
tags: [dbms_warning]
source_file: DBMS_WARNING.html
---

# DBMS_WARNING.GET_WARNING_SETTING_STRING

This function returns the entire warning string for the current session.

## Syntax

```sql
DBMS_WARNING.GET_WARNING_SETTING_STRING
 RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_WARNING.GET_WARNING_SETTING_STRING RETURN VARCHAR2; Usage Notes Use this function when you do not have SELECT or READ privilege on v$parameter or v$paramater2 fixed tables, or if you want to parse the warning string yourself and then modify and set the new value using SET_WARNING_SETTING_STRING .