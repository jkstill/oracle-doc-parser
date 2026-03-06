---
id: 19c__DBMS_SPD.GET_PREFS
name: DBMS_SPD.GET_PREFS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPD
tags: [dbms_spd]
source_file: DBMS_SPD.html
---

# DBMS_SPD.GET_PREFS

This function returns the value for the specified preferences for SQL plan directives.

## Syntax

```sql
DBMS_SPD.GET_PREFS (
   pname     IN   VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pname | VARCHAR2) | IN | Preference name. The procedure supports the preference SPD_RETENTION_WEEKS . |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SPD.GET_PREFS ( pname IN VARCHAR2) RETURN VARCHAR2; Parameters Table 160-5 GET_PREFS Function Parameters Parameter Description pname Preference name. The procedure supports the preference SPD_RETENTION_WEEKS . Return Values Preference value Exceptions ORA-38171 INSUFFICIENT_PRIVILEGE : The user does not have proper privilege to perform the operation. ORA-28104 INVALID_INPUT : The input value is not valid. Usage Notes The ADMINISTER SQL MANAGEMENT OBJECT privilege is required to execute this procedure. SPD_RETENTION_WEEKS - SQL plan directives are purged if not used for more than the value set for this preference.