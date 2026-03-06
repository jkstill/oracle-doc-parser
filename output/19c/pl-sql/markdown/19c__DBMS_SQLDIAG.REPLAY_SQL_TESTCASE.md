---
id: 19c__DBMS_SQLDIAG.REPLAY_SQL_TESTCASE
name: DBMS_SQLDIAG.REPLAY_SQL_TESTCASE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.REPLAY_SQL_TESTCASE

This function automates the reproduction of the SQL Test Case.

## Syntax

```sql
DBMS_SQLDIAG.REPLAY_SQL_TESTCASE (
   directory       IN   VARCHAR2,
   filename        IN   VARCHAR2,
   ctrlOptions     IN   VARCHAR2  := NULL,
   format          IN   VARCHAR2  := 'TEXT')
   RETURN CLOB;

DBMS_SQLDIAG.REPLAY_SQL_TESTCASE (
   directory       IN   VARCHAR2,
   sqlTestCase     IN   CLOB,
   ctrlOptions     IN   VARCHAR2  := NULL,
   format          IN   VARCHAR2  := 'TEXT')
   RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| directory | VARCHAR2 | IN | Directory containing test case files |
| filename | VARCHAR2 | IN | Name of a file containing an XML document describing the SQL test case |
| ctrlOptions | VARCHAR2 | IN | Opaque control parameters. For example, to execute three times, set ctrlOptions with the following string: '<parameter name="mexec_count">3</parameter>' . replay - EXPLAIN (default), OUTLINE , EXECUTION or OUTLINE EXECUTION . This parameter defines TCB replay functionality. EXPLAIN : Replay explains the statement without using outlines OUTLINE : Replay uses outlines mode and explains the statement using outlines EXECUTION : Replay executes the statement without using outlines OUTLINE EXECUTION : Replay executes the statement using outlines Note that if the user gives an incorrect parameter value, then the replay runs in default mode and no error is thrown. name=mexec_count - Value is any positive number ( N ). This parameter tells TCB to execute the statement for N time and capture runtime info at end of each execution. |
| sqlTestCase | CLOB | IN | SQL test case |
| format | VARCHAR2 | IN | Format of the replay report. Possible formats are: TEXT , XML and HTML .. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_SQLDIAG.REPLAY_SQL_TESTCASE ( directory IN VARCHAR2, filename IN VARCHAR2, ctrlOptions IN VARCHAR2 := NULL, format IN VARCHAR2 := 'TEXT') RETURN CLOB; DBMS_SQLDIAG.REPLAY_SQL_TESTCASE ( directory IN VARCHAR2, sqlTestCase IN CLOB, ctrlOptions IN VARCHAR2 := NULL, format IN VARCHAR2 := 'TEXT') RETURN CLOB; Parameters Table 165-30 REPLAY_SQL_TESTCASE Function Parameters Parameter Description directory Directory containing test case files filename Name of a file containing an XML document describing the SQL test case ctrlOptions Opaque control parameters. For example, to execute three times, set ctrlOptions with the following string: '<parameter name="mexec_count">3</parameter>' . replay - EXPLAIN (default), OUTLINE , EXECUTION or OUTLINE EXECUTION . This parameter defines TCB replay functionality. EXPLAIN : Replay explains the statement without using outlines OUTLINE : Replay uses outlines mode and explains the statement using outlines EXECUTION : Replay executes the statement without using outlines OUTLINE EXECUTION : Replay executes the statement using outlines Note that if the user gives an incorrect parameter value, then the replay runs in default mode and no error is thrown. name=mexec_count - Value is any positive number ( N ). This parameter tells TCB to execute the statement for N time and capture runtime info at end of each execution. sqlTestCase SQL test case format Format of the replay report. Possible formats are: TEXT , XML and HTML .. Examples TCB Replay Mode: Execute SELECT /* tcbdynpl_1 */ /*+ gather_plan_statistics */ * FROM (SELECT * FROM emp where emp.sal > 100) emp, dept WHERE emp.deptno = dept.deptno And emp.sal > 1000 /* tcbdynpl_1 */ Explain Plan Plan Hash Value : 2219294842 ----------------------------------------------------------------- | Id | Operation | Name | Rows | ----------------------------------------------------------------- | 0 | SELECT STATEMENT | | 13 | | * 1 | HASH JOIN | | 13 | | 2 | NESTED LOOPS | | | | 3 | NESTED LOOPS | | 13 | | 4 | STATISTICS COLLECTOR | | | | 5 | TABLE ACCESS FULL | DEPT | 4 | | * 6 | INDEX RANGE SCAN | EMP_IDX_DEPTNO | | | * 7 | TABLE ACCESS BY INDEX ROWID | EMP | 3 | | * 8 | TABLE ACCESS FULL | EMP | 13 | ----------------------------------------------------------------- Predicate Information (identified by operation id): ------------------------------------------ * 1 - access("EMP"."DEPTNO"="DEPT"."DEPTNO") * 6 - access("EMP"."DEPTNO"="DEPT"."DEPTNO") * 7 - filter("EMP"."SAL">1000) * 8 - filter("EMP"."SAL">1000) Runtime Plan Plan Hash Value : 2219294842 ------------------------------------------------------- | Id | Operation | Name | E-Card | A-Card | ------------------------------------------------------- | 0 | SELECT STATEMENT | | | 0 | | * 1 | HASH JOIN | | 13 | 0 | | 2 | TABLE ACCESS FULL | DEPT | 4 | 0 | | * 3 | TABLE ACCESS FULL | EMP | 13 | 0 | ------------------------------------------------------- Predicate Information (identified by operation id): ------------------------------------------ * 1 - access("EMP"."DEPTNO"="DEPT"."DEPTNO") * 3 - filter("EMP"."SAL">1000) REPLAY Note: ----------- - Replay used dynamic sampling - Replay forced Dynamic plan