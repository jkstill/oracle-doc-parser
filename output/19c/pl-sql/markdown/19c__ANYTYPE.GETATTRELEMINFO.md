---
id: 19c__ANYTYPE.GETATTRELEMINFO
name: ANYTYPE.GETATTRELEMINFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYTYPE
tags: [anytype]
source_file: ANYTYPE-TYPE.html
---

# ANYTYPE.GETATTRELEMINFO

This function gets the type information for an attribute of the type (if it is of TYPECODE_OBJECT ). Gets the type information for a collection's element type if the self parameter is of a collection type.

## Syntax

```sql
MEMBER FUNCTION GETATTRELEMINFO (
   self           IN ANYTYPE, 
   pos            IN PLS_INTEGER,
   prec           OUT PLS_INTEGER, 
   scale          OUT PLS_INTEGER,
   len            OUT PLS_INTEGER, 
   csid           OUT PLS_INTEGER, 
   csfrm          OUT PLS_INTEGER,
   attr_elt_type  OUT ANYTYPE
   aname          OUT VARRCHAR2)
   RETURN         PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYTYPE | IN | The ANYTYPE . |
| pos | PLS_INTEGER | IN | If self is of TYPECODE_OBJECT , this gives the attribute position (starting at 1). It is ignored otherwise. |
| prec | PLS_INTEGER | OUT | If attribute/collection element typecode represents a NUMBER . Gives precision and scale. Ignored otherwise. |
| scale | PLS_INTEGER | OUT | If attribute/collection element typecode represents a NUMBER . Gives precision and scale. Ignored otherwise. |
| len | PLS_INTEGER | OUT | If typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Gives length. |
| csid, csfrm |  |  | If typecode represents a type requiring character information such as: CHAR , VARCHAR , or VARCHAR2 . Gives character set ID , character set form. |
| attr_elt_type | ANYTYPE | OUT | If attribute/collection element typecode represents a user-defined type, this returns the ANYTYPE corresponding to it. User can subsequently describe the attr_elt_type . |
| aname | VARRCHAR2) | OUT | Attribute name (if it is an attribute of an object type, NULL otherwise). |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax MEMBER FUNCTION GETATTRELEMINFO ( self IN ANYTYPE, pos IN PLS_INTEGER, prec OUT PLS_INTEGER, scale OUT PLS_INTEGER, len OUT PLS_INTEGER, csid OUT PLS_INTEGER, csfrm OUT PLS_INTEGER, attr_elt_type OUT ANYTYPE aname OUT VARRCHAR2) RETURN PLS_INTEGER; Parameters Table 282-8 GETATTRELEMINFO Function Parameters Parameter Description self The ANYTYPE . pos If self is of TYPECODE_OBJECT , this gives the attribute position (starting at 1). It is ignored otherwise. prec If attribute/collection element typecode represents a NUMBER . Gives precision and scale. Ignored otherwise. scale If attribute/collection element typecode represents a NUMBER . Gives precision and scale. Ignored otherwise. len If typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Gives length. csid, csfrm If typecode represents a type requiring character information such as: CHAR , VARCHAR , or VARCHAR2 . Gives character set ID , character set form. attr_elt_type If attribute/collection element typecode represents a user-defined type, this returns the ANYTYPE corresponding to it. User can subsequently describe the attr_elt_type . aname Attribute name (if it is an attribute of an object type, NULL otherwise). Return Values The typecode of the attribute or collection element. Exceptions DBMS_TYPES.INVALID_PARAMETERS: Invalid Parameters (position is beyond bounds or the ANYTYPE is not properly constructed).