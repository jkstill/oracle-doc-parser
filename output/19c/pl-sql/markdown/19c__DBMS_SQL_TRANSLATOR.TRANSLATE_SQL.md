---
id: 19c__DBMS_SQL_TRANSLATOR.TRANSLATE_SQL
name: DBMS_SQL_TRANSLATOR.TRANSLATE_SQL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.TRANSLATE_SQL

This procedure translates a SQL statement using a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.TRANSLATE_SQL (
   sql_text          IN           CLOB,
   translated_text   OUT  NOCOPY  CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB | IN | SQL statement |
| translated_text | NOCOPY | OUT | Translated SQL statement |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.TRANSLATE_SQL ( sql_text IN CLOB, translated_text OUT NOCOPY CLOB); Parameters Table 164-32 TRANSLATE_SQL Procedure Parameters Parameter Description sql_text SQL statement translated_text Translated SQL statement Exceptions Table 164-33 TRANSLATE_SQL Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Examples ALTER SESSION SET SQL_TRANSLATION_PROFILE = tsql_application; DECLARE translated_text CLOB; BEGIN DBMS_SQL_TRANSLATOR.TRANSLATE_SQL( sql_text => 'select top 5 * from emp', translated_text => translated_text); END;