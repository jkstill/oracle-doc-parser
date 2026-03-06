---
id: 19c__DBMS_UTILITY.VALIDATE
name: DBMS_UTILITY.VALIDATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.VALIDATE

This procedure makes invalid database objects valid.

## Syntax

```sql
DBMS_UTILITY.VALIDATE(
    object_id       NUMBER);

DBMS_UTILITY.VALIDATE(
   owner          VARCHAR2, 
   objname        VARCHAR2, 
   namespace      NUMBER,   edition_name   := SYS_CONTEXT ('USERENV', 'CURRENT_EDITION'));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Name of the user who owns the object. Same as the OWNER field in ALL_OBJECTS . |
| objname | VARCHAR2 | IN | Name of the object to be validated. Same as the OBJECT_NAME field in ALL_OBJECTS . |
| namespace | NUMBER | IN | Namespace of the object. Same as the namespace field in obj$ . Equivalent numeric values are as follows: 1 — TABLE / PROCEDURE / TYPE 2 — BODY 3 — TRIGGER 4 — INDEX 5 — CLUSTER 8 — LOB 9 — DIRECTORY 10 — QUEUE 11 — REPLICATION OBJECT GROUP 12 — REPLICATION PROPAGATOR 13 — JAVA SOURCE 14 — JAVA RESOURCE 58 — (Data Mining) MODEL |
| edition_name |  |  | [Note: Currently not operable. Reserved for future use] |

## Usage Notes

Syntax DBMS_UTILITY.VALIDATE( object_id NUMBER); DBMS_UTILITY.VALIDATE( owner VARCHAR2, objname VARCHAR2, namespace NUMBER, edition_name := SYS_CONTEXT ('USERENV', 'CURRENT_EDITION')); Parameters Table 187-34 VALIDATE Procedure Parameters Parameter Description owner Name of the user who owns the object. Same as the OWNER field in ALL_OBJECTS . objname Name of the object to be validated. Same as the OBJECT_NAME field in ALL_OBJECTS . namespace Namespace of the object. Same as the namespace field in obj$ . Equivalent numeric values are as follows: 1 — TABLE / PROCEDURE / TYPE 2 — BODY 3 — TRIGGER 4 — INDEX 5 — CLUSTER 8 — LOB 9 — DIRECTORY 10 — QUEUE 11 — REPLICATION OBJECT GROUP 12 — REPLICATION PROPAGATOR 13 — JAVA SOURCE 14 — JAVA RESOURCE 58 — (Data Mining) MODEL edition_name [Note: Currently not operable. Reserved for future use] Usage Notes No errors are raised if the object does not exist or is already valid or is an object that cannot be validated. If the object being validated is not actual in the specified edition, the subprogram automatically switches into the edition in which the object is actual prior to validation. That is, a call to VALIDATE will not actualize the object in the specified edition. The INVALIDATE Procedure invalidates a database object and optionally changes its PL/SQL compiler parameter settings. The object to be invalidated is specified by its object_id . The subprogram automatically switches to the edition in which the object is actual prior to invalidation. That is, a call to INVALIDATE will not actualize the object in the current edition.