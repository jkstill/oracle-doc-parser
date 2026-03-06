---
id: 19c__DBMS_SHARED_POOL.UNKEEP
name: DBMS_SHARED_POOL.UNKEEP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SHARED_POOL
tags: [dbms_shared_pool]
source_file: DBMS_SHARED_POOL.html
---

# DBMS_SHARED_POOL.UNKEEP

This procedure unkeeps the named object.

## Syntax

```sql
DBMS_SHARED_POOL.UNKEEP (
   name         VARCHAR2, 
   flag         CHAR DEFAULT 'P');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The name of the object to unkeep. |
| flag | CHAR | IN | A character string indicating what kind of object to keep the name identifies. The string is not case sensitive. This parameter is optional. If the parameter is not specified, the package assumes that the first parameter is the name of a package/procedure/function and will resolve the name. |
| schema |  |  | The user name or the schema to which the object belongs to. |
| objname |  |  | The name of the object to unkeep. |
| namespace |  |  | A number that indicates the library cache namespace in which the object has to be searched for. |
| edition_name |  |  | The name of the edition that the target object resides in. This parameter is optional. |
| hash |  |  | A 16-byte hash value for the object. |

## Usage Notes

Syntax DBMS_SHARED_POOL.UNKEEP ( name VARCHAR2, flag CHAR DEFAULT 'P'); DBMS_SHARED_POOL.UNKEEP ( schema VARCHAR2, objname VARCHAR2, namespace NUMBER, edition_name VARCHAR2 DEFAULT NULL); DBMS_SHARED_POOL.UNKEEP ( hash VARCHAR2, namespace NUMBER); WARNING: This procedure may not be supported in the future if automatic mechanisms are implemented to make this unnecessary. WARNING: This procedure may not be supported in the future if automatic mechanisms are implemented to make this unnecessary. Parameters Table 157-7 UNKEEP Procedure Parameters Parameter Description name The name of the object to unkeep. flag A character string indicating what kind of object to keep the name identifies. The string is not case sensitive. This parameter is optional. If the parameter is not specified, the package assumes that the first parameter is the name of a package/procedure/function and will resolve the name. schema The user name or the schema to which the object belongs to. objname The name of the object to unkeep. namespace A number that indicates the library cache namespace in which the object has to be searched for. edition_name The name of the edition that the target object resides in. This parameter is optional. hash A 16-byte hash value for the object. Exceptions ORA-06502 : An exception is raised if the named object cannot be found