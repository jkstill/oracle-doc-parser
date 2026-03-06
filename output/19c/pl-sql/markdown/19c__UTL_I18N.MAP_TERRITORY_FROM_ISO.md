---
id: 19c__UTL_I18N.MAP_TERRITORY_FROM_ISO
name: UTL_I18N.MAP_TERRITORY_FROM_ISO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.MAP_TERRITORY_FROM_ISO

This function returns an Oracle territory name from an ISO locale.

## Syntax

```sql
UTL_I18N.MAP_TERRITORY_FROM_ISO (
  isolocale IN VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| isolocale | VARCHAR2) | IN | Specifies the ISO locale. The mapping is case-insensitive. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_I18N.MAP_TERRITORY_FROM_ISO ( isolocale IN VARCHAR2) RETURN VARCHAR2; Parameters Table 265-17 MAP_TERRITORY_FROM_ISO Function Parameters Parameter Description isolocale Specifies the ISO locale. The mapping is case-insensitive. Usage Notes If the user specifies an invalid locale string, then the function returns a NULL string. If the user specifies a locale string that includes only the territory (for example, _fr instead of fr_fr ), then the function returns the default territory name for the specified territory (for example, France ). Examples UTL_I18N.MAP_TERRITORY_FROM_ISO('en_US') This returns ' America' . See Also: Oracle Database Globalization Support Guide for a list of valid Oracle territories See Also: Oracle Database Globalization Support Guide for a list of valid Oracle territories