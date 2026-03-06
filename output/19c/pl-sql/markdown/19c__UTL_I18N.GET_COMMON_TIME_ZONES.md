---
id: 19c__UTL_I18N.GET_COMMON_TIME_ZONES
name: UTL_I18N.GET_COMMON_TIME_ZONES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_COMMON_TIME_ZONES

This function returns a listing of the most coemmonly used time zones. This list contains a subset of the time zones that are supported in the database.

## Syntax

```sql
UTL_I18N.GET_COMMON_TIME_ZONES
 RETURN STRING_ARRAY;
```

**Returns:** `STRING_ARRAY`

## Usage Notes

Syntax UTL_I18N.GET_COMMON_TIME_ZONES RETURN STRING_ARRAY; Examples Returns the list of the most commonly used time zones. DECLARE retval UTL_I18N.STRING_ARRAY; BEGIN retval := UTL_I18N.GET_COMMON_TIME_ZONES; END; /