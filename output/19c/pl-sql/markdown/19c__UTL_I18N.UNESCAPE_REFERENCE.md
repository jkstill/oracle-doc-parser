---
id: 19c__UTL_I18N.UNESCAPE_REFERENCE
name: UTL_I18N.UNESCAPE_REFERENCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.UNESCAPE_REFERENCE

This function returns a string from an input string that contains character references. It decodes each character reference to the corresponding character value.

## Syntax

```sql
UTL_I18N.UNESCAPE_REFERENCE ( 
   str IN VARCHAR2 CHARACTER SET ANY_CS)
 RETURN VARCHAR2 CHARACTER SET str%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | Specifies the input string |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: " ESCAPE_REFERENCE Function " for more information about escape sequences See Also: " ESCAPE_REFERENCE Function " for more information about escape sequences Syntax UTL_I18N.UNESCAPE_REFERENCE ( str IN VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2 CHARACTER SET str%CHARSET; Parameters Table 265-24 UNESCAPE_REFERENCE Function Parameters Parameter Description str Specifies the input string Usage Notes If the user specifies a NULL string or a string whose length is 0, then the function returns a NULL string. If the function fails, then it returns the original string.