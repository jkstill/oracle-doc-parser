---
id: 19c__DBMS_DEBUG.EXECUTE
name: DBMS_DEBUG.EXECUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.EXECUTE

This procedure executes SQL or PL/SQL code in the target session. The target session is assumed to be waiting at a breakpoint (or other event). The call to DBMS_DEBUG . EXECUTE occurs in the debug session, which then asks the target session to execute the code.

## Syntax

```sql
DBMS_DEBUG.EXECUTE (
   what         IN VARCHAR2,
   frame#       IN BINARY_INTEGER,
   bind_results IN BINARY_INTEGER,
   results      IN OUT NOCOPY dbms_debug_vc2coll,
   errm         IN OUT NOCOPY VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| what | VARCHAR2 | IN | SQL or PL/SQL source to execute |
| frame# | BINARY_INTEGER | IN | The context in which to execute the code. Only -1 (global context) is supported at this time. |
| bind_results | BINARY_INTEGER | IN | Whether the source wants to bind to results in order to return values from the target session: 0 = No 1 = Yes |
| results | NOCOPY | IN OUT | Collection in which to place results, if bind_results is not 0 |
| errm | NOCOPY | IN OUT | Error message, if an error occurred; otherwise, NULL |

## Usage Notes

Syntax DBMS_DEBUG.EXECUTE ( what IN VARCHAR2, frame# IN BINARY_INTEGER, bind_results IN BINARY_INTEGER, results IN OUT NOCOPY dbms_debug_vc2coll, errm IN OUT NOCOPY VARCHAR2); Parameters Table 57-24 EXECUTE Procedure Parameters Parameter Description what SQL or PL/SQL source to execute frame# The context in which to execute the code. Only -1 (global context) is supported at this time. bind_results Whether the source wants to bind to results in order to return values from the target session: 0 = No 1 = Yes results Collection in which to place results, if bind_results is not 0 errm Error message, if an error occurred; otherwise, NULL Examples Example 1 This example executes a SQL statement. It returns no results. DECLARE coll sys.dbms_debug_vc2coll; -- results (unused) errm VARCHAR2(100); BEGIN dbms_debug.execute('insert into emp(ename,empno,deptno) ' || 'values(''LJE'', 1, 1)', -1, 0, coll, errm); END; Example 2 This example executes a PL/SQL block, and it returns no results. The block is an autonomous transaction, which means that the value inserted into the table becomes visible in the debug session. DECLARE coll sys.dbms_debug_vc2coll; errm VARCHAR2(100); BEGIN dbms_debug.execute( 'DECLARE PRAGMA autonomous_transaction; ' || 'BEGIN ' || ' insert into emp(ename, empno, deptno) ' || ' values(''LJE'', 1, 1); ' || ' COMMIT; ' || 'END;', -1, 0, coll, errm); END; Example 3 This example executes a PL/SQL block, and it returns some results. DECLARE coll sys.dbms_debug_vc2coll; errm VARCHAR2(100); BEGIN dbms_debug.execute( 'DECLARE ' || ' pp SYS.dbms_debug_vc2coll := SYS.dbms_debug_vc2coll(); ' || ' x PLS_INTEGER; ' || ' i PLS_INTEGER := 1; ' || 'BEGIN ' || ' SELECT COUNT(*) INTO x FROM emp; ' || ' pp.EXTEND(x * 6); ' || ' FOR c IN (SELECT * FROM emp) LOOP ' || ' pp(i) := ''Ename: '' || c.ename; i := i+1; ' || ' pp(i) := ''Empno: '' || c.empno; i := i+1; ' || ' pp(i) := ''Job: '' || c.job; i := i+1; ' || ' pp(i) := ''Mgr: '' || c.mgr; i := i+1; ' || ' pp(i) := ''Sal: '' || c.sal; i := i+1; ' || ' pp(i) := null; i := i+1; ' || ' END LOOP; ' || ' :1 := pp;' || 'END;', -1, 1, coll, errm); each := coll.FIRST; WHILE (each IS NOT NULL) LOOP dosomething(coll(each)); each := coll.NEXT(each); END LOOP; END;