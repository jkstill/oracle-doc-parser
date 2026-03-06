---
id: 19c__DBMS_SQL_TRANSLATOR.REGISTER_SQL_TRANSLATION
name: DBMS_SQL_TRANSLATOR.REGISTER_SQL_TRANSLATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.REGISTER_SQL_TRANSLATION

This procedure registers a custom translation of a SQL statement in a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.REGISTER_SQL_TRANSLATION (
   profile_name      IN VARCHAR2,
   sql_text          IN CLOB,
   translated_text   IN CLOB DEFAULT NULL,
   enable            IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| sql_text | CLOB | IN | SQL statement |
| translated_text | CLOB | IN | Translated SQL statement |
| enable | BOOLEAN | IN | Enable or disable the translation |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.REGISTER_SQL_TRANSLATION ( profile_name IN VARCHAR2, sql_text IN CLOB, translated_text IN CLOB DEFAULT NULL, enable IN BOOLEAN DEFAULT TRUE); Parameters Table 164-22 REGISTER_SQL_TRANSLATION Procedure Parameters Parameter Description profile_name Name of profile sql_text SQL statement translated_text Translated SQL statement enable Enable or disable the translation Exceptions Table 164-23 REGISTER_SQL_TRANSLATION Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Usage Notes When the Oracle Database translates a statement using a translation profile, it searches for the registered custom translation first, and only invokes the translator package if no match is found. When a translation is registered in a profile, it may be disabled. Oracle Database does not search for disabled translations. When translated_text is NULL , no translation is required and the original statement is used. The old translation of the SQL statement, if present, is replaced with the new translation. To deregister a translation, use the DEREGISTER_SQL_TRANSLATION Procedure . Examples BEGIN DBMS_SQL_TRANSLATOR.REGISTER_SQL_TRANSLATION( profile_name => 'tsql_application', sql_text => 'select top 5 * from emp', translated_text => 'SELECT * FROM emp WHERE rownum <= :SYS_N_001'); END;