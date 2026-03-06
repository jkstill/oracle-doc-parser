---
id: 19c__DBMS_SQL.RETURN_RESULT
name: DBMS_SQL.RETURN_RESULT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.RETURN_RESULT

This procedure returns the result of an executed statement to the client application.

## Syntax

```sql
DBMS_SQL.RETURN_RESULT(
   rc           IN OUT      SYS_REFCURSOR, 
   to_client    IN          BOOLEAN           DEFAULT TRUE);

DBMS_SQL.RETURN_RESULT(
   rc           IN OUT      INTEGER, 
   to_client    IN          BOOLEAN           DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rc | SYS_REFCURSOR | IN OUT | Statement cursor or ref cursor |
| to_client | BOOLEAN | IN | Returns (or does not return) the statement result to the client. If not, it is returned to the immediate caller. |

## Usage Notes

The result can be retrieved later by the client. Alternatively, it can return the statement result to and be retrieved later by the immediate caller that executes a recursive statement in which this statement result will be returned. The caller can be: A PL/SQL stored procedure executing the recursive statement using DBMS_SQL A Java stored procedure using JDBC A .NET stored procedure using ADO.NET An external procedure using the Oracle Call Interface (OCI) Syntax DBMS_SQL.RETURN_RESULT( rc IN OUT SYS_REFCURSOR, to_client IN BOOLEAN DEFAULT TRUE); DBMS_SQL.RETURN_RESULT( rc IN OUT INTEGER, to_client IN BOOLEAN DEFAULT TRUE); Parameters Table 162-30 RETURN_RESULT Procedure Parameters Parameter Description rc Statement cursor or ref cursor to_client Returns (or does not return) the statement result to the client. If not, it is returned to the immediate caller. Usage Notes Currently only a SQL query can be returned, and the return of statement results over remote procedure calls is not supported. Once the statement is returned, it is no longer accessible except by the client or the immediate caller to which it is returned. Statement results cannot be returned when the statement being executed by the client or any intermediate recursive statement is a SQL query and an error is raised. A ref cursor being returned can be strongly or weakly-typed. A query being returned can be partially fetched. Because EXECUTE IMMEDIATE statement provides no interface to retrieve the statement results returned from its recursive statement, the cursors of the statement results returned to the caller of the EXECUTE IMMEDIATE statement will be closed when the statement completes. To retrieve the returned statement results from a recursive statement in PL/SQL, use DBMS_SQL to execute the recursive statement. Examples CREATE PROCEDURE proc AS rc1 sys_refcursor; rc2 sys_refcursor; BEGIN OPEN rc1 FOR SELECT * FROM t1; DBMS_SQL.RETURN_RESULT(rc1); OPEN rc2 FOR SELECT * FROM t2; DBMS_SQL.RETURN_RESULT(rc2); END; /