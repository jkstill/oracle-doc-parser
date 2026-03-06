---
id: 19c__DBMS_SPD.ALTER_SQL_PLAN_DIRECTIVE
name: DBMS_SPD.ALTER_SQL_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPD
tags: [dbms_spd]
source_file: DBMS_SPD.html
---

# DBMS_SPD.ALTER_SQL_PLAN_DIRECTIVE

This procedure changes different attributes of a SQL plan directive.

## Syntax

```sql
DBMS_SPD.ALTER_SQL_PLAN_DIRECTIVE (
   directive_id        IN     NUMBER,
   attribute_name      IN     VARCHAR2,
   attribute_value     IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| directive_id | NUMBER | IN | SQL plan directive ID |
| attribute_name | VARCHAR2 | IN | ENABLED AUTO_DROP |
| attribute_value | VARCHAR2) | IN | Possible values: ENABLED: - If YES directive is enabled and may be used - If NO directive is not enabled and will not be used AUTO_DROP : - If YES directive will be dropped automatically if not used for SPD_RETENTION_WEEKS . This is the default behavior. - If NO directive will not be dropped automatically |

## Usage Notes

Syntax DBMS_SPD.ALTER_SQL_PLAN_DIRECTIVE ( directive_id IN NUMBER, attribute_name IN VARCHAR2, attribute_value IN VARCHAR2); Parameters Table 160-2 ALTER_SQL_PLAN_DIRECTIVE Procedure Parameters Parameter Description directive_id SQL plan directive ID attribute_name ENABLED AUTO_DROP attribute_value Possible values: ENABLED: - If YES directive is enabled and may be used - If NO directive is not enabled and will not be used AUTO_DROP : - If YES directive will be dropped automatically if not used for SPD_RETENTION_WEEKS . This is the default behavior. - If NO directive will not be dropped automatically Exceptions ORA-38171 INSUFFICIENT_PRIVILEGE : The user does not have proper privilege to perform the operation. ORA-28104 INVALID_INPUT : The input value is not valid. ORA-13158 OBJECT_DOES_NOT_EXIST : The specified object does not exist. Usage Notes The ADMINISTER SQL MANAGEMENT OBJECT privilege is required to execute this procedure. Examples BEGIN DBMS_SPD.ALTER_SQL_PLAN_DIRECTIVE (12345, 'STATE', 'PERMANENT'); END;