---
id: 19c__DBMS_ILM.STOP_ILM
name: DBMS_ILM.STOP_ILM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM
tags: [dbms_ilm]
source_file: DBMS_ILM.html
---

# DBMS_ILM.STOP_ILM

This procedure terminates ILM ADO jobs associated to a particular task Id or job name.

## Syntax

```sql
DBMS_ILM.STOP_ILM (
   task_id               IN         NUMBER,
   p_drop_running_jobs   IN         BOOLEAN  DEFAULT FALSE),
   p_jobname             IN         VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_id | NUMBER | IN | Number that uniquely identifies a particular ADO task |
| p_drop_running_jobs | BOOLEAN | IN | Determines whether running jobs are dropped |
| p_jobname | VARCHAR2 | IN | Name of job to be terminated |

## Usage Notes

Syntax DBMS_ILM.STOP_ILM ( task_id IN NUMBER, p_drop_running_jobs IN BOOLEAN DEFAULT FALSE), p_jobname IN VARCHAR2 DEFAULT NULL); Parameters Table 86-10 STOP_ILM Procedure Parameters Parameter Description task_id Number that uniquely identifies a particular ADO task p_drop_running_jobs Determines whether running jobs are dropped p_jobname Name of job to be terminated