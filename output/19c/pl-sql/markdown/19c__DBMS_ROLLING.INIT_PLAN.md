---
id: 19c__DBMS_ROLLING.INIT_PLAN
name: DBMS_ROLLING.INIT_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROLLING
tags: [dbms_rolling]
source_file: DBMS_ROLLING.html
---

# DBMS_ROLLING.INIT_PLAN

This procedure initializes a rolling operation plan with system-generated default values.

## Syntax

```sql
DBMS_ROLLING.INIT_PLAN (
   future_primary   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| future_primary | VARCHAR2) | IN | DB_UNIQUE_NAME of the future primary (also known as the Leading Group Master (LGM)) |

## Usage Notes

Syntax DBMS_ROLLING.INIT_PLAN ( future_primary IN VARCHAR2); Parameters Table 147-2 INIT_PLAN Procedure Parameters Parameter Description future_primary DB_UNIQUE_NAME of the future primary (also known as the Leading Group Master (LGM)) Exceptions ORA-45400 : operation not permitted on current database ORA-45401 : upgrade plan is already active ORA-45402 : LOG_ARCHIVE_CONFIG must contain the DG_CONFIG attribute ORA-45403 : database %s must be specified in DG_CONFIG ORA-45411 : operation requires additional arguments ORA-65040 : operation not allowed from within a pluggable database Usage Notes A plan must be prepared before any parameters can be customized.