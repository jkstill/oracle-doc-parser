---
id: 19c__DBMS_SQL_TRANSLATOR.SQL_HASH
name: DBMS_SQL_TRANSLATOR.SQL_HASH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.SQL_HASH

This procedure computes the hash value of a SQL statement in the session's SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.SQL_HASH (
   sql_text         IN    CLOB) 
RETURN NUMBER DETERMINISTIC;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB) | IN | SQL statement |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.SQL_HASH ( sql_text IN CLOB) RETURN NUMBER DETERMINISTIC; Parameters Table 164-26 SQL_HASH Function Parameters Parameter Description sql_text SQL statement Return Values Returns hash value of the SQL statement in the SQL translation profile Exceptions Table 164-27 SQL_HASH Function Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface Examples DECLARE sqltext CLOB; txltext CLOB; sqlhash NUMBER; BEGIN sqltext := 'SELECT TOP 1 * FROM emp'; sqlhash := DBMS_SQL_TRANSLATOR.SQL_HASH (sqltext); SELECT translated_text INTO txltext FROM user_sql_translations WHERE sql_hash = sqlhash AND DBMS_LOB.COMPARE (sql_text, sqltext) = 0; END;