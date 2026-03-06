---
id: 19c__DBMS_SQL.DESCRIBE_COLUMNS3
name: DBMS_SQL.DESCRIBE_COLUMNS3
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DESCRIBE_COLUMNS3

This procedure describes the specified column. This is an alternative to DESCRIBE_COLUMNS Procedure.

## Syntax

```sql
DBMS_SQL.DESCRIBE_COLUMNS3 ( 
   c              IN  INTEGER, 
   col_cnt        OUT INTEGER, 
   desc_t         OUT DESC_TAB3);

BMS_SQL.DESCRIBE_COLUMNS3 ( 
   c              IN  INTEGER, 
   col_cnt        OUT INTEGER, 
   desc_t         OUT DESC_TAB4);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor for the columns being described. |
| col_cnt | INTEGER | OUT | Number of columns in the select list of the query. |
| desc_t | DESC_TAB3) | OUT | Describe table to fill in with the description of each of the columns of the query. This table is indexed from one to the number of elements in the select list of the query. |

## Usage Notes

Syntax DBMS_SQL.DESCRIBE_COLUMNS3 ( c IN INTEGER, col_cnt OUT INTEGER, desc_t OUT DESC_TAB3); BMS_SQL.DESCRIBE_COLUMNS3 ( c IN INTEGER, col_cnt OUT INTEGER, desc_t OUT DESC_TAB4); Pragmas PRAGMA RESTRICT_REFERENCES(describe_columns3,WNDS); Parameters Table 162-22 DESCRIBE_COLUMNS3 Procedure Parameters Parameter Description c ID number of the cursor for the columns being described. col_cnt Number of columns in the select list of the query. desc_t Describe table to fill in with the description of each of the columns of the query. This table is indexed from one to the number of elements in the select list of the query. Usage Notes The cursor passed in by the cursor ID has to be OPEN ed and PARSE d, otherwise an "invalid cursor id" error is raised. Examples CREATE TYPE PROJECT_T AS OBJECT ( projname VARCHAR2(20), mgr VARCHAR2(20)) / CREATE TABLE projecttab(deptno NUMBER, project HR.PROJECT_T) / DECLARE curid NUMBER; desctab DBMS_SQL.DESC_TAB3; colcnt NUMBER; sql_stmt VARCHAR2(200) := 'select * from projecttab'; BEGIN curid := DBMS_SQL.OPEN_CURSOR; DBMS_SQL.PARSE(curid, sql_stmt, DBMS_SQL.NATIVE); DBMS_SQL.DESCRIBE_COLUMNS3(curid, colcnt, desctab); FOR i IN 1 .. colcnt LOOP IF desctab(i).col_type = 109 THEN DBMS_OUTPUT.PUT(desctab(i).col_name || ' is user-defined type: '); DBMS_OUTPUT.PUT_LINE(desctab(i).col_schema_name || '.' || desctab(i).col_type_name); END IF; END LOOP; DBMS_SQL.CLOSE_CURSOR(curid); END; / Output: PROJECT is user-defined type: HR.PROJECT_T