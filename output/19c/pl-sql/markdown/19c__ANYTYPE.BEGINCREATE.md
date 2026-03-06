---
id: 19c__ANYTYPE.BEGINCREATE
name: ANYTYPE.BEGINCREATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYTYPE
tags: [anytype]
source_file: ANYTYPE-TYPE.html
---

# ANYTYPE.BEGINCREATE

This procedure creates a new instance of ANYTYPE which can be used to create a transient type description.

## Syntax

```sql
STATIC PROCEDURE BEGINCREATE(
   typecode       IN          PLS_INTEGER,
   atype          OUT NOCOPY  ANYTYPE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| typecode | PLS_INTEGER | IN | Use a constant from DBMS_TYPES package. Typecodes for user-defined type: DBMS_TYPES.TYPECODE_OBJECT DBMS_TYPES.TYPECODE_VARRAY or DBMS_TYPES.TYPECODE_TABLE Typecodes for builtin types: DBMS_TYPES.TYPECODE_NUMBER, and similar types. |
| atype | NOCOPY | OUT | ANYTYPE for a transient type |

## Usage Notes

Syntax STATIC PROCEDURE BEGINCREATE( typecode IN PLS_INTEGER, atype OUT NOCOPY ANYTYPE); Parameters Table 282-2 BEGINCREATE Procedure Parameters Parameter Description typecode Use a constant from DBMS_TYPES package. Typecodes for user-defined type: DBMS_TYPES.TYPECODE_OBJECT DBMS_TYPES.TYPECODE_VARRAY or DBMS_TYPES.TYPECODE_TABLE Typecodes for builtin types: DBMS_TYPES.TYPECODE_NUMBER, and similar types. atype ANYTYPE for a transient type