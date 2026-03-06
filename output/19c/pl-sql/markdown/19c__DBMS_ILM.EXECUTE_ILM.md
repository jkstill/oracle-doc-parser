---
id: 19c__DBMS_ILM.EXECUTE_ILM
name: DBMS_ILM.EXECUTE_ILM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM
tags: [dbms_ilm]
source_file: DBMS_ILM.html
---

# DBMS_ILM.EXECUTE_ILM

This procedure executes an ADO task.

## Syntax

```sql
DBMS_ILM.EXECUTE_ILM (
   task_id             OUT    NUMBER,
   ilm_scope           IN     NUMBER DEFAULT SCOPE_SCHEMA,
   execution_mode      IN     NUMBER DEFAULT ILM_EXECUTION_ONLINE);

DBMS_ILM.EXECUTE_ILM (
   owner               IN     VARCHAR2,
   object_name         IN     VARCHAR2,
   task_id             OUT    NUMBER, 
   subobject_name      IN     VARCHAR2 DEFAULT NULL,
   policy_name         IN     VARCHAR2 DEFAULT ILM_ALL_POLICIES,
   execution_mode      IN     NUMBER DEFAULT ILM_EXECUTION_ONLINE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_id | NUMBER | OUT | Identifies a particular ADO task |
| ilm_scope | NUMBER | IN | Determines the set of objects considered for ADO execution. The default is to consider only the objects in the schema. |
| execution_mode | NUMBER | IN | Whether the ADO task be executed online ( ILM_EXECUTION_ONLINE ) or offline ( ILM_EXECUTION_OFFLINE ) |
| owner | VARCHAR2 | IN | Owner of the object |
| object_name | VARCHAR2 | IN | Name of the object |
| subobject_name | VARCHAR2 | IN | Name of the subobject (partition name in the case of partitioned tables) |
| policy_name | VARCHAR2 | IN | Name of the ADO policy to be evaluated on the object. The package constant ILM_ALL_POLICIES should be used if all ADO policies on an object should be evaluated. |

## Usage Notes

There are two overloads to this procedure. The first overload executes an ADO task for a set of objects without having evaluated them previously. The second overload executes ADO policies for a specific object. Syntax DBMS_ILM.EXECUTE_ILM ( task_id OUT NUMBER, ilm_scope IN NUMBER DEFAULT SCOPE_SCHEMA, execution_mode IN NUMBER DEFAULT ILM_EXECUTION_ONLINE); DBMS_ILM.EXECUTE_ILM ( owner IN VARCHAR2, object_name IN VARCHAR2, task_id OUT NUMBER, subobject_name IN VARCHAR2 DEFAULT NULL, policy_name IN VARCHAR2 DEFAULT ILM_ALL_POLICIES, execution_mode IN NUMBER DEFAULT ILM_EXECUTION_ONLINE); Parameters Table 86-6 EXECUTE_ILM Procedure Parameters Parameter Description task_id Identifies a particular ADO task ilm_scope Determines the set of objects considered for ADO execution. The default is to consider only the objects in the schema. execution_mode Whether the ADO task be executed online ( ILM_EXECUTION_ONLINE ) or offline ( ILM_EXECUTION_OFFLINE ) owner Owner of the object object_name Name of the object subobject_name Name of the subobject (partition name in the case of partitioned tables) policy_name Name of the ADO policy to be evaluated on the object. The package constant ILM_ALL_POLICIES should be used if all ADO policies on an object should be evaluated. Usage Notes The EXECUTE_ILM procedure can be used by users who want more control of when ADO is performed, and who do not want to wait until the next maintenance window. The procedure executes like a DDL in that it auto commits before and after the ADO task and related jobs are created.