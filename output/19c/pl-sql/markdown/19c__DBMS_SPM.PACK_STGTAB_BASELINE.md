---
id: 19c__DBMS_SPM.PACK_STGTAB_BASELINE
name: DBMS_SPM.PACK_STGTAB_BASELINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.PACK_STGTAB_BASELINE

This function packs (exports) SQL plan baselines from SQL management base into a staging table.

## Syntax

```sql
DBMS_SPM.PACK_STGTAB_BASELINE (
   table_name       IN VARCHAR2,
   table_owner      IN VARCHAR2 := NULL,
   sql_handle       IN VARCHAR2 := NULL,
   plan_name        IN VARCHAR2 := NULL,
   sql_text         IN CLOB     := NULL,
   creator          IN VARCHAR2 := NULL,   origin           IN VARCHAR2 := NULL,
   enabled          IN VARCHAR2 := NULL,
   accepted         IN VARCHAR2 := NULL,
   fixed            IN VARCHAR2 := NULL,
   module           IN VARCHAR2 := NULL,
   action           IN VARCHAR2 := NULL)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | Name of staging table into which SQL plan baselines are packed (case insensitive unless double quoted) |
| table_owner | VARCHAR2 | IN | Name of staging table owner.Default NULL means current schema is the table owner |
| sql_handle | VARCHAR2 | IN | SQL handle (case sensitive) |
| plan_name | VARCHAR2 | IN | Plan name (case sensitive, % wildcards accepted) |
| sql_text | CLOB | IN | SQL text string (case sensitive, % wildcards accepted) |
| creator | VARCHAR2 | IN | Creator of SQL plan baseline (case insensitive unless double quoted) |
| origin | VARCHAR2 | IN | Origin of SQL plan baseline, should be 'MANUAL-LOAD' , 'AUTO-CAPTURE' , 'MANUAL_SQLTUNE' or 'AUTO-SQLTUNE' (case insensitive) |
| enabled | VARCHAR2 | IN | Must be ' YES ' or ' NO ' (case insensitive) |
| accepted | VARCHAR2 | IN | Must be ' YES ' or ' NO ' (case insensitive) |
| fixed | VARCHAR2 | IN | Must be ' YES ' or ' NO ' (case insensitive) |
| module | VARCHAR2 | IN | Module (case sensitive) |
| action | VARCHAR2 | IN | Action (case sensitive) |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SPM.PACK_STGTAB_BASELINE ( table_name IN VARCHAR2, table_owner IN VARCHAR2 := NULL, sql_handle IN VARCHAR2 := NULL, plan_name IN VARCHAR2 := NULL, sql_text IN CLOB := NULL, creator IN VARCHAR2 := NULL, origin IN VARCHAR2 := NULL, enabled IN VARCHAR2 := NULL, accepted IN VARCHAR2 := NULL, fixed IN VARCHAR2 := NULL, module IN VARCHAR2 := NULL, action IN VARCHAR2 := NULL) RETURN NUMBER; Parameters Table 161-22 PACK_STGTAB_BASELINE Function Parameters Parameter Description table_name Name of staging table into which SQL plan baselines are packed (case insensitive unless double quoted) table_owner Name of staging table owner.Default NULL means current schema is the table owner sql_handle SQL handle (case sensitive) plan_name Plan name (case sensitive, % wildcards accepted) sql_text SQL text string (case sensitive, % wildcards accepted) creator Creator of SQL plan baseline (case insensitive unless double quoted) origin Origin of SQL plan baseline, should be 'MANUAL-LOAD' , 'AUTO-CAPTURE' , 'MANUAL_SQLTUNE' or 'AUTO-SQLTUNE' (case insensitive) enabled Must be ' YES ' or ' NO ' (case insensitive) accepted Must be ' YES ' or ' NO ' (case insensitive) fixed Must be ' YES ' or ' NO ' (case insensitive) module Module (case sensitive) action Action (case sensitive) Return Values Number of SQL plan baselines packed