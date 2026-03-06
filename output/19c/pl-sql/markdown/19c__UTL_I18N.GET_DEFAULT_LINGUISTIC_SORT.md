---
id: 19c__UTL_I18N.GET_DEFAULT_LINGUISTIC_SORT
name: UTL_I18N.GET_DEFAULT_LINGUISTIC_SORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_DEFAULT_LINGUISTIC_SORT

This function returns the most commonly used Oracle linguistic sort for the specified language.

## Syntax

```sql
UTL_I18N.GET_DEFAULT_LINGUISTIC_SORT (
   language  IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| language | VARCHAR2 | IN | Specifies a valid Oracle language. It is case-insensitive. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_I18N.GET_DEFAULT_LINGUISTIC_SORT ( language IN VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2; Parameters Table 265-6 GET_DEFAULT_LINGUISTIC_SORT Function Parameters Parameter Description language Specifies a valid Oracle language. It is case-insensitive. Usage Notes If the user specifies an invalid language name, then the function returns a NULL string. Examples Displays the name of the most appropriate linguistic sort name for the language used in the current SQL session. DECLARE retval VARCHAR2(50); BEGIN SELECT value INTO retval FROM nls_database_parameters WHERE parameter = 'NLS_LANGUAGE'; retval := UTL_I18N.GET_DEFAULT_LINGUISTIC_SORT(retval); DBMS_OUTPUT.PUT_LINE(retval); END; /