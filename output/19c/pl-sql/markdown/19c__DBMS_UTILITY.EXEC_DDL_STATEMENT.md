---
id: 19c__DBMS_UTILITY.EXEC_DDL_STATEMENT
name: DBMS_UTILITY.EXEC_DDL_STATEMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.EXEC_DDL_STATEMENT

This procedure executes the DDL statement in parse_string .

## Syntax

```sql
DBMS_UTILITY.EXEC_DDL_STATEMENT (
   parse_string IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parse_string | VARCHAR2) | IN | DDL statement to be executed |

## Usage Notes

Syntax DBMS_UTILITY.EXEC_DDL_STATEMENT ( parse_string IN VARCHAR2); Parameters Table 187-17 EXEC_DDL_STATEMENT Procedure Parameters Parameter Description parse_string DDL statement to be executed