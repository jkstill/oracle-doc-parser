---
id: 19c__DBMS_SPD.DROP_SQL_PLAN_DIRECTIVE
name: DBMS_SPD.DROP_SQL_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPD
tags: [dbms_spd]
source_file: DBMS_SPD.html
---

# DBMS_SPD.DROP_SQL_PLAN_DIRECTIVE

This procedure drops a SQL plan directive.

## Syntax

```sql
DBMS_SPD.DROP_SQL_PLAN_DIRECTIVE (
   directive_id        IN     NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| directive_id | NUMBER) | IN | SQL plan directive ID |

## Usage Notes

Syntax DBMS_SPD.DROP_SQL_PLAN_DIRECTIVE ( directive_id IN NUMBER); Parameters Table 160-4 DROP_SQL_PLAN_DIRECTIVE Procedure Parameters Parameter Description directive_id SQL plan directive ID Exceptions ORA-38171 INSUFFICIENT_PRIVILEGE : The user does not have proper privilege to perform the operation. ORA-28104 INVALID_INPUT : The input value is not valid. ORA-13158 OBJECT_DOES_NOT_EXIST : The specified object does not exist. Usage Notes The ADMINISTER SQL MANAGEMENT OBJECT privilege is required to execute this procedure. Examples BEGIN DBMS_SPD.DROP_SQL_PLAN_DIRECTIVE (12345); END;