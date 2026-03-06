---
id: 19c__DBMS_ADVANCED_REWRITE.DECLARE_REWRITE_EQUIVALENCE
name: DBMS_ADVANCED_REWRITE.DECLARE_REWRITE_EQUIVALENCE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVANCED_REWRITE
tags: [dbms_advanced_rewrite]
source_file: DBMS_ADVANCED_REWRITE.html
---

# DBMS_ADVANCED_REWRITE.DECLARE_REWRITE_EQUIVALENCE

This procedure creates a declaration indicating that source_stmt is functionally equivalent to destination_stmt for as long as the equivalence declaration remains enabled, and that destination_stmt is more favorable in terms of performance.

## Syntax

```sql
DBMS_ADVANCED_REWRITE.DECLARE_REWRITE_EQUIVALENCE (
   name                 VARCHAR2,
   source_stmt          VARCHAR2,
   destination_stmt     VARCHAR2,
   validate             BOOLEAN    := TRUE,
   rewrite_mode         VARCHAR2   := 'TEXT_MATCH');

DBMS_ADVANCED_REWRITE.DECLARE_REWRITE_EQUIVALENCE (
   name                 VARCHAR2,
   source_stmt          CLOB,
   destination_stmt     CLOB,
   validate             BOOLEAN   := TRUE,
   rewrite_mode         VARCHAR2  := 'TEXT_MATCH');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | A name for the equivalence declaration. The name can be of the form owner.name , where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is created in the current schema. The invoker must have the appropriate CREATE MATERIALIZED VIEW privileges to alter an equivalence declaration. |
| source_stmt | VARCHAR2 | IN | A sub- SELECT expression in either VARCHAR2 or CLOB format. This is the query statement that is the target of optimization. |
| destination_stmt | VARCHAR2 | IN | A sub- SELECT expression in either VARCHAR2 or CLOB format. |
| validate | BOOLEAN | IN | A Boolean indicating whether to validate that the specified source_stmt is functionally equivalent to the specified destination_stmt . If validate is specified as TRUE , DECLARE_REWRITE_EQUIVALENCE evaluates the two sub- SELECT s and compares their results. If the results are not the same, DECLARE_REWRITE_EQUIVALENCE does not create the rewrite equivalence and returns an error condition. If FALSE , DECLARE_REWRITE_EQUIVALENCE does not validate the equivalence. |
| rewrite_mode | VARCHAR2 | IN | The following modes are supported, in increasing order of power: disabled : Query rewrite does not use the equivalence declaration. Use this mode to temporarily disable use of the rewrite equivalence declaration. text_match : Query rewrite uses the equivalence declaration only in its text match modes. This mode is useful for simple transformations. general : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. However, query rewrite makes no attempt to rewrite the specified destination_query . recursive : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. Moreover, query rewrite further attempts to rewrite the specified destination_query for further performance enhancements whenever it uses the equivalence declaration. Oracle recommends you use the least powerful mode that is sufficient to solve your performance problem. |

## Usage Notes

The scope of the declaration is system wide. The query rewrite engine uses such declarations to perform rewrite transformations in QUERY_REWRITE_INTEGRITY = trusted and stale_tolerated modes. Because the underlying equivalences between the source and destination statements cannot be enforced by the query rewrite engine, queries can be only rewritten in trusted and stale_tolerated integrity modes. Syntax DBMS_ADVANCED_REWRITE.DECLARE_REWRITE_EQUIVALENCE ( name VARCHAR2, source_stmt VARCHAR2, destination_stmt VARCHAR2, validate BOOLEAN := TRUE, rewrite_mode VARCHAR2 := 'TEXT_MATCH'); DBMS_ADVANCED_REWRITE.DECLARE_REWRITE_EQUIVALENCE ( name VARCHAR2, source_stmt CLOB, destination_stmt CLOB, validate BOOLEAN := TRUE, rewrite_mode VARCHAR2 := 'TEXT_MATCH'); Parameters Table 15-3 DECLARE_REWRITE_EQUIVALENCE Procedure Parameters Parameter Description name A name for the equivalence declaration. The name can be of the form owner.name , where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is created in the current schema. The invoker must have the appropriate CREATE MATERIALIZED VIEW privileges to alter an equivalence declaration. source_stmt A sub- SELECT expression in either VARCHAR2 or CLOB format. This is the query statement that is the target of optimization. destination_stmt A sub- SELECT expression in either VARCHAR2 or CLOB format. validate A Boolean indicating whether to validate that the specified source_stmt is functionally equivalent to the specified destination_stmt . If validate is specified as TRUE , DECLARE_REWRITE_EQUIVALENCE evaluates the two sub- SELECT s and compares their results. If the results are not the same, DECLARE_REWRITE_EQUIVALENCE does not create the rewrite equivalence and returns an error condition. If FALSE , DECLARE_REWRITE_EQUIVALENCE does not validate the equivalence. rewrite_mode The following modes are supported, in increasing order of power: disabled : Query rewrite does not use the equivalence declaration. Use this mode to temporarily disable use of the rewrite equivalence declaration. text_match : Query rewrite uses the equivalence declaration only in its text match modes. This mode is useful for simple transformations. general : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. However, query rewrite makes no attempt to rewrite the specified destination_query . recursive : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. Moreover, query rewrite further attempts to rewrite the specified destination_query for further performance enhancements whenever it uses the equivalence declaration. Oracle recommends you use the least powerful mode that is sufficient to solve your performance problem. Exceptions Table 15-4 DECLARE_REWRITE_EQUIVALENCE Procedure Exceptions Exception Description ORA-30388 Name of the rewrite equivalence is not specified ORA-30391 The specified rewrite equivalence does not exist ORA-30392 The checksum analysis for the rewrite equivalence failed ORA-30393 A query block in the statement did not write ORA-30396 Rewrite equivalence procedures require the COMPATIBLE parameter to be set to 10.1 or greater Usage Notes Query rewrite using equivalence declarations occurs simultaneously and in concert with query rewrite using materialized views. The same query rewrite engine is used for both. The query rewrite engine uses the same rewrite rules to rewrite queries using both equivalence declarations and materialized views. Because the rewrite equivalence represents a specific rewrite crafted by a sophisticated user, the query rewrite engine gives priority to rewrite equivalences over materialized views when it is possible to perform a rewrite with either a materialized view or a rewrite equivalence. For this same reason, the cost-based optimizer (specifically, cost-based rewrite) will not choose an unrewritten query plan over a query plan that is rewritten to use a rewrite equivalence even if the cost of the un-rewritten plan appears more favorable. Query rewrite matches properties of the incoming request query against the equivalence declaration's source_stmt or the materialized view's defining statement, respectively, and derives an equivalent relational expression in terms of the equivalence declaration's destination_stmt or the materialized view's container table, respectively.