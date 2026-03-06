---
id: 19c__DBMS_SCHEDULER.SET_ATTRIBUTE_NULL
name: DBMS_SCHEDULER.SET_ATTRIBUTE_NULL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.SET_ATTRIBUTE_NULL

This procedure sets an attribute of an object to NULL .

## Syntax

```sql
DBMS_SCHEDULER.SET_ATTRIBUTE_NULL (
   name              IN VARCHAR2,
   attribute         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The name of the object |
| attribute | VARCHAR2) | IN | The attribute being changed |

## Usage Notes

The attributes that can be set depend on the object being altered. If the object is enabled, it is disabled before being altered and reenabled afterward. If the object cannot be reenabled, an error is generated and the object is left in a disabled state. Syntax DBMS_SCHEDULER.SET_ATTRIBUTE_NULL ( name IN VARCHAR2, attribute IN VARCHAR2); Parameters Table 151-96 SET_ATTRIBUTE_NULL Procedure Parameters Parameter Description name The name of the object attribute The attribute being changed Usage Notes To run SET_ATTRIBUTE_NULL for a window, group of type WINDOW , or job class, you must have the MANAGE SCHEDULER privilege. Otherwise, you must be the owner of the object being altered or have ALTER privileges on that object or have the CREATE ANY JOB privilege.