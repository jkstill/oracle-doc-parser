---
id: 19c__DBMS_MVIEW.EXPLAIN_MVIEW
name: DBMS_MVIEW.EXPLAIN_MVIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.EXPLAIN_MVIEW

This procedure enables you to learn what is possible with a materialized view or potential materialized view. For example, you can determine if a materialized view is fast refreshable and what types of query rewrite you can perform with a particular materialized view.

## Syntax

```sql
DBMS_MVIEW.EXPLAIN_MVIEW (
   mv            IN VARCHAR2,
   statement_id  IN VARCHAR2:= NULL);

DBMS_MVIEW.EXPLAIN_MVIEW (
   mv          IN VARCHAR2,
   msg_array   OUT SYS.ExplainMVArrayType);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mv | VARCHAR2 | IN | The name of an existing materialized view (optionally qualified with the owner name separated by a ".") or a SELECT statement or a CREATE MATERIALIZED VIEW statement for a potential materialized view. |
| statement_id | VARCHAR2 | IN | A client-supplied unique identifier to associate output rows with specific invocations of EXPLAIN_MVIEW |
| msg_array | SYS.ExplainMVArrayType) | OUT | The PL/SQL VARRAY that receives the output. Use this parameter to direct EXPLAIN_MVIEW 's output to a PL/SQL VARRAY rather than MV_CAPABILITIES_TABLE . |

## Usage Notes

Using this procedure is straightforward. You simply call DBMS_MVIEW . EXPLAIN_MVIEW , passing in as parameters the schema and materialized view name for an existing materialized view. Alternatively, you can specify the SELECT string or CREATE MATERIALIZED VIEW statement for a potential materialized view. The materialized view or potential materialized view is then analyzed and the results are written into either a table called MV_CAPABILITIES_TABLE , which is the default, or to an array called MSG_ARRAY . The procedure is overloaded: The first version is for explaining an existing or potential materialized view with output to MV_CAPABILITIES_TABLE . The second version is for explaining an existing or potential materialized view with output to a VARRAY . Syntax DBMS_MVIEW.EXPLAIN_MVIEW ( mv IN VARCHAR2, statement_id IN VARCHAR2:= NULL); DBMS_MVIEW.EXPLAIN_MVIEW ( mv IN VARCHAR2, msg_array OUT SYS.ExplainMVArrayType); Parameters Table 113-5 EXPLAIN_MVIEW Procedure Parameters Parameter Description mv The name of an existing materialized view (optionally qualified with the owner name separated by a ".") or a SELECT statement or a CREATE MATERIALIZED VIEW statement for a potential materialized view. statement_id A client-supplied unique identifier to associate output rows with specific invocations of EXPLAIN_MVIEW msg_array The PL/SQL VARRAY that receives the output. Use this parameter to direct EXPLAIN_MVIEW 's output to a PL/SQL VARRAY rather than MV_CAPABILITIES_TABLE . Usage Notes You must run the utlxmv.sql script to create MV_CAPABILITIES_TABLE in the current schema prior to calling EXPLAIN_MVIEW except when you direct output to a VARRAY . The script is found in the ADMIN directory.