---
id: 19c__UTL_I18N.MAP_LOCALE_TO_ISO
name: UTL_I18N.MAP_LOCALE_TO_ISO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.MAP_LOCALE_TO_ISO

This function returns an ISO locale name from an Oracle language name and an Oracle territory name.

## Syntax

```sql
UTL_I18N.MAP_LOCALE_TO_ISO ( 
   ora_language   IN VARCHAR2,
   ora_territory  IN VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ora_language | VARCHAR2 | IN | Specifies an Oracle language name. It is case-insensitive. |
| ora_territory | VARCHAR2) | IN | Specifies an Oracle territory name. It is case-insensitive. |

**Returns:** `VARCHAR2`

## Usage Notes

A valid string must include at least one of the following: a valid Oracle language name or a valid Oracle territory name. Syntax UTL_I18N.MAP_LOCALE_TO_ISO ( ora_language IN VARCHAR2, ora_territory IN VARCHAR2) RETURN VARCHAR2; Parameters Table 265-16 MAP_LOCALE_TO_ISO Function Parameters Parameter Description ora_language Specifies an Oracle language name. It is case-insensitive. ora_territory Specifies an Oracle territory name. It is case-insensitive. Usage Notes If the user specifies an invalid string, then the function returns a NULL string. Examples UTL_I18N.MAP_LOCALE_TO_ISO('American','America') This returns 'en_US' . See Also: Oracle Database Globalization Support Guide for a list of valid Oracle languages and territories