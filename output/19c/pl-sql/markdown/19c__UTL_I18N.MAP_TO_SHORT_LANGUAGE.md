---
id: 19c__UTL_I18N.MAP_TO_SHORT_LANGUAGE
name: UTL_I18N.MAP_TO_SHORT_LANGUAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.MAP_TO_SHORT_LANGUAGE

This function maps an Oracle language name to an Oracle short language name.

## Syntax

```sql
UTL_I18N.MAP_TO_SHORT_LANGUAGE (
   language    IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| language | VARCHAR2 | IN | Specifies a valid full language name. It is case-insensitive. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_I18N.MAP_TO_SHORT_LANGUAGE ( language IN VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2; Parameters Table 265-18 MAP_TO_SHORT_LANGUAGE Function Parameters Parameter Description language Specifies a valid full language name. It is case-insensitive. Usage Notes If the user specifies an invalid language name, then the function returns a NULL string. Examples Returns the short language name for the language. DECLARE retval VARCHAR2(100);BEGIN retval := UTL_I18N.MAP_TO_SHORT_LANGUAGE('american'); DBMS_OUTPUT.PUT_LINE(retval);END;/US