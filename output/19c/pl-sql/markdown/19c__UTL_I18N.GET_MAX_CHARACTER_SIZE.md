---
id: 19c__UTL_I18N.GET_MAX_CHARACTER_SIZE
name: UTL_I18N.GET_MAX_CHARACTER_SIZE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_MAX_CHARACTER_SIZE

This function returns the maximum character size of a given character set.

## Syntax

```sql
UTL_I18N.GET_MAX_CHARACTER_SIZE(
    charset_name       IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| charset_name | VARCHAR2 | IN | Specifies a valid character set name. It is case-insensitive. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_I18N.GET_MAX_CHARACTER_SIZE( charset_name IN VARCHAR2 CHARACTER SET ANY_CS) RETURN PLS_INTEGER; Parameters Table 265-11 GET_MAX_CHARACTER_SIZE Function Parameters Parameter Description charset_name Specifies a valid character set name. It is case-insensitive. Usage Notes For shift-sensitive character sets, the returned maximum character size will include the possible extra shift characters. Examples UTL_I18N.GET_MAX_CHARACTER_SIZE('AL32UTF8'); This returns 4.