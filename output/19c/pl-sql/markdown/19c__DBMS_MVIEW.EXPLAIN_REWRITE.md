---
id: 19c__DBMS_MVIEW.EXPLAIN_REWRITE
name: DBMS_MVIEW.EXPLAIN_REWRITE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.EXPLAIN_REWRITE

This procedure enables you to learn why a query failed to rewrite, or, if it rewrites, which materialized views will be used.

## Syntax

```sql
DBMS_MVIEW.EXPLAIN_REWRITE (
    query           VARCHAR2,
    mv              VARCHAR2(30),
    statement_id    VARCHAR2(30));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| query | VARCHAR2 | IN | SQL SELECT statement to be explained |
| mv | VARCHAR2(30) | IN | The fully qualified name of an existing materialized view in the form of SCHEMA.MV . For multiple materialized views, you can provide a comma-delimited list of names. |
| statement_id | VARCHAR2(30)) | IN | A client-supplied unique identifier to distinguish output messages |
| msg_array |  |  | The PL/SQL VARRAY that receives the output. Use this parameter to direct EXPLAIN_REWRITE 's output to a PL/SQL VARRAY . |

## Usage Notes

Using the results from the procedure, you can take the appropriate action needed to make a query rewrite if at all possible. The query specified in the EXPLAIN_REWRITE statement is never actually executed. A demo file, xrwutl.sql , is available to help format the output from EXPLAIN_REWRITE . Syntax You can obtain the output from DBMS_MVIEW.EXPLAIN_REWRITE in two ways. The first is to use a table, while the second is to create a VARRAY . The following shows the basic syntax for using an output table: DBMS_MVIEW.EXPLAIN_REWRITE ( query VARCHAR2, mv VARCHAR2(30), statement_id VARCHAR2(30)); You can create an output table called REWRITE_TABLE by executing the utlxrw.sql script. The query parameter is a text string representing the SQL query. The parameter, mv , is a fully qualified materialized view name in the form of schema.mv . This is an optional parameter. When it is not specified, EXPLAIN_REWRITE returns any relevant messages regarding all the materialized views considered for rewriting the given query. When schema is omitted and only mv is specified, EXPLAIN_REWRITE looks for the materialized view in the current schema. If you want to direct the output of EXPLAIN_REWRITE to a VARRAY instead of a table, you should call the procedure as follows: DBMS_MVIEW.EXPLAIN_REWRITE ( query [VARCHAR2 | CLOB], mv VARCHAR2(30), output_array SYS.RewriteArrayType); Note that if the query is less than 256 characters long, EXPLAIN_REWRITE can be easily invoked with the EXECUTE command from SQL*Plus. Otherwise, the recommended method is to use a PL/SQL BEGIN... END block, as shown in the examples in /rdbms/demo/smxrw* . You can also use EXPLAIN_REWRITE with multiple materialized views, in which case the syntax will be the same as with a single materialized view, except that the materialized views are specified by a comma-delimited string. For example, to find out whether a given set of materialized views mv1 , mv2 , and mv3 could be used to rewrite the query, query_txt , and, if not, why not, use EXPLAIN_REWRITE as follows: DBMS_MVIEW.EXPLAIN_REWRITE(query_txt, 'mv1, mv2, mv3') See Oracle Database Data Warehousing Guide for more information on using the EXPLAIN_REWRITE procedure. Parameters Table 113-6 EXPLAIN_REWRITE Procedure Parameters Parameter Description query SQL SELECT statement to be explained mv The fully qualified name of an existing materialized view in the form of SCHEMA.MV . For multiple materialized views, you can provide a comma-delimited list of names. statement_id A client-supplied unique identifier to distinguish output messages msg_array The PL/SQL VARRAY that receives the output. Use this parameter to direct EXPLAIN_REWRITE 's output to a PL/SQL VARRAY . Usage Notes To obtain the output into a table, you must run the utlxrw.sq l script before calling EXPLAIN_REWRITE . This script creates a table named REWRITE_TABLE in the current schema.