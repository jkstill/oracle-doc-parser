---
id: 19c__ANYTYPE.GETINFO
name: ANYTYPE.GETINFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYTYPE
tags: [anytype]
source_file: ANYTYPE-TYPE.html
---

# ANYTYPE.GETINFO

This function gets the type information for the ANYTYPE .

## Syntax

```sql
MEMBER FUNCTION GETINFO (
   self        IN ANYTYPE,
   prec        OUT PLS_INTEGER, 
   scale       OUT PLS_INTEGER,
   len         OUT PLS_INTEGER, 
   csid        OUT PLS_INTEGER,
   csfrm       OUT PLS_INTEGER,
   schema_name OUT VARCHAR2, 
   type_name   OUT VARCHAR2, 
   version     OUT varchar2,
   numelems    OUT PLS_INTEGER)
   RETURN      PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYTYPE | IN | The ANYTYPE . |
| prec | PLS_INTEGER | OUT | If typecode represents a number. Gives precision and scale. Ignored otherwise. |
| scale | PLS_INTEGER | OUT | If typecode represents a number. Gives precision and scale. Ignored otherwise. |
| len | PLS_INTEGER | OUT | If typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Gives length. |
| csid | PLS_INTEGER | OUT | If typecode represents a type requiring character information such as: CHAR , VARCHAR , or VARCHAR2 . |
| csid | PLS_INTEGER | OUT | If typecode represents a type requiring character information such as: CHAR , VARCHAR , or VARCHAR2 . |
| schema_name | VARCHAR2 | OUT | Type's schema (if persistent). |
| type_name | VARCHAR2 | OUT | Type's typename. |
| version | varchar2 | OUT | Type's version. |
| numelems | PLS_INTEGER) | OUT | If self is a TYPECODE_VARRAY , this gives the VARRAY count. If self is of TYPECODE_OBJECT , this gives the number of attributes. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax MEMBER FUNCTION GETINFO ( self IN ANYTYPE, prec OUT PLS_INTEGER, scale OUT PLS_INTEGER, len OUT PLS_INTEGER, csid OUT PLS_INTEGER, csfrm OUT PLS_INTEGER, schema_name OUT VARCHAR2, type_name OUT VARCHAR2, version OUT varchar2, numelems OUT PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 282-7 GETINFO Function Parameters Parameter Description self The ANYTYPE . prec If typecode represents a number. Gives precision and scale. Ignored otherwise. scale If typecode represents a number. Gives precision and scale. Ignored otherwise. len If typecode represents a RAW , CHAR , VARCHAR , or VARCHAR2 type. Gives length. csid If typecode represents a type requiring character information such as: CHAR , VARCHAR , or VARCHAR2 . csid If typecode represents a type requiring character information such as: CHAR , VARCHAR , or VARCHAR2 . schema_name Type's schema (if persistent). type_name Type's typename. version Type's version. numelems If self is a TYPECODE_VARRAY , this gives the VARRAY count. If self is of TYPECODE_OBJECT , this gives the number of attributes. Return Values The typecode of self . Exceptions DBMS_TYPES.INVALID_PARAMETERS : Invalid Parameters (position is beyond bounds or the ANYTYPE is not properly Constructed).