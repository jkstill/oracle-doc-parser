---
id: 19c__DBMS_SHARED_POOL.KEEP
name: DBMS_SHARED_POOL.KEEP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SHARED_POOL
tags: [dbms_shared_pool]
source_file: DBMS_SHARED_POOL.html
---

# DBMS_SHARED_POOL.KEEP

This procedure keeps an object in the shared pool. Once an object has been kept in the shared pool, it is not subject to aging out of the pool. This may be useful for frequently used large objects. When large objects are brought into the shared pool, several objects may need to be aged out to create a contiguous area large enough.

## Syntax

```sql
DBMS_SHARED_POOL.KEEP (
   name         VARCHAR2, 
   flag         CHAR DEFAULT 'P');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The name of the object to keep. |
| flag | CHAR | IN | A character string indicating what kind of object to keep the name identifies. The string is not case sensitive. This parameter is optional. If the parameter is not specified, the package assumes that the first parameter is the name of a package/procedure/function and will resolve the name. Set to 'P' or 'p' to fully specify that the input is the name of a package/procedure/function. Set to 'Q' or 'q' to specify that the input is the name of a sequence. Set to 'R' or 'r' to specify that the input is the name of a trigger. Set to 'T' or 't' to specify that the input is the name of a type. Set to 'JS' or 'js' to specify that the input is the name of a java source. Set to 'JC' or 'jc' to specify that the input is the name of a java class. Set to 'JD' or 'jd' to specify that the input is the name of a java shared data. Set to 'C' or 'c' to specify that the input is the name of a cursor. |
| schema |  |  | The user name or the schema to which the object belongs to. |
| objname |  |  | The name of the object to keep. |
| namespace |  |  | A number indicating the library cache namespace in which the object has to be searched for. |
| heaps |  |  | The heaps to keep. For example, if heap 0 and heap 6 are to be kept. |
| edition_name |  |  | The name of the edition that the target object resides in. This parameter is optional. |
| hash |  |  | A 16-byte hash value for the object. |

## Usage Notes

Syntax DBMS_SHARED_POOL.KEEP ( name VARCHAR2, flag CHAR DEFAULT 'P'); DBMS_SHARED_POOL.KEEP ( schema VARCHAR2, objname VARCHAR2, namespace NUMBER, heaps NUMBER, edition_name VARCHAR2 DEFAULT NULL); DBMS_SHARED_POOL.KEEP ( hash VARCHAR2, namespace NUMBER, heaps NUMBER); Parameters Table 157-3 KEEP Procedure Parameters Parameter Description name The name of the object to keep. flag A character string indicating what kind of object to keep the name identifies. The string is not case sensitive. This parameter is optional. If the parameter is not specified, the package assumes that the first parameter is the name of a package/procedure/function and will resolve the name. Set to 'P' or 'p' to fully specify that the input is the name of a package/procedure/function. Set to 'Q' or 'q' to specify that the input is the name of a sequence. Set to 'R' or 'r' to specify that the input is the name of a trigger. Set to 'T' or 't' to specify that the input is the name of a type. Set to 'JS' or 'js' to specify that the input is the name of a java source. Set to 'JC' or 'jc' to specify that the input is the name of a java class. Set to 'JD' or 'jd' to specify that the input is the name of a java shared data. Set to 'C' or 'c' to specify that the input is the name of a cursor. schema The user name or the schema to which the object belongs to. objname The name of the object to keep. namespace A number indicating the library cache namespace in which the object has to be searched for. heaps The heaps to keep. For example, if heap 0 and heap 6 are to be kept. edition_name The name of the edition that the target object resides in. This parameter is optional. hash A 16-byte hash value for the object. Exceptions An exception is raised if the named object is not found. Usage Notes There are two kinds of objects: PL/SQL objects, triggers, sequences, types, and Java objects, which are specified by name. SQL cursor objects which are specified by a two-part number (indicating a location in the shared pool). For example: DBMS_SHARED_POOL.KEEP('scott.hispackage') This keeps package HISPACKAGE , owned by SCOTT . The names for PL/SQL objects follow SQL rules for naming objects (for example, delimited identifiers and multibyte names are allowed). A cursor can be kept by DBMS_SHARED_POOL . KEEP('0034CDFF, 20348871','C') , 0034CDFF being the ADDRESS and 20348871 the HASH_VALUE . Note that the complete hexadecimal address must be in the first 8 characters.