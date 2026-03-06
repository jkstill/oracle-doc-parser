---
id: 19c__DBMS_SQLDIAG.CREATE_SQL_PATCH
name: DBMS_SQLDIAG.CREATE_SQL_PATCH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.CREATE_SQL_PATCH

This function creates a SQL patch based on a set of user specified hints for specific statements identified by SQL text.

## Syntax

```sql
DBMS_SQLDIAG.CREATE_SQL_PATCH (
    sql_text        IN   CLOB,
    hint_text       IN   CLOB,
    name            IN   VARCHAR2   := NULL,
    description     IN   VARCHAR2   := NULL,
    category        IN   VARCHAR2   := NULL,
    validate        IN   BOOLEAN    := TRUE)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB | IN | Text of the SQL statement |
| sql_id |  |  | The SQL identifier for the SQL statement |
| hint_text | CLOB | IN | Hints to include in the SQL patch |
| name | VARCHAR2 | IN | Optional SQL patch name |
| description | VARCHAR2 | IN | Description of the SQL patch |
| category | VARCHAR2 | IN | Category name |
| validate | BOOLEAN | IN | Whether to validate the provided hints |

**Returns:** `VARCHAR2`

## Usage Notes

A SQL patch is usually created automatically by the SQL Repair Advisor to prevent any errors during the compilation or execution of a SQL statement. This function provides a way to manually create a SQL patch based on a set of hints that resolves the error. Syntax DBMS_SQLDIAG.CREATE_SQL_PATCH ( sql_text IN CLOB, hint_text IN CLOB, name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, category IN VARCHAR2 := NULL, validate IN BOOLEAN := TRUE) RETURN VARCHAR2; DBMS_SQLDIAG.CREATE_SQL_PATCH ( sql_id IN VARCHAR2, hint_text IN CLOB, name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, category IN VARCHAR2 := NULL, validate IN BOOLEAN := TRUE) RETURN VARCHAR2; Parameters Table 165-14 CREATE_SQL_PATCH Function Parameters Parameter Description sql_text Text of the SQL statement sql_id The SQL identifier for the SQL statement hint_text Hints to include in the SQL patch name Optional SQL patch name description Description of the SQL patch category Category name validate Whether to validate the provided hints Return Values Both functions return the SQL patch name.