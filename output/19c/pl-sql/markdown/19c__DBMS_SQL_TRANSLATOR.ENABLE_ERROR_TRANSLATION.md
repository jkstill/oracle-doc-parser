---
id: 19c__DBMS_SQL_TRANSLATOR.ENABLE_ERROR_TRANSLATION
name: DBMS_SQL_TRANSLATOR.ENABLE_ERROR_TRANSLATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.ENABLE_ERROR_TRANSLATION

This procedure enables or disables a custom translation of an Oracle error code in a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.ENABLE_ERROR_TRANSLATION (
   profile_name      IN  VARCHAR2,
   sql_text          IN CLOB,
   enable            IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| sql_text | CLOB | IN | SQL statement |
| enable | BOOLEAN | IN | Enable or disable the translation |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.ENABLE_ERROR_TRANSLATION ( profile_name IN VARCHAR2, sql_text IN CLOB, enable IN BOOLEAN DEFAULT TRUE); Parameters Table 164-12 ENABLE_ERROR_TRANSLATION Procedure Parameters Parameter Description profile_name Name of profile sql_text SQL statement enable Enable or disable the translation Exceptions Table 164-13 ENABLE_ERROR_TRANSLATION Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Examples BEGIN DBMS_SQL_TRANSLATOR.ENABLE_ERROR_TRANSLATION( profile_name => 'tsql_application', sql_text => 'SELECT TOP 5 * FROM emp' enable => TRUE); END;