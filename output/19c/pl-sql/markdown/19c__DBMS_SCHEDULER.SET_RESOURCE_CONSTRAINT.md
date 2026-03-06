---
id: 19c__DBMS_SCHEDULER.SET_RESOURCE_CONSTRAINT
name: DBMS_SCHEDULER.SET_RESOURCE_CONSTRAINT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.SET_RESOURCE_CONSTRAINT

This procedure allows users to specify the resources used by jobs.

## Syntax

```sql
DBMS_SCHEDULER.SET_RESOURCE_CONSTRAINT (
   object_name       IN VARCHAR2,
   resource_name     IN VARCHAR2,
   units             IN NUMBER DEFAULT 1);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name | VARCHAR2 | IN | The name of a program or a job, or a comma separated list of these objects. |
| resource_name | VARCHAR2 | IN | The name of the resource. |
| units | NUMBER | IN | The number of units of this resource that the job or program uses. |

## Usage Notes

Syntax DBMS_SCHEDULER.SET_RESOURCE_CONSTRAINT ( object_name IN VARCHAR2, resource_name IN VARCHAR2, units IN NUMBER DEFAULT 1); Parameters Table 151-100 SET_RESOURCE_CONSTRAINT Procedure Parameters Parameter Description object_name The name of a program or a job, or a comma separated list of these objects. resource_name The name of the resource. units The number of units of this resource that the job or program uses. Usages Notes object_name can be the name or comma-separated list of names of either programs or jobs. This creates a constraint on the named resource for these programs or jobs. units specifies the number of units of the resource that the program or job can use. If units is set to 0, then the program or job does not use this resource anymore, and the resulting constraint is deleted. Setting units to 0 on a resource with no previous constraint results in an error. When multiple constraints are defined on the same resource, the object types must match. When one or more existing constraints for a resource are based on jobs and a new constraint is added for the same resource that is based on a program (or vice versa) an error will be raised.