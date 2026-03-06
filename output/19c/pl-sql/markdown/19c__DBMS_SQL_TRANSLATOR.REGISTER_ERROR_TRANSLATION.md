---
id: 19c__DBMS_SQL_TRANSLATOR.REGISTER_ERROR_TRANSLATION
name: DBMS_SQL_TRANSLATOR.REGISTER_ERROR_TRANSLATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.REGISTER_ERROR_TRANSLATION

This procedure registers a custom translation of an Oracle error code and SQLSTATE in a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.REGISTER_ERROR_TRANSLATION (
   profile_name          IN   VARCHAR2,
   error_code            IN   PLS_INTEGER,
   translated_code       IN   PLS_INTEGER DEFAULT NULL,
   translated_sqlstate   IN   VARCHAR2 DEFAULT NULL,
   enable                IN   BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| error_code | PLS_INTEGER | IN | Oracle error code |
| translated_code | PLS_INTEGER | IN | Translated error code |
| translated_sqlstate | VARCHAR2 | IN | Translated SQLSTATE |
| enable | BOOLEAN | IN | Enable or disable the translation |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.REGISTER_ERROR_TRANSLATION ( profile_name IN VARCHAR2, error_code IN PLS_INTEGER, translated_code IN PLS_INTEGER DEFAULT NULL, translated_sqlstate IN VARCHAR2 DEFAULT NULL, enable IN BOOLEAN DEFAULT TRUE); Parameters Table 164-20 REGISTER_ERROR_TRANSLATION Procedure Parameters Parameter Description profile_name Name of profile error_code Oracle error code translated_code Translated error code translated_sqlstate Translated SQLSTATE enable Enable or disable the translation Exceptions Table 164-21 REGISTER_ERROR_TRANSLATION Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Usage Notes When the Oracle Database translates an Oracle error code using a translation profile, it searches for the registered custom translation first, and only invokes the translator package if no match is found. When a translation is registered in a profile, it may be disabled. Oracle Database does not search for disabled translations. The old translation of the error code and SQLSTATE , if present, is replaced with the new translation. To deregister a translation, use the DEREGISTER_ERROR_TRANSLATION Procedure . Examples BEGIN DBMS_SQL_TRANSLATOR.REGISTER_ERROR_TRANSLATION( profile_name => 'tsql_application', error_code => 1, translated_code => 2601); END;