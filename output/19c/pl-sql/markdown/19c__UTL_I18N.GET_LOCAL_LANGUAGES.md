---
id: 19c__UTL_I18N.GET_LOCAL_LANGUAGES
name: UTL_I18N.GET_LOCAL_LANGUAGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_LOCAL_LANGUAGES

This function returns the local language names for the specified territory.

## Syntax

```sql
UTL_I18N.GET_LOCAL_LANGUAGES (
   territory    IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN STRING_ARRAY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| territory | VARCHAR2 | IN | Specifies a valid Oracle territory. It is case-insensitive. |

**Returns:** `STRING_ARRAY`

## Usage Notes

Syntax UTL_I18N.GET_LOCAL_LANGUAGES ( territory IN VARCHAR2 CHARACTER SET ANY_CS) RETURN STRING_ARRAY; Parameters Table 265-7 GET_LOCAL_LANGUAGES Function Parameters Parameter Description territory Specifies a valid Oracle territory. It is case-insensitive. Usage Notes If the user specifies an invalid territory name, then the function returns a NULL string. Examples Returns the list of local languages used in Belgium. DECLARE retval UTL_I18N.STRING_ARRAY; cnt INTEGER; BEGIN retval := UTL_I18N.GET_LOCAL_LANGUAGES('BELGIUM'); DBMS_OUTPUT.PUT('Count = '); DBMS_OUTPUT.PUT_LINE(retval.LAST); cnt := retval.FIRST; WHILE cnt IS NOT NULL LOOP DBMS_OUTPUT.PUT_LINE(retval(cnt)); cnt := retval.NEXT(cnt); END LOOP; END; / ... Count = 2 DUTCH FRENCH