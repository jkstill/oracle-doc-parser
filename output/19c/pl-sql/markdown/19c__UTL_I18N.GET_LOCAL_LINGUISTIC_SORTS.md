---
id: 19c__UTL_I18N.GET_LOCAL_LINGUISTIC_SORTS
name: UTL_I18N.GET_LOCAL_LINGUISTIC_SORTS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_LOCAL_LINGUISTIC_SORTS

This function returns a list of the Oracle linguistic sort names that are appropriate for the specified language. A BINARY sort is included for all languages.

## Syntax

```sql
UTL_I18N.GET_LOCAL_LINGUISTIC_SORTS (
   language  IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN STRING_ARRAY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| language | VARCHAR2 | IN | Specifies a valid Oracle language. It is case-insensitive. |

**Returns:** `STRING_ARRAY`

## Usage Notes

Syntax UTL_I18N.GET_LOCAL_LINGUISTIC_SORTS ( language IN VARCHAR2 CHARACTER SET ANY_CS) RETURN STRING_ARRAY; Parameters Table 265-8 GET_LOCAL_LINGUISTIC_SORTS Function Parameters Parameter Description language Specifies a valid Oracle language. It is case-insensitive. Usage Notes If the user specifies an invalid language name, then the function returns a NULL string. Examples Displays the local linguistic sort names for JAPANESE . DECLARE retval UTL_I18N.STRING_ARRAY; cnt INTEGER; BEGIN retval := UTL_I18N.GET_LOCAL_LINGUISTIC_SORTS('Japanese'); DBMS_OUTPUT.PUT('Count = '); DBMS_OUTPUT.PUT_LINE(retval.COUNT); cnt := retval.FIRST; WHILE cnt IS NOT NULL LOOP DBMS_OUTPUT.PUT_LINE(retval(cnt)); cnt := retval.NEXT(cnt); END LOOP; END; / ... Count = 2 JAPANESE_M BINARY