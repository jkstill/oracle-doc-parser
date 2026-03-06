---
id: 19c__DBMS_SHARED_POOL.PURGE
name: DBMS_SHARED_POOL.PURGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SHARED_POOL
tags: [dbms_shared_pool]
source_file: DBMS_SHARED_POOL.html
---

# DBMS_SHARED_POOL.PURGE

This procedure purges the named object or specified heaps of the object.

## Syntax

```sql
DBMS_SHARED_POOL.PURGE (
   name         VARCHAR2, 
   flag         CHAR DEFAULT 'P', 
   heaps        NUMBER DEFAULT 1);

DBMS_SHARED_POOL.PURGE (
   schema       VARCHAR2,
   objname      VARCHAR2,
   namespace    NUMBER,
   heaps        NUMBER,
   edition_name VARCHAR2 DEFAULT NULL);

DBMS_SHARED_POOL.PURGE (
   hash         VARCHAR2,
   namespace    NUMBER,
   heaps        NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the object to purge. The value for this identifier is the concatenation of the address and hash_value columns from the v$sqlarea view. This is displayed by the SIZES procedure. Currently, TABLE and VIEW objects may not be purged. |
| flag | CHAR | IN | (Optional) If this is not specified, then the package assumes that the first parameter is the name of a package/procedure/function and resolves the name. Set to 'P' or 'p' to fully specify that the input is the name of a package/procedure/function. Set to 'T' or 't' to specify that the input is the name of a type. Set to 'R' or 'r' to specify that the input is the name of a trigger. Set to 'Q' or 'q' to specify that the input is the name of a sequence. In case the first argument is a cursor address and hash-value, the parameter should be set to any character except 'P' or 'p' or 'Q' or 'q' or 'R' or 'r' or 'T' or 't'. |
| heaps | NUMBER | IN | Heaps to be purged. For example, if heap 0 and heap 6 are to be purged: 1<<0 | 1<<6 => hex 0x41 => decimal 65, so specify heaps =>65. Default value is 1 , that is, heap 0 which means the whole object would be purged |
| schema | VARCHAR2 | IN | User name or the schema to which the object belongs |
| objname | VARCHAR2 | IN | Name of the object to purge |
| namespace | NUMBER | IN | Parameter is a number indicating the library cache namespace in which the object is to be searched |
| hash | VARCHAR2 | IN | 16-byte hash value for the object |
| edition_name | VARCHAR2 | IN | The name of the edition that the target object resides in. This parameter is optional. |

## Usage Notes

Syntax DBMS_SHARED_POOL.PURGE ( name VARCHAR2, flag CHAR DEFAULT 'P', heaps NUMBER DEFAULT 1); DBMS_SHARED_POOL.PURGE ( schema VARCHAR2, objname VARCHAR2, namespace NUMBER, heaps NUMBER, edition_name VARCHAR2 DEFAULT NULL); DBMS_SHARED_POOL.PURGE ( hash VARCHAR2, namespace NUMBER, heaps NUMBER); Parameters Table 157-5 PURGE Procedure Parameters Parameter Description name Name of the object to purge. The value for this identifier is the concatenation of the address and hash_value columns from the v$sqlarea view. This is displayed by the SIZES procedure. Currently, TABLE and VIEW objects may not be purged. flag (Optional) If this is not specified, then the package assumes that the first parameter is the name of a package/procedure/function and resolves the name. Set to 'P' or 'p' to fully specify that the input is the name of a package/procedure/function. Set to 'T' or 't' to specify that the input is the name of a type. Set to 'R' or 'r' to specify that the input is the name of a trigger. Set to 'Q' or 'q' to specify that the input is the name of a sequence. In case the first argument is a cursor address and hash-value, the parameter should be set to any character except 'P' or 'p' or 'Q' or 'q' or 'R' or 'r' or 'T' or 't'. heaps Heaps to be purged. For example, if heap 0 and heap 6 are to be purged: 1<<0 | 1<<6 => hex 0x41 => decimal 65, so specify heaps =>65. Default value is 1 , that is, heap 0 which means the whole object would be purged schema User name or the schema to which the object belongs objname Name of the object to purge namespace Parameter is a number indicating the library cache namespace in which the object is to be searched hash 16-byte hash value for the object edition_name The name of the edition that the target object resides in. This parameter is optional. Exceptions ORA-6570 : An exception is raised if the named object cannot be found ORA-6570 : An object cannot be purged it marked as permanently kept Usage Notes All objects supported by the KEEP Procedure are supported for PURGE .