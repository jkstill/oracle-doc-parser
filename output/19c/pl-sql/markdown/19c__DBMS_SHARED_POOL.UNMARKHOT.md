---
id: 19c__DBMS_SHARED_POOL.UNMARKHOT
name: DBMS_SHARED_POOL.UNMARKHOT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SHARED_POOL
tags: [dbms_shared_pool]
source_file: DBMS_SHARED_POOL.html
---

# DBMS_SHARED_POOL.UNMARKHOT

This procedure unmarks a library cache object as a hot object.

## Syntax

```sql
DBMS_SHARED_POOL.UNMARKHOT (
   schema         VARCHAR2, 
   objname        VARCHAR2,
   namespace      NUMBER  DEFAULT 1, 
   global         BOOLEAN DEFAULT TRUE,
   edition_name   VARCHAR2 DEFAULT NULL);

DBMS_SHARED_POOL.UNMARKHOT (
   hash          VARCHAR2, 
   namespace     NUMBER DEFAULT 1,
   global        BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2 | IN | User name or the schema to which the object belongs |
| objname | VARCHAR2 | IN | Name of the object |
| namespace | NUMBER | IN | Number indicating the library cache namespace in which the object is to be searched |
| global | BOOLEAN | IN | If TRUE , unmark the object hot on all Oracle RAC instances. The default value of this parameter is TRUE . |
| hash | VARCHAR2 | IN | A 16-byte hash value for the object |
| edition_name | VARCHAR2 | IN | Denotes the name of the edition that the target object resides in. This parameter is optional. |

## Usage Notes

Syntax DBMS_SHARED_POOL.UNMARKHOT ( schema VARCHAR2, objname VARCHAR2, namespace NUMBER DEFAULT 1, global BOOLEAN DEFAULT TRUE, edition_name VARCHAR2 DEFAULT NULL); DBMS_SHARED_POOL.UNMARKHOT ( hash VARCHAR2, namespace NUMBER DEFAULT 1, global BOOLEAN DEFAULT TRUE); Parameters Table 157-8 UNMARKHOT Procedure Parameters Parameter Description schema User name or the schema to which the object belongs objname Name of the object namespace Number indicating the library cache namespace in which the object is to be searched global If TRUE , unmark the object hot on all Oracle RAC instances. The default value of this parameter is TRUE . hash A 16-byte hash value for the object edition_name Denotes the name of the edition that the target object resides in. This parameter is optional. Exceptions ORA-06502 : An exception is raised if the named object cannot be found due to incorrect input ORA-04043 : An exception is raised if the named object cannot be found (bad namespace, or hash input, or non-existent object) Usage Notes If a package or type's specification is marked hot or unhot, then the corresponding package or type body will be implicitly marked as hot or unhot.