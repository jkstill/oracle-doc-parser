---
id: 19c__DBMS_SQL_TRANSLATOR.DEREGISTER_SQL_TRANSLATION
name: DBMS_SQL_TRANSLATOR.DEREGISTER_SQL_TRANSLATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.DEREGISTER_SQL_TRANSLATION

This procedure deregisters the custom translation of a SQL statement in a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.DEREGISTER_SQL_TRANSLATION (
   profile_name      IN  VARCHAR2,
   sql_text          IN  CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| sql_text | CLOB) | IN | SQL statement |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.DEREGISTER_SQL_TRANSLATION ( profile_name IN VARCHAR2, sql_text IN CLOB); Parameters Table 164-6 DEREGISTER_SQL_TRANSLATION Procedure Parameters Parameter Description profile_name Name of profile sql_text SQL statement Exceptions Table 164-7 DEREGISTER_SQL_TRANSLATION Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist PROFILE_EXISTS Profile already exists Examples BEGIN DBMS_SQL_TRANSLATOR.DEREGISTER_SQL_TRANSLATION( profile_name => 'tsql_application', sql_text => 'select top 5 * from emp'); END;