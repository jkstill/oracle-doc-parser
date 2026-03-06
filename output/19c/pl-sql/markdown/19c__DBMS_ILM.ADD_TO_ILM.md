---
id: 19c__DBMS_ILM.ADD_TO_ILM
name: DBMS_ILM.ADD_TO_ILM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM
tags: [dbms_ilm]
source_file: DBMS_ILM.html
---

# DBMS_ILM.ADD_TO_ILM

This procedure adds the object specified through the argument to a particular ADO task and evaluates the ADO policies on this object.

## Syntax

```sql
DBMS_ILM.ADD_TO_ILM (
   task_id           IN    NUMBER,
   owner             IN    VARCHAR2,
   object_name       IN    VARCHAR2,
   subobject_name    IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_id | NUMBER | IN | Identifies a particular ADO task |
| owner | VARCHAR2 | IN | Owner of the object |
| object_name | VARCHAR2 | IN | Name of the object |
| subobject_name | VARCHAR2 | IN | Name of the subobject (partition name in the case of partitioned tables) |

## Usage Notes

The procedure can only be executed on an ADO task in an inactive state. The results of the ADO policy evaluation on this object can be viewed using the appropriate views depending on role and access ( USER_ILMTASKS or DBA_ILMTASKS , USER_ILMEVALUATIONDETAILS or DBA_ILMEVALUATIONDETAILS , USER_ILMRESULTS or DBA_ILMRESULTS ). Syntax DBMS_ILM.ADD_TO_ILM ( task_id IN NUMBER, owner IN VARCHAR2, object_name IN VARCHAR2, subobject_name IN VARCHAR2 DEFAULT NULL); Parameters Table 86-4 ADD_TO_ILM Procedure Parameters Parameter Description task_id Identifies a particular ADO task owner Owner of the object object_name Name of the object subobject_name Name of the subobject (partition name in the case of partitioned tables)