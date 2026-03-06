---
id: 19c__ANYTYPE.SETINFO
name: ANYTYPE.SETINFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYTYPE
tags: [anytype]
source_file: ANYTYPE-TYPE.html
---

# ANYTYPE.SETINFO

This procedure sets any additional information required for constructing a COLLECTION or builtin type.

## Syntax

```sql
MEMBER PROCEDURE SETINFO(
   self          IN OUT NOCOPY ANYTYPE,
   prec          IN PLS_INTEGER,
   scale         IN PLS_INTEGER,
   len           IN PLS_INTEGER,
   csid          IN PLS_INTEGER,
   csfrm         IN PLS_INTEGER,
   atype         IN ANYTYPE DEFAULT NULL,
   elem_tc       IN PLS_INTEGER DEFAULT NULL,
   elem_count    IN PLS_INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | The transient ANYTYPE that is being constructed. |
| prec | PLS_INTEGER | IN | Optional.Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. |
| scale | PLS_INTEGER | IN | Optional.Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. |
| len | PLS_INTEGER | IN | Optional. Required if typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Gives length. |
| csid | PLS_INTEGER | IN | Required if typecode represents types requiring character information such as CHAR , VARCHAR , or VARCHAR2 . |
| csfrm | PLS_INTEGER | IN | Required if typecode represents types requiring character information such as CHAR , VARCHAR , or VARCHAR2 . |
| atype | ANYTYPE | IN | Optional. Required if collection element typecode is a user-defined type such as TYPECODE_OBJECT , and similar others. It is also required for a built-in type that needs user-defined type information such as TYPECODE_REF . This parameter is not needed otherwise. |

## Usage Notes

Syntax MEMBER PROCEDURE SETINFO( self IN OUT NOCOPY ANYTYPE, prec IN PLS_INTEGER, scale IN PLS_INTEGER, len IN PLS_INTEGER, csid IN PLS_INTEGER, csfrm IN PLS_INTEGER, atype IN ANYTYPE DEFAULT NULL, elem_tc IN PLS_INTEGER DEFAULT NULL, elem_count IN PLS_INTEGER DEFAULT 0); Parameters Table 282-3 SETINFO Procedure Parameters Parameter Description self The transient ANYTYPE that is being constructed. prec Optional.Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. scale Optional.Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. len Optional. Required if typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Gives length. csid Required if typecode represents types requiring character information such as CHAR , VARCHAR , or VARCHAR2 . csfrm Required if typecode represents types requiring character information such as CHAR , VARCHAR , or VARCHAR2 . atype Optional. Required if collection element typecode is a user-defined type such as TYPECODE_OBJECT , and similar others. It is also required for a built-in type that needs user-defined type information such as TYPECODE_REF . This parameter is not needed otherwise. The Following Parameters Are Required For Collection Types Exceptions DBMS_TYPES.INVALID_PARAMETER : Invalid Parameters (typecode, typeinfo) DBMS_TYPES.INCORRECT_USAGE : Incorrect usage (cannot call after calling ENDCREATE , and similar actions.) Usage Notes It is an error to call this function on an ANYTYPE that represents a persistent user defined type.