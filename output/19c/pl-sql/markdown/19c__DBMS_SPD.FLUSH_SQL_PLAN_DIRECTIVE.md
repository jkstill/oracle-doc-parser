---
id: 19c__DBMS_SPD.FLUSH_SQL_PLAN_DIRECTIVE
name: DBMS_SPD.FLUSH_SQL_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPD
tags: [dbms_spd]
source_file: DBMS_SPD.html
---

# DBMS_SPD.FLUSH_SQL_PLAN_DIRECTIVE

This procedure allows for manual flushing of the SQL plan directives that are automatically recorded in SGA memory while executing SQL statements.

## Syntax

```sql
DBMS_SPD.FLUSH_SQL_PLAN_DIRECTIVE;
```

## Usage Notes

The information recorded in the SGA is periodically flushed by an Oracle background process. This procedure provides a way to flush the information manually. Syntax DBMS_SPD.FLUSH_SQL_PLAN_DIRECTIVE; Exceptions ORA-38171 INSUFFICIENT_PRIVILEGE : The user does not have proper privilege to perform the operation. Usage Notes The ADMINISTER SQL MANAGEMENT OBJECT privilege is required to execute this procedure. Examples BEGIN DBMS_SPD.FLUSH_SQL_PLAN_DIRECTIVE; END;