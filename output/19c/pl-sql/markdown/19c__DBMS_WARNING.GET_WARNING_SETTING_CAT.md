---
id: 19c__DBMS_WARNING.GET_WARNING_SETTING_CAT
name: DBMS_WARNING.GET_WARNING_SETTING_CAT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WARNING
tags: [dbms_warning]
source_file: DBMS_WARNING.html
---

# DBMS_WARNING.GET_WARNING_SETTING_CAT

This function returns the specific warning category setting for the current session.

## Syntax

```sql
DBMS_WARNING.GET_WARNING_SETTING_CAT (
   warning_category    IN    VARCHAR2)
RETURN warning_value;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| warning_category | VARCHAR2) | IN | Name of the category. Allowed values are all valid category names ( ALL , INFORMATIONAL , SEVERE and PERFORMANCE ). |

**Returns:** `warning_value`

## Usage Notes

Syntax DBMS_WARNING.GET_WARNING_SETTING_CAT ( warning_category IN VARCHAR2) RETURN warning_value; Parameters Table 188-5 GET_WARNING_SETTING_CAT Function Parameters Parameter Description warning_category Name of the category. Allowed values are all valid category names ( ALL , INFORMATIONAL , SEVERE and PERFORMANCE ).