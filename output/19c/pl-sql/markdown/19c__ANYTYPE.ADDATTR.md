---
id: 19c__ANYTYPE.ADDATTR
name: ANYTYPE.ADDATTR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYTYPE
tags: [anytype]
source_file: ANYTYPE-TYPE.html
---

# ANYTYPE.ADDATTR

This procedure adds an attribute to an ANYTYPE (of typecode DBMS_TYPES . TYPECODE_OBJECT ).

## Syntax

```sql
MEMBER PROCEDURE ADDATTR(
   self          IN OUT NOCOPY ANYTYPE,
   aname         IN VARCHAR2,
   typecode      IN PLS_INTEGER,
   prec          IN PLS_INTEGER,
   scale         IN PLS_INTEGER,
   len           IN PLS_INTEGER,
   csid          IN PLS_INTEGER,
   csfrm         IN PLS_INTEGER,
   attr_type     IN ANYTYPE DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | The transient ANYTYPE that is being constructed. Must be of type DBMS_TYPES.TYPECODE_OBJECT. |
| aname | VARCHAR2 | IN | Optional. Attribute's name. Could be NULL . |
| typecode | PLS_INTEGER | IN | Attribute's typecode. Can be built-in or user-defined typecode (from DBMS_TYPES package). |
| prec | PLS_INTEGER | IN | Optional. Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. |
| scale | PLS_INTEGER | IN | Optional. Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. |
| len | PLS_INTEGER | IN | Optional. Required if typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Give length. |
| csid | PLS_INTEGER | IN | Optional. Required if typecode represents a type requiring character information, such as CHAR , VARCHAR , or VARCHAR2 . |
| csfrm | PLS_INTEGER | IN | Optional. Required if typecode represents a type requiring character information, such as CHAR , VARCHAR , or VARCHAR2 . |
| attr_type | ANYTYPE | IN | Optional. ANYTYPE corresponding to a user-defined type. This parameter is required if the attribute is a user defined type. |

## Usage Notes

Syntax MEMBER PROCEDURE ADDATTR( self IN OUT NOCOPY ANYTYPE, aname IN VARCHAR2, typecode IN PLS_INTEGER, prec IN PLS_INTEGER, scale IN PLS_INTEGER, len IN PLS_INTEGER, csid IN PLS_INTEGER, csfrm IN PLS_INTEGER, attr_type IN ANYTYPE DEFAULT NULL); Parameters Table 282-5 ADDATTR Procedure Parameters Parameter Description self The transient ANYTYPE that is being constructed. Must be of type DBMS_TYPES.TYPECODE_OBJECT. aname Optional. Attribute's name. Could be NULL . typecode Attribute's typecode. Can be built-in or user-defined typecode (from DBMS_TYPES package). prec Optional. Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. scale Optional. Required if typecode represents a NUMBER . Give precision and scale. Ignored otherwise. len Optional. Required if typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Give length. csid Optional. Required if typecode represents a type requiring character information, such as CHAR , VARCHAR , or VARCHAR2 . csfrm Optional. Required if typecode represents a type requiring character information, such as CHAR , VARCHAR , or VARCHAR2 . attr_type Optional. ANYTYPE corresponding to a user-defined type. This parameter is required if the attribute is a user defined type. Exceptions DBMS_TYPES.INVALID_PARAMETERS : Invalid Parameters (typecode, typeinfo) DBMS_TYPES.INCORRECT_USAGE : Incorrect usage (cannot call after calling EndCreate , and similar actions.)