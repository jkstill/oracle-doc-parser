---
id: 19c__DBMS_ADVANCED_REWRITE.ALTER_REWRITE_EQUIVALENCE
name: DBMS_ADVANCED_REWRITE.ALTER_REWRITE_EQUIVALENCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVANCED_REWRITE
tags: [dbms_advanced_rewrite]
source_file: DBMS_ADVANCED_REWRITE.html
---

# DBMS_ADVANCED_REWRITE.ALTER_REWRITE_EQUIVALENCE

This table list the all the package subprograms in alphabetical order.

## Syntax

```sql
DBMS_ADVANCED_REWRITE.ALTER_REWRITE_EQUIVALENCE (
   name            VARCHAR2,
   rewrite_mode    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | A name for the equivalence declaration to alter. The name can be of the form owner.name , where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is altered in the current schema. The invoker must have the appropriate alter materialized view privileges to alter an equivalence declaration outside their own schema. |
| rewrite_mode | VARCHAR2) | IN | The following modes are supported, in increasing order of power: disabled : Query rewrite does not use the equivalence declaration. Use this mode to temporarily disable use of the rewrite equivalence declaration. text_match : Query rewrite uses the equivalence declaration only in its text match modes. This mode is useful for simple transformations. general : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. However, query rewrite makes no attempt to rewrite the specified destination_query . recursive : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. Moreover, query rewrite further attempts to rewrite the specified destination_query for further performance enhancements whenever it uses the equivalence declaration. Oracle recommends you use the least powerful mode that is sufficient to solve your performance problem. |

## Usage Notes

Syntax DBMS_ADVANCED_REWRITE.ALTER_REWRITE_EQUIVALENCE ( name VARCHAR2, rewrite_mode VARCHAR2); Parameters Table 15-2 ALTER_REWRITE_EQUIVALENCE Procedure Parameters Parameter Description name A name for the equivalence declaration to alter. The name can be of the form owner.name , where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is altered in the current schema. The invoker must have the appropriate alter materialized view privileges to alter an equivalence declaration outside their own schema. rewrite_mode The following modes are supported, in increasing order of power: disabled : Query rewrite does not use the equivalence declaration. Use this mode to temporarily disable use of the rewrite equivalence declaration. text_match : Query rewrite uses the equivalence declaration only in its text match modes. This mode is useful for simple transformations. general : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. However, query rewrite makes no attempt to rewrite the specified destination_query . recursive : Query rewrite uses the equivalence declaration in all of its transformation modes against the incoming request queries. Moreover, query rewrite further attempts to rewrite the specified destination_query for further performance enhancements whenever it uses the equivalence declaration. Oracle recommends you use the least powerful mode that is sufficient to solve your performance problem.