---
id: 19c__DBMS_EDITIONS_UTILITIES.SET_NULL_COLUMN_VALUES_TO_EXPR
name: DBMS_EDITIONS_UTILITIES.SET_NULL_COLUMN_VALUES_TO_EXPR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EDITIONS_UTILITIES
tags: [dbms_editions_utilities]
source_file: DBMS_EDITIONS_UTILITIES.html
---

# DBMS_EDITIONS_UTILITIES.SET_NULL_COLUMN_VALUES_TO_EXPR

This procedure replaces NULL values in a replacement column with the value of an expression.

## Syntax

```sql
DBMS_EDITIONS_UTILITIES.SET_NULL_COLUMN_VALUES_TO_EXPR;
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   expression    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | A potentially schema-qualified table name |
| column_name | VARCHAR2 | IN | Name of the column to be updated |
| expression | VARCHAR2) | IN | An expression composed of columns in the same table, constants, and SQL functions |

## Usage Notes

The expression evaluation cost is deferred to future updates and queries. The procedure is intended for use only during an edition-based redefinition (EBR) exercise. See Also: Oracle Database Development Guide regarding transforming pre- to post-upgrade representation See Also: Oracle Database Development Guide regarding transforming pre- to post-upgrade representation Syntax DBMS_EDITIONS_UTILITIES.SET_NULL_COLUMN_VALUES_TO_EXPR; table_name IN VARCHAR2, column_name IN VARCHAR2, expression IN VARCHAR2); Parameters Table 66-4 SET_NULL_COLUMN_VALUES_TO_EXPR Procedure Parameters Parameter Description table_name A potentially schema-qualified table name column_name Name of the column to be updated expression An expression composed of columns in the same table, constants, and SQL functions