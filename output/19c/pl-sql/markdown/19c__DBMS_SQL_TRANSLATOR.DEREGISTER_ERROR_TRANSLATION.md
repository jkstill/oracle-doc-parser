---
id: 19c__DBMS_SQL_TRANSLATOR.DEREGISTER_ERROR_TRANSLATION
name: DBMS_SQL_TRANSLATOR.DEREGISTER_ERROR_TRANSLATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.DEREGISTER_ERROR_TRANSLATION

This procedure deregisters the translation of an Oracle error code and SQLSTATE in a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.DEREGISTER_ERROR_TRANSLATION (
   profile_name          IN   VARCHAR2,
   error_code            IN   PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| error_code | PLS_INTEGER) | IN | Oracle error code |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.DEREGISTER_ERROR_TRANSLATION ( profile_name IN VARCHAR2, error_code IN PLS_INTEGER); Parameters Table 164-8 DEREGISTER_ERROR_TRANSLATION Procedure Parameters Parameter Description profile_name Name of profile error_code Oracle error code Exceptions Table 164-9 DEREGISTER_ERROR_TRANSLATION Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Examples BEGIN DBMS_SQL_TRANSLATOR.DEREGISTER_ERROR_TRANSLATION( profile_name => 'tsql_application', error_code => 1); END;