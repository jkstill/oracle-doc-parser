---
id: 19c__DBMS_SPD.SET_PREFS
name: DBMS_SPD.SET_PREFS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPD
tags: [dbms_spd]
source_file: DBMS_SPD.html
---

# DBMS_SPD.SET_PREFS

This procedure allows the setting of different preferences for SQL plan directives.

## Syntax

```sql
DBMS_SPD.SET_PREFS (
   pname     IN   VARCHAR2,
   pvalue    IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pname | VARCHAR2 | IN | Preference name. The procedure supports the preference SPD_RETENTION_WEEKS . |
| pvalue | VARCHAR2) | IN | Preference value. SPD_RETENTION_WEEKS: SQL plan directives are purged if not used for more than the value set for this preference. Default is 53 ( SPD_RETENTION_WEEKS_DEFAULT ) weeks, which means a directive is purged if it has been left unused for little over a year. It can be set to any value greater than or equal to 0. Also value NULL can be passed to set the preference to default. |

## Usage Notes

Syntax DBMS_SPD.SET_PREFS ( pname IN VARCHAR2, pvalue IN VARCHAR2); Parameters Table 160-7 SET_PREFS Procedure Parameters Parameter Description pname Preference name. The procedure supports the preference SPD_RETENTION_WEEKS . pvalue Preference value. SPD_RETENTION_WEEKS: SQL plan directives are purged if not used for more than the value set for this preference. Default is 53 ( SPD_RETENTION_WEEKS_DEFAULT ) weeks, which means a directive is purged if it has been left unused for little over a year. It can be set to any value greater than or equal to 0. Also value NULL can be passed to set the preference to default. Exceptions ORA-38171 INSUFFICIENT_PRIVILEGE : The user does not have proper privilege to perform the operation. ORA-28104 INVALID_INPUT : The input value is not valid. Usage Notes The ADMINISTER SQL MANAGEMENT OBJECT privilege is required to execute this procedure. SPD_RETENTION_WEEKS - SQL plan directives are purged if not used for more than the value set for this preference. Examples BEGIN DBMS_SPD.SET_PREFS('SPD_RETENTION_WEEKS', '4'); END;