---
id: 19c__DBMS_SCHEDULER.DROP_RESOURCE
name: DBMS_SCHEDULER.DROP_RESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_RESOURCE

This procedure drops a resource.

## Syntax

```sql
DBMS_SCHEDULER.DROP_RESOURCE (
   resource_name  IN VARCHAR2,
   force          IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| resource_name | VARCHAR2 | IN | The name of the resource to be dropped. Can be a comma-delimited list. |
| force | BOOLEAN | IN | If force is set to FALSE , the resource must not have any existing constraints, otherwise an error occurs. If force is set to TRUE , the resource will be dropped and any constraints defined on this resource will also be dropped. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_RESOURCE ( resource_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-56 DROP_RESOURCE Procedure Parameters Parameter Description resource_name The name of the resource to be dropped. Can be a comma-delimited list. force If force is set to FALSE , the resource must not have any existing constraints, otherwise an error occurs. If force is set to TRUE , the resource will be dropped and any constraints defined on this resource will also be dropped. Usage Notes Only the owner or a user with the CREATE ANY JOB system privilege may drop the resource. See Also: Creating or Dropping a Resource in Oracle Database Administrator’s Guide See Also: Creating or Dropping a Resource in Oracle Database Administrator’s Guide