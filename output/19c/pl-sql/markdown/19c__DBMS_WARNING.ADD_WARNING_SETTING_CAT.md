---
id: 19c__DBMS_WARNING.ADD_WARNING_SETTING_CAT
name: DBMS_WARNING.ADD_WARNING_SETTING_CAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WARNING
tags: [dbms_warning]
source_file: DBMS_WARNING.html
---

# DBMS_WARNING.ADD_WARNING_SETTING_CAT

You can modify the current session's or system's warning settings with the value supplied in this procedure. The value will be added to the existing parameter setting if the value for the warning_category or warning_value has not been set, or override the existing value.

## Syntax

```sql
DBMS_WARNING.ADD_WARNING_SETTING_CAT (
   warning_category    IN    VARCHAR2,
   warning_value       IN    VARCHAR2,
   scope               IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| warning_category | VARCHAR2 | IN | Name of the category. Allowed values are ALL , INFORMATIONAL , SEVERE and PERFORMANCE . |
| warning_value | VARCHAR2 | IN | Value for the category. Allowed values are ENABLE , DISABLE , and ERROR . |
| scope | VARCHAR2) | IN | Specifies if the changes are being performed in the session context or the system context. Allowed values are SESSION or SYSTEM . |

## Usage Notes

The effect of calling this function is same as adding the qualifier ( ENABLE / DISABLE / ERROR ) on the category specified to the end of the current session or system setting. Syntax DBMS_WARNING.ADD_WARNING_SETTING_CAT ( warning_category IN VARCHAR2, warning_value IN VARCHAR2, scope IN VARCHAR2); Parameters Table 188-2 ADD_WARNING_SETTING_CAT Procedure Parameters Parameter Description warning_category Name of the category. Allowed values are ALL , INFORMATIONAL , SEVERE and PERFORMANCE . warning_value Value for the category. Allowed values are ENABLE , DISABLE , and ERROR . scope Specifies if the changes are being performed in the session context or the system context. Allowed values are SESSION or SYSTEM .