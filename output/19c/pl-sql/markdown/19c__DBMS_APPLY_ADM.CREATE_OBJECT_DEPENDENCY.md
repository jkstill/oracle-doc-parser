---
id: 19c__DBMS_APPLY_ADM.CREATE_OBJECT_DEPENDENCY
name: DBMS_APPLY_ADM.CREATE_OBJECT_DEPENDENCY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.CREATE_OBJECT_DEPENDENCY

This procedure creates an object dependency. An object dependency is a virtual dependency definition that defines a parent-child relationship between two objects at a destination database.

## Syntax

```sql
DBMS_APPLY_ADM.CREATE_OBJECT_DEPENDENCY(
   object_name         IN  VARCHAR2,
   parent_object_name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name | VARCHAR2 | IN | The name of the child database object, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| parent_object_name | VARCHAR2) | IN | The name of the parent database object, specified as [ schema_name .] object_name . For example, hr.departments . If the schema is not specified, then the current user is the default. |

## Usage Notes

An apply component schedules execution of transactions that involve the child object after all transactions with a lower commit system change number (commit SCN) that involve the parent object have been committed. An apply component uses the object identifier of the objects in the logical change records (LCRs) to detect dependencies. The apply component does not use column values in the LCRs to detect dependencies. Note: An error is raised if NULL is specified for either of the procedure parameters. See Also: DROP_OBJECT_DEPENDENCY Procedure Note: An error is raised if NULL is specified for either of the procedure parameters. See Also: DROP_OBJECT_DEPENDENCY Procedure Syntax DBMS_APPLY_ADM.CREATE_OBJECT_DEPENDENCY( object_name IN VARCHAR2, parent_object_name IN VARCHAR2); Parameters Table 21-6 CREATE_OBJECT_DEPENDENCY Procedure Parameters Parameter Description object_name The name of the child database object, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. parent_object_name The name of the parent database object, specified as [ schema_name .] object_name . For example, hr.departments . If the schema is not specified, then the current user is the default.