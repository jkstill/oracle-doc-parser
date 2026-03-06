---
id: 19c__DBMS_SCHEDULER.REMOVE_FROM_INCOMPATIBILITY
name: DBMS_SCHEDULER.REMOVE_FROM_INCOMPATIBILITY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.REMOVE_FROM_INCOMPATIBILITY

This procedure removes jobs or programs from an existing incompatibility definition.

## Syntax

```sql
DBMS_SCHEDULER.REMOVE_FROM_INCOMPATIBILITY (
   incompatibility_name    IN VARCHAR2,
   object_name             IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| incompatibility_name | VARCHAR2 | IN | The name of the incompatibility definition. |
| object_name | VARCHAR2) | IN | One or more (comma-separated) programs or jobs |

## Usage Notes

Syntax DBMS_SCHEDULER.REMOVE_FROM_INCOMPATIBILITY ( incompatibility_name IN VARCHAR2, object_name IN VARCHAR2); Parameters Table 151-74 REMOVE_FROM_INCOMPATIBILITY Procedure Parameters Parameter Description incompatibility_name The name of the incompatibility definition. object_name One or more (comma-separated) programs or jobs Usage Notes This procedure does not raise an error if any specified objects do not already exist in the incompatibility definition. See Also: Using Incompatibility Definitions in Oracle Database Administrator’s Guide See Also: Using Incompatibility Definitions in Oracle Database Administrator’s Guide