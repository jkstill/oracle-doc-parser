---
id: 19c__DBMS_SHARED_POOL.MARKHOT
name: DBMS_SHARED_POOL.MARKHOT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SHARED_POOL
tags: [dbms_shared_pool]
source_file: DBMS_SHARED_POOL.html
---

# DBMS_SHARED_POOL.MARKHOT

This procedure marks a library cache object as a hot object.

## Syntax

```sql
DBMS_SHARED_POOL.MARKHOT (
   schema         VARCHAR2, 
   objname        VARCHAR2,
   namespace      NUMBER DEFAULT 1,   
   global         BOOLEAN DEFAULT TRUE,
   edition_name   VARCHAR2 DEFAULT NULL);

DBMS_SHARED_POOL.MARKHOT (
   hash          VARCHAR2, 
   namespace     NUMBER DEFAULT 1,
   global        BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2 | IN | User name or the schema to which the object belongs |
| objname | VARCHAR2 | IN | Name of the object |
| namespace | NUMBER | IN | Number indicating the library cache namespace in which the object is to be searched. Views, such as USER_OBJECTS and DBA_OBJECTS , reflect the namespace as a number column, as do most dictionary tables such as OBJ$ . |
| global | BOOLEAN | IN | If TRUE (default), mark the object hot on all Oracle RAC instances |
| hash | VARCHAR2 | IN | 16-byte hash value for the object |
| edition_name | VARCHAR2 | IN | Denotes the name of the edition that the target object resides in. This parameter is optional. |

## Usage Notes

Syntax DBMS_SHARED_POOL.MARKHOT ( schema VARCHAR2, objname VARCHAR2, namespace NUMBER DEFAULT 1, global BOOLEAN DEFAULT TRUE, edition_name VARCHAR2 DEFAULT NULL); DBMS_SHARED_POOL.MARKHOT ( hash VARCHAR2, namespace NUMBER DEFAULT 1, global BOOLEAN DEFAULT TRUE); Parameters Table 157-4 MARKHOT Procedure Parameters Parameter Description schema User name or the schema to which the object belongs objname Name of the object namespace Number indicating the library cache namespace in which the object is to be searched. Views, such as USER_OBJECTS and DBA_OBJECTS , reflect the namespace as a number column, as do most dictionary tables such as OBJ$ . global If TRUE (default), mark the object hot on all Oracle RAC instances hash 16-byte hash value for the object edition_name Denotes the name of the edition that the target object resides in. This parameter is optional. Exceptions ORA-06502 : An exception is raised if the named object cannot be found due to incorrect input ORA-04043 : An exception is raised if the named object cannot be found (bad namespace, or hash input) Usage Notes If a package or type's specification is marked hot or unhot, then the corresponding package or type body will be implicitly marked as hot or unhot. Users can examine column, V$DB_OBJECT_CACHE.PROPERTY , to see whether or not the object has been marked hot. The values for PROPERTY are: HOTCOPYnnn - An object that is a hot copy with integer identifier of 'nnn'. For example, HOTCOPY5 , HOTCOPY94 , and HOTCOPY125 . HOTCOPY -As above but the identifier is unknown HOT -The "root" kgl object that has been marked as hot NULL -A normal object