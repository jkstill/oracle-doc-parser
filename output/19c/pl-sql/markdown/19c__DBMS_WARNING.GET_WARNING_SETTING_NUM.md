---
id: 19c__DBMS_WARNING.GET_WARNING_SETTING_NUM
name: DBMS_WARNING.GET_WARNING_SETTING_NUM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WARNING
tags: [dbms_warning]
source_file: DBMS_WARNING.html
---

# DBMS_WARNING.GET_WARNING_SETTING_NUM

This function returns the specific warning number setting for the current session.

## Syntax

```sql
DBMS_WARNING.GET_WARNING_SETTING_NUM (
   warning_number      IN    NUMBER)
RETURN warning_value;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| warning_number | NUMBER) | IN | Warning number. Allowed values are all valid warning numbers. |

**Returns:** `warning_value`

## Usage Notes

Syntax DBMS_WARNING.GET_WARNING_SETTING_NUM ( warning_number IN NUMBER) RETURN warning_value; Parameters Table 188-6 GET_WARNING_SETTING_NUM Function Parameters Parameter Description warning_number Warning number. Allowed values are all valid warning numbers.