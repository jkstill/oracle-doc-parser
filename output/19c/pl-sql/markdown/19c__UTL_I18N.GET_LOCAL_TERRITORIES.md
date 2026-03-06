---
id: 19c__UTL_I18N.GET_LOCAL_TERRITORIES
name: UTL_I18N.GET_LOCAL_TERRITORIES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_LOCAL_TERRITORIES

This function returns the local territory names for the specified language.

## Syntax

```sql
UTL_I18N.GET_LOCAL_TERRITORIES (
   language  IN VARCHAR2 CHARACTER SET ANY_CS)
 RETURN STRING_ARRAY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| language | VARCHAR2 | IN | Specifies a valid Oracle language. It is case-insensitive. |

**Returns:** `STRING_ARRAY`

## Usage Notes

Syntax UTL_I18N.GET_LOCAL_TERRITORIES ( language IN VARCHAR2 CHARACTER SET ANY_CS) RETURN STRING_ARRAY; Parameters Table 265-9 GET_LOCAL_TERRITORIES Function Parameters Parameter Description language Specifies a valid Oracle language. It is case-insensitive. Usage Notes If the user specifies an invalid language name, then the function returns a NULL string. Examples Returns the list of Oracle territories that use German as one of their local languages. DECLARE retval UTL_I18N.STRING_ARRAY; cnt INTEGER; BEGIN retval := UTL_I18N.GET_LCOAL_TERRITORIIES('GERMAN'); DBMS_OUTPUT.PUT('Count = '); DBMS_OUTPUT.PUT_LINE(retval.LAST); cnt := retval.FIRST; WHILE cnt IS NOT NULL LOOP DBMS_OUTPUT.PUT_LINE(retval(cnt)); cnt := retval.NEXT(cnt)); END LOOP; END; / ... Count = 4 GERMANY AUSTRIA LUXEMBOURG SWITZERLAND