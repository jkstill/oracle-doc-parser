---
id: 19c__DBMS_ADVANCED_REWRITE.VALIDATE_REWRITE_EQUIVALENCE
name: DBMS_ADVANCED_REWRITE.VALIDATE_REWRITE_EQUIVALENCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVANCED_REWRITE
tags: [dbms_advanced_rewrite]
source_file: DBMS_ADVANCED_REWRITE.html
---

# DBMS_ADVANCED_REWRITE.VALIDATE_REWRITE_EQUIVALENCE

This procedure validates the specified rewrite equivalence declaration.

## Syntax

```sql
DBMS_ADVANCED_REWRITE.VALIDATE_REWRITE_EQUIVALENCE (
   name         VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | A name for the equivalence declaration to validate. The name can be of the form owner.name, where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is validated in the current schema. The invoker must have sufficient privileges to execute both the source_stmt and destination_stmt of the specified equivalence declaration. |

## Usage Notes

It uses the same validation method as described with the VALIDATE parameter in " VALIDATE_REWRITE_EQUIVALENCE Procedure " . Syntax DBMS_ADVANCED_REWRITE.VALIDATE_REWRITE_EQUIVALENCE ( name VARCHAR2); Parameters Table 15-6 VALIDATE_REWRITE_EQUIVALENCE Procedure Parameters Parameter Description name A name for the equivalence declaration to validate. The name can be of the form owner.name, where owner complies with the rules for a schema name, and name compiles with the rules for a table name. Alternatively, a simple name that complies with the rules for a table name can be specified. In this case, the rewrite equivalence is validated in the current schema. The invoker must have sufficient privileges to execute both the source_stmt and destination_stmt of the specified equivalence declaration.