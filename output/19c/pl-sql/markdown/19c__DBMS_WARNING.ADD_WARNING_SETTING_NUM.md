---
id: 19c__DBMS_WARNING.ADD_WARNING_SETTING_NUM
name: DBMS_WARNING.ADD_WARNING_SETTING_NUM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WARNING
tags: [dbms_warning]
source_file: DBMS_WARNING.html
---

# DBMS_WARNING.ADD_WARNING_SETTING_NUM

You can modify the current session or system warning settings with the value supplied in this procedure. If the value was already set, you will override the existing value.

## Syntax

```sql
DBMS_WARNING.ADD_WARNING_SETTING_NUM (
   warning_number      IN    NUMBER,
   warning_value       IN    VARCHAR2,
   scope               IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| warning_number | NUMBER | IN | The warning number. Allowed values are all valid warning numbers. |
| warning_value | VARCHAR2 | IN | Value for the category. Allowed values are ENABLE , DISABLE , and ERROR . |
| scope | VARCHAR2) | IN | Specifies if the changes are being performed in the session context or the system context. Allowed values are SESSION or SYSTEM . |

## Usage Notes

The effect of calling this function is same as adding the qualifier ( ENABLE / DISABLE / ERROR ) on the category specified to the end of the current session or system setting. Syntax DBMS_WARNING.ADD_WARNING_SETTING_NUM ( warning_number IN NUMBER, warning_value IN VARCHAR2, scope IN VARCHAR2); Parameters Table 188-3 ADD_WARNING_SETTING_NUM Procedure Parameters Parameter Description warning_number The warning number. Allowed values are all valid warning numbers. warning_value Value for the category. Allowed values are ENABLE , DISABLE , and ERROR . scope Specifies if the changes are being performed in the session context or the system context. Allowed values are SESSION or SYSTEM .