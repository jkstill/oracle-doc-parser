---
id: 19c__DBMS_SQL_TRANSLATOR.TRANSLATE_ERROR
name: DBMS_SQL_TRANSLATOR.TRANSLATE_ERROR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.TRANSLATE_ERROR

This procedure translates an Oracle error code and an ANSI SQLSTATE using the session's SQL translation profile

## Syntax

```sql
DBMS_SQL_TRANSLATOR.TRANSLATE_ERROR (
   error_code           IN           PLS_INTEGER,
   translated_code      OUT          PLS_INTEGER,
   translated_sqlstate  OUT NOCOPY   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| error_code | PLS_INTEGER | IN | Oracle error code |
| translated_code | PLS_INTEGER | OUT | Translated error code |
| translated_sqlstate | NOCOPY | OUT | Translated SQLSTATE |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.TRANSLATE_ERROR ( error_code IN PLS_INTEGER, translated_code OUT PLS_INTEGER, translated_sqlstate OUT NOCOPY VARCHAR2); Parameters Table 164-30 TRANSLATE_ERROR Procedure Parameters Parameter Description error_code Oracle error code translated_code Translated error code translated_sqlstate Translated SQLSTATE Exceptions Table 164-31 TRANSLATE_ERROR Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist NO_TRANSLATION_FOUND No translation of the SQL statement or error code is found Examples DECLARE translated_code BINARY_INTEGER; translated_sqlstate VARCHAR2(5); BEGIN DBMS_SQL_TRANSLATOR.TRANSLATE_ERROR( error_code => 1, translated_code => translated_code, translated_sqlstate => translated_sqlstate); END;