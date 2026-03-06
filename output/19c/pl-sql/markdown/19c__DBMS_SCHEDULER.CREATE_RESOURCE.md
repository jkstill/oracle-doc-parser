---
id: 19c__DBMS_SCHEDULER.CREATE_RESOURCE
name: DBMS_SCHEDULER.CREATE_RESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_RESOURCE

This procedure allows users to specify the resources used by jobs or to create a new resource.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_RESOURCE (
  resource_name    IN VARCHAR2,
  units            IN PLS_INTEGER,
  status           IN VARCHAR2 DEFAULT 'ENFORCE_CONSTRAINTS',
  constraint_level IN VARCHAR2 DEFAULT 'JOB_LEVEL',
  comments         IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| resource_name | VARCHAR2 | IN | The name of the resource. |
| units | PLS_INTEGER | IN | The number of units of this resource that the job or program uses. |
| status | VARCHAR2 | IN | The status of the resource. ‘ENFORCE_CONSTRAINTS’. This is the default value, and when set, will force the scheduler to enforce resource limits. When the maximum number of units of this resource has been reached no additional jobs using this resource will get started. ‘IGNORE_CONSTRAINTS’. When set, the scheduler will ignore any constraints on this resource. ‘BLOCKED_ALL_JOBS’. No jobs having a constraint on this resource will be allowed to run. The resource is considered to be permanently blocking until switched to one of the other two states. |
| constraint_level | VARCHAR2 | IN | Level of the constraint: JOB_LEVEL or PROGRAM_LEVEL . For incompatibilities, for JOB_LEVEL , the incompatibility members must be jobs; for PROGRAM_LEVEL the incompatibility members must be programs. |
| comments | VARCHAR2 | IN | Descriptive comment about the resource. |

## Usage Notes

Syntax DBMS_SCHEDULER.CREATE_RESOURCE ( resource_name IN VARCHAR2, units IN PLS_INTEGER, status IN VARCHAR2 DEFAULT 'ENFORCE_CONSTRAINTS', constraint_level IN VARCHAR2 DEFAULT 'JOB_LEVEL', comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-32 CREATE_RESOURCE Procedure Parameters Parameter Description resource_name The name of the resource. units The number of units of this resource that the job or program uses. status The status of the resource. ‘ENFORCE_CONSTRAINTS’. This is the default value, and when set, will force the scheduler to enforce resource limits. When the maximum number of units of this resource has been reached no additional jobs using this resource will get started. ‘IGNORE_CONSTRAINTS’. When set, the scheduler will ignore any constraints on this resource. ‘BLOCKED_ALL_JOBS’. No jobs having a constraint on this resource will be allowed to run. The resource is considered to be permanently blocking until switched to one of the other two states. constraint_level Level of the constraint: JOB_LEVEL or PROGRAM_LEVEL . For incompatibilities, for JOB_LEVEL , the incompatibility members must be jobs; for PROGRAM_LEVEL the incompatibility members must be programs. comments Descriptive comment about the resource. Usage Notes The following example creates a new resource. BEGIN DBMS_SCHEDULER.CREATE_RESOURCE( resource_name => 'my_resource', units => 3, state => 'ENFORCE_CONSTRAINTS', comments => 'Resource1' ) END; / See Also: Creating or Dropping a Resource in Oracle Database Administrator’s Guide SET_RESOURCE_CONSTRAINT Procedure See Also: Creating or Dropping a Resource in Oracle Database Administrator’s Guide SET_RESOURCE_CONSTRAINT Procedure