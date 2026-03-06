---
id: 19c__DBMS_SQLDIAG.INTERRUPT_DIAGNOSIS_TASK
name: DBMS_SQLDIAG.INTERRUPT_DIAGNOSIS_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.INTERRUPT_DIAGNOSIS_TASK

This procedure interrupts a diagnostic task.

## Syntax

```sql
DBMS_SQLDIAG.INTERRUPT_DIAGNOSIS_TASK (
    taskname        IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| taskname | VARCHAR2) | IN | Name of task |

## Usage Notes

Syntax DBMS_SQLDIAG.INTERRUPT_DIAGNOSIS_TASK ( taskname IN VARCHAR2); Parameters Table 165-27 INTERRUPT_DIAGNOSIS_TASK Procedure Parameters Parameter Description taskname Name of task