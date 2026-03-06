---
id: 19c__DBMS_SQL_TRANSLATOR.SQL_ID
name: DBMS_SQL_TRANSLATOR.SQL_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.SQL_ID

This procedure computes the SQL identifier of a SQL statement in a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.SQL_ID (
   sql_text         IN    CLOB) 
RETURN VARCHAR2 DETERMINISTIC;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB) | IN | SQL statement |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.SQL_ID ( sql_text IN CLOB) RETURN VARCHAR2 DETERMINISTIC; Parameters Table 164-28 SQL_ID Function Parameters Parameter Description sql_text SQL statement Return Values Returns the SQL ID of the SQL statement in the SQL translation profile Exceptions Table 164-29 SQL_ID Function Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface Examples DECLARE sqltext CLOB; sqlid VARCHAR2(13); BEGIN sqltext := 'SELECT TOP 1 * FROM emp'; sqlid := DBMS_SQL_TRANSLATOR.SQL_ID (sqltext); END;