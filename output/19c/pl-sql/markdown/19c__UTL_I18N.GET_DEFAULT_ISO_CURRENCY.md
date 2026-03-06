---
id: 19c__UTL_I18N.GET_DEFAULT_ISO_CURRENCY
name: UTL_I18N.GET_DEFAULT_ISO_CURRENCY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_DEFAULT_ISO_CURRENCY

This function returns the default ISO 4217 currency code for the specified territory.

## Syntax

```sql
UTL_I18N.GET_DEFAULT_ISO_CURRENCY (
   territory    IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| territory | VARCHAR2 | IN | Specifies a valid Oracle territory. It is case-insensitive. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_I18N.GET_DEFAULT_ISO_CURRENCY ( territory IN VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2; Parameters Table 265-5 GET_DEFAULT_ISO_CURRENCY Function Parameters Parameter Description territory Specifies a valid Oracle territory. It is case-insensitive. Usage Notes If the user specifies an invalid territory name, then the function returns a NULL string. Examples Displays the default ISO currency code for China. DECLARE retval VARCHAR2(50); BEGIN retval := UTL_I18N.GET_DEFAULT_ISO_CURRENCY('CHINA'); DBMS_OUTPUT.PUT_LINE(retval); END; /