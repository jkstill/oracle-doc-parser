---
id: 19c__DBMS_ILM.REMOVE_FROM_ILM
name: DBMS_ILM.REMOVE_FROM_ILM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM
tags: [dbms_ilm]
source_file: DBMS_ILM.html
---

# DBMS_ILM.REMOVE_FROM_ILM

This procedure removes the object specified through the argument from a particular ADO task.

## Syntax

```sql
DBMS_ILM.REMOVE_FROM_ILM (
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

The procedure can only be executed on an ADO task in an inactive state. Syntax DBMS_ILM.REMOVE_FROM_ILM ( task_id IN NUMBER, owner IN VARCHAR2, object_name IN VARCHAR2, subobject_name IN VARCHAR2 DEFAULT NULL); Parameters Table 86-9 REMOVE_FROM_ILM Procedure Parameters Parameter Description task_id Identifies a particular ADO task owner Owner of the object object_name Name of the object subobject_name Name of the subobject (partition name in the case of partitioned tables)