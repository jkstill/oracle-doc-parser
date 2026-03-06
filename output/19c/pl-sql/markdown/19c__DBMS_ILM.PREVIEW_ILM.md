---
id: 19c__DBMS_ILM.PREVIEW_ILM
name: DBMS_ILM.PREVIEW_ILM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM
tags: [dbms_ilm]
source_file: DBMS_ILM.html
---

# DBMS_ILM.PREVIEW_ILM

This procedure evaluates the ADO policies on the objects specified using the ILM_SCOPE argument.

## Syntax

```sql
DBMS_ILM.PREVIEW_ILM (
   task_id           OUT    NUMBER,
  ilm_scope          IN     NUMBER DEFAULT SCOPE_SCHEMA);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_id | NUMBER | OUT | Identifies a particular ADO task |
| ilm_scope | NUMBER | IN | Identifies the scope of execution. Should be either SCOPE_DATABASE or SCOPE_SCHEMA as described in Constants |

## Usage Notes

It returns a number as task_id which identifies a particular ADO task. This can be used to view the results of the policy evaluation in the appropriate views depending on role and access ( USER_ILMTASKS or DBA_ILMTASKS , USER_ILMEVALUATIONDETAILS or DBA_ILMEVALUATIONDETAILS , USER_ILMRESULTS or DBA_ILMRESULTS ). The PREVIEW_ILM procedure leaves the ADO task in an inactive state. Once you have previewed the results, you can add or delete objects to this task. Syntax DBMS_ILM.PREVIEW_ILM ( task_id OUT NUMBER, ilm_scope IN NUMBER DEFAULT SCOPE_SCHEMA); Parameters Table 86-8 PREVIEW_ILM Procedure Parameters Parameter Description task_id Identifies a particular ADO task ilm_scope Identifies the scope of execution. Should be either SCOPE_DATABASE or SCOPE_SCHEMA as described in Constants