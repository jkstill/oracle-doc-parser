---
id: 19c__DBMS_SQL.TO_CURSOR_NUMBER
name: DBMS_SQL.TO_CURSOR_NUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.TO_CURSOR_NUMBER

This function takes an OPEN ed strongly or weakly-typed ref cursor and transforms it into a DBMS_SQL cursor number.

## Syntax

```sql
DBMS_SQL.TO_CURSOR_NUMBER(
   rc IN OUT SYS_REFCURSOR)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rc | SYS_REFCURSOR) | IN OUT | REF CURSOR to be transformed into a cursor number |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_SQL.TO_CURSOR_NUMBER( rc IN OUT SYS_REFCURSOR) RETURN INTEGER; Parameters Table 162-31 TO_CURSOR_NUMBER Function Parameters Parameter Description rc REF CURSOR to be transformed into a cursor number Return Values Returns a DBMS_SQL manageable cursor number transformed from a REF CURSOR Usage Notes The REF CURSOR passed in has to be OPEN ed, otherwise an error is raised. Once the REF CURSOR is transformed into a DBMS_SQL cursor number, the REF CURSOR is no longer accessible by any native dynamic SQL operations. The DBMS_SQL cursor that is returned by this subprogram performs in the same way as a DBMS_SQL cursor that has already been executed. Examples CREATE OR REPLACE PROCEDURE DO_QUERY(sql_stmt VARCHAR2) IS TYPE CurType IS REF CURSOR; src_cur CurType; curid NUMBER; desctab DBMS_SQL.DESC_TAB; colcnt NUMBER; namevar VARCHAR2(50); numvar NUMBER; datevar DATE; empno NUMBER := 100; BEGIN -- sql_stmt := 'select ...... from employees where employee_id = :b1'; OPEN src_cur FOR sql_stmt USING empno; -- Switch from native dynamic SQL to DBMS_SQL curid := DBMS_SQL.TO_CURSOR_NUMBER (src_cur); DBMS_SQL.DESCRIBE_COLUMNS(curid, colcnt, desctab); -- Define columns FOR i IN 1 .. colcnt LOOP IF desctab(i).col_type = 2 THEN DBMS_SQL.DEFINE_COLUMN(curid, i, numvar); ELSIF desctab(i).col_type = 12 THEN DBMS_SQL.DEFINE_COLUMN(curid, i, datevar); ....... ELSE DBMS_SQL.DEFINE_COLUMN(curid, i, namevar, 25); END IF; END LOOP; -- Fetch Rows WHILE DBMS_SQL.FETCH_ROWS(curid) > 0 LOOP FOR i IN 1 .. colcnt LOOP IF (desctab(i).col_type = 1) THEN DBMS_SQL.COLUMN_VALUE(curid, i, namevar); ELSIF (desctab(i).col_type = 2) THEN DBMS_SQL.COLUMN_VALUE(curid, i, numvar); ELSIF (desctab(i).col_type = 12) THEN DBMS_SQL.COLUMN_VALUE(curid, i, datevar); .... END IF; END LOOP; END LOOP; DBMS_SQL.CLOSE_CURSOR(curid); END; /