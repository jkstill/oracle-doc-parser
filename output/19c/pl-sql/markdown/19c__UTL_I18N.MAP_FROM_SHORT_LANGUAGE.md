---
id: 19c__UTL_I18N.MAP_FROM_SHORT_LANGUAGE
name: UTL_I18N.MAP_FROM_SHORT_LANGUAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.MAP_FROM_SHORT_LANGUAGE

This function maps an Oracle short language name to an Oracle language name.

## Syntax

```sql
UTL_I18N.MAP_FROM_SHORT_LANGUAGE (
   language           IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| language | VARCHAR2 | IN | Specifies a valid short language name. It is case-insensitive. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_I18N.MAP_FROM_SHORT_LANGUAGE ( language IN VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2; Parameters Table 265-14 MAP_FROM_SHORT_LANGUAGE Function Parameters Parameter Description language Specifies a valid short language name. It is case-insensitive. Usage Notes If the user specifies an invalid language name, then the function returns a NULL string. Examples Returns the default linguistic sort name for the customer with the ID of 9000. Note that the table customers is from the oe user in the Common Schema. Because the customer's language preference is stored using a short language name, you need to convert to a full language name by calling the GET_DEFAULT_LINGUISTIC_SORT procedure. DECLARE short_n VARCHAR2(10); ling_n VARCHAR2(50); BEGIN SELECT nls_language INTO short FROM customers WHERE customer_id = 9000; ling_n := UTL_I18N.GET_DEFAULT_LINGUISTIC_SORT ( UTL_I18N.MAP_FROM_SHORT_LANGUAGE(short_n)); DBMS_OUTPUT.PUT_LINE(ling_n); END; /