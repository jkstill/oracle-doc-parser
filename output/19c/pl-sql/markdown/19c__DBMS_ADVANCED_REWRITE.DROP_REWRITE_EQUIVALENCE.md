---
id: 19c__DBMS_ADVANCED_REWRITE.DROP_REWRITE_EQUIVALENCE
name: DBMS_ADVANCED_REWRITE.DROP_REWRITE_EQUIVALENCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVANCED_REWRITE
tags: [dbms_advanced_rewrite]
source_file: DBMS_ADVANCED_REWRITE.html
---

# DBMS_ADVANCED_REWRITE.DROP_REWRITE_EQUIVALENCE

This procedure drops the specified rewrite equivalence declaration.

## Syntax

```sql
DBMS_ADVANCED_REWRITE.DROP_REWRITE_EQUIVALENCE (
   name        VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | A name for the equivalence declaration to drop. The name can be of the form owner.name , where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is dropped in the current schema. The invoker must have the appropriate drop materialized view privilege to drop an equivalence declaration outside their own schema. |

## Usage Notes

Syntax DBMS_ADVANCED_REWRITE.DROP_REWRITE_EQUIVALENCE ( name VARCHAR2); Parameters Table 15-5 DROP_REWRITE_EQUIVALENCE Procedure Parameters Parameter Description name A name for the equivalence declaration to drop. The name can be of the form owner.name , where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is dropped in the current schema. The invoker must have the appropriate drop materialized view privilege to drop an equivalence declaration outside their own schema.