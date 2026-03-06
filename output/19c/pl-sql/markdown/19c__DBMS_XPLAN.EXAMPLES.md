---
id: 19c__DBMS_XPLAN.EXAMPLES
name: DBMS_XPLAN.EXAMPLES
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XPLAN
tags: [dbms_xplan]
source_file: DBMS_XPLAN.html
---

# DBMS_XPLAN.EXAMPLES

These examples show sample uses of DBMS_XPLAN.

## Syntax

```sql
EXPLAIN PLAN FOR
SELECT * FROM emp e, dept d
   WHERE e.deptno = d.deptno
   AND e.ename='benoit';
```

## Usage Notes

Displaying a Plan Table Using DBMS_XPLAN.DISPLAY Execute an explain plan command on a SELECT statement: EXPLAIN PLAN FOR SELECT * FROM emp e, dept d WHERE e.deptno = d.deptno AND e.ename='benoit'; Display the plan using the DBMS_XPLAN.DISPLAY table function SET LINESIZE 130 SET PAGESIZE 0 SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY); This query produces the following output: Plan hash value: 3693697075 --------------------------------------------------------------------------- | Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time | --------------------------------------------------------------------------- | 0 | SELECT STATEMENT | | 1 | 57 | 6 (34)| 00:00:01 | |* 1 | HASH JOIN | | 1 | 57 | 6 (34)| 00:00:01 | |* 2 | TABLE ACCESS FULL| EMP | 1 | 37 | 3 (34)| 00:00:01 | | 3 | TABLE ACCESS FULL| DEPT | 4 | 80 | 3 (34)| 00:00:01 | --------------------------------------------------------------------------- Predicate Information (identified by operation id): --------------------------------------------------- 1 - access("E"."DEPTNO"="D"."DEPTNO") 2 - filter("E"."ENAME"='benoit') 15 rows selected. Displaying a Cursor Execution Plan Using DBMS_XPLAN.DISPLAY_CURSOR By default, the table function DISPLAY_CURSOR formats the execution plan for the last SQL statement executed by the session. For example: SELECT ename FROM emp e, dept d WHERE e.deptno = d.deptno AND e.empno=7369; ENAME ---------- SMITH To display the execution plan of the last executed statement for that session: SET PAGESIZE 0 SELECT * FROM DBMS_XPLAN.DISPLAY_CURSOR(); This query produces the following output: Plan hash value: 3693697075, SQL hash value: 2096952573, child number: 0 ------------------------------------------------------------------ SELECT ename FROM emp e, dept d WHERE e.deptno = d.deptno AND e.empno=7369 --------------------------------------------------------------------------- | Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time | --------------------------------------------------------------------------- | 0 | SELECT STATEMENT | | | | | | |* 1 | HASH JOIN | | 1 | 16 | 6 (34)| 00:00:01 | |* 2 | TABLE ACCESS FULL| EMP | 1 | 13 | 3 (34)| 00:00:01 | | 3 | TABLE ACCESS FULL| DEPT | 4 | 12 | 3 (34)| 00:00:01 | --------------------------------------------------------------------------- Predicate Information (identified by operation id): --------------------------------------------------- 1 - access("E"."DEPTNO"="D"."DEPTNO") 2 - filter("E"."EMPNO"=7369) 21 rows selected. You can also use the table function DISPLAY_CURSOR to display the execution plan for any loaded cursor stored in the cursor cache. In that case, you must supply a reference to the child cursor to the table function. This includes the SQL ID of the statement and optionally the child number. Run a query with a distinctive comment: SELECT /* TOTO */ ename, dname FROM dept d join emp e USING (deptno); Get sql_id and child_number for the preceding statement: SELECT sql_id, child_number FROM v$sql WHERE sql_text LIKE '%TOTO%'; SQL_ID CHILD_NUMBER ---------- ----------------------------- gwp663cqh5qbf 0 Display the execution plan for the cursor: SELECT * FROM DBMS_XPLAN.DISPLAY_CURSOR('gwp663cqh5qbf',0); Plan hash value: 3693697075, SQL ID: gwp663cqh5qbf, child number: 0 -------------------------------------------------------- SELECT /* TOTO */ ename, dname FROM dept d JOIN emp e USING (deptno); ---------------------------------------------------------------------------- | Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time | ---------------------------------------------------------------------------- | 0 | SELECT STATEMENT | | | | 7 (100)| | | 1 | SORT GROUP BY | | 4 | 64 | 7 (43)| 00:00:01 | |* 2 | HASH JOIN | | 14 | 224 | 6 (34)| 00:00:01 | | 3 | TABLE ACCESS FULL| DEPT | 4 | 44 | 3 (34)| 00:00:01 | | 4 | TABLE ACCESS FULL| EMP | 14 | 70 | 3 (34)| 00:00:01 | ---------------------------------------------------------------------------- Predicate Information (identified by operation id): --------------------------------------------------- 2 - access("E"."DEPTNO"="D"."DEPTNO") Instead of issuing two queries, one to the get the sql_id and child_number pair and one to display the plan, you can combine these in a single query: Display the execution plan of all cursors matching the string 'TOTO': SELECT t.* FROM v$sql s, DBMS_XPLAN.DISPLAY_CURSOR(s.sql_id, s.child_number) t WHERE sql_text LIKE '%TOTO%'; Displaying a Plan Table with Parallel Information