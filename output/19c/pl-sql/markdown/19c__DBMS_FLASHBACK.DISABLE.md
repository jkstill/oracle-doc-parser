---
id: 19c__DBMS_FLASHBACK.DISABLE
name: DBMS_FLASHBACK.DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK
tags: [dbms_flashback]
source_file: DBMS_FLASHBACK.html
---

# DBMS_FLASHBACK.DISABLE

This procedure disables the Flashback mode for the entire session.

## Syntax

```sql
DBMS_FLASHBACK.DISABLE;
```

## Usage Notes

Syntax DBMS_FLASHBACK.DISABLE; Examples The following example queries the salary of an employee, Joe, on August 30, 2000: EXECUTE dbms_flashback.enable_at_time('30-AUG-2000'); SELECT salary FROM emp where name = 'Joe' EXECUTE dbms_flashback.disable;