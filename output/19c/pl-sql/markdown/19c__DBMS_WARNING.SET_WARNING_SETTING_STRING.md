---
id: 19c__DBMS_WARNING.SET_WARNING_SETTING_STRING
name: DBMS_WARNING.SET_WARNING_SETTING_STRING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WARNING
tags: [dbms_warning]
source_file: DBMS_WARNING.html
---

# DBMS_WARNING.SET_WARNING_SETTING_STRING

This procedure replaces previous settings with the new value.

## Syntax

```sql
DBMS_WARNING.SET_WARNING_SETTING_STRING (
   warning_value   IN   VARCHAR2,
   scope           IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| warning_value | VARCHAR2 | IN | The new string that will constitute the new value. |
| scope | VARCHAR2) | IN | This will specify if the changes are being done in the session context, or system context. Allowed values are SESSION or SYSTEM . |

## Usage Notes

The warning string may contain mix of category and warning numbers using the same syntax as used on the right hand side of '=' when issuing an ALTER SESSION or SYSTEM SET PLSQL_WARNINGS command. This will have same effect as ALTER SESSION or ALTER SYSTEM command. Syntax DBMS_WARNING.SET_WARNING_SETTING_STRING ( warning_value IN VARCHAR2, scope IN VARCHAR2); Parameters Table 188-7 SET_WARNING_SETTING_STRING Procedure Parameters Parameter Description warning_value The new string that will constitute the new value. scope This will specify if the changes are being done in the session context, or system context. Allowed values are SESSION or SYSTEM .