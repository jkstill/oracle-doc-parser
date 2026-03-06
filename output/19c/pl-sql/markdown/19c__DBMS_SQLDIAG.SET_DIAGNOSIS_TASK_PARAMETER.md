---
id: 19c__DBMS_SQLDIAG.SET_DIAGNOSIS_TASK_PARAMETER
name: DBMS_SQLDIAG.SET_DIAGNOSIS_TASK_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.SET_DIAGNOSIS_TASK_PARAMETER

This procedure is called to update the value of a SQL diagnosis parameter of type VARCHAR2 .

## Syntax

```sql
DBMS_SQLDIAG.SET_DIAGNOSIS_TASK_PARAMETER (
    taskname           IN   VARCHAR2,
    parameter          IN   VARCHAR2,    value              IN   NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| taskname | VARCHAR2 | IN | Identifier of the task to execute |
| parameter | VARCHAR2 | IN | Name of the parameter to set |
| value | NUMBER) | IN | New value of the specified parameter |

## Usage Notes

The task must be set to its initial state before calling this procedure. The diagnosis parameters that can be set by this procedure are: MODE : diag scope (comprehensive, limited) _SQLDIAG_FINDING_MODE : findings in the report (see " Table 165-8 " for possible values) Syntax DBMS_SQLDIAG.SET_DIAGNOSIS_TASK_PARAMETER ( taskname IN VARCHAR2, parameter IN VARCHAR2, value IN NUMBER); Parameters Table 165-34 SET_DIAGNOSIS_TASK_PARAMETER Procedure Parameters Parameter Description taskname Identifier of the task to execute parameter Name of the parameter to set value New value of the specified parameter