---
id: 19c__DBMS_SCHEDULER.ADD_TO_INCOMPATIBILITY
name: DBMS_SCHEDULER.ADD_TO_INCOMPATIBILITY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.ADD_TO_INCOMPATIBILITY

This procedure adds jobs or programs to an existing incompatibility definition.

## Syntax

```sql
DBMS_SCHEDULER.ADD_TO_INCOMPATIBILITY (
   incompatibility_name    IN VARCHAR2,
   object_name             IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| incompatibility_name | VARCHAR2 | IN | The name of the incompatibility definition. |
| object_name | VARCHAR2) | IN | One or more (comma-separated) programs or jobs |

## Usage Notes

Syntax DBMS_SCHEDULER.ADD_TO_INCOMPATIBILITY ( incompatibility_name IN VARCHAR2, object_name IN VARCHAR2); Parameters Table 151-16 ADD_TO_INCOMPATIBILITY Procedure Parameters Parameter Description incompatibility_name The name of the incompatibility definition. object_name One or more (comma-separated) programs or jobs Usage Notes This procedure does not raise an error if any specified objects already exist in the incompatibility definition. See Also: Using Incompatibility Definitions in Oracle Database Administrator’s Guide See Also: Using Incompatibility Definitions in Oracle Database Administrator’s Guide