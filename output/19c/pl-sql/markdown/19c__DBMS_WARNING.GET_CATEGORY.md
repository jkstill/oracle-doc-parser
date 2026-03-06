---
id: 19c__DBMS_WARNING.GET_CATEGORY
name: DBMS_WARNING.GET_CATEGORY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WARNING
tags: [dbms_warning]
source_file: DBMS_WARNING.html
---

# DBMS_WARNING.GET_CATEGORY

This function returns the category name, given the message number.

## Syntax

```sql
DBMS_WARNING.GET_CATEGORY (
   warning_number  IN   pls_integer) 
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| warning_number | pls_integer) | IN | The warning message number. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_WARNING.GET_CATEGORY ( warning_number IN pls_integer) RETURN VARCHAR2; Parameters Table 188-4 GET_CATEGORY Function Parameters Parameter Description warning_number The warning message number.