---
id: 19c__ANYDATASET.SET_
name: ANYDATASET.SET*
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.SET*

This procedure sets the current data value.

## Syntax

```sql
MEMBER PROCEDURE SETBDOUBLE(
   self              IN OUT NOCOPY ANYDATASET, 
   dbl               IN BINARY_DOUBLE, 
   last_elem         IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETBFLOAT(
   self              IN OUT NOCOPY ANYDATASET, 
   fl                IN BINARY_FLOAT, 
   last_elem         IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETBFILE(
   self              IN OUT NOCOPY ANYDATASET,
   b                 IN BFILE,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETBLOB(
   self              IN OUT NOCOPY ANYDATASET,
   b                 IN BLOB,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETCHAR(
   self              IN OUT NOCOPY ANYDATASET,
   c                 IN CHAR,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETCLOB(
   self              IN OUT NOCOPY ANYDATASET,
   c                 IN CLOB,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETCOLLECTION(
   self              IN OUT NOCOPY ANYDATASET,
   col               IN "<collection_type>",
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETDATE(
   self              IN OUT NOCOPY ANYDATASET,
   dat               IN DATE,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETINTERVALDS(
   self              IN OUT NOCOPY ANYDATASET,
   inv               IN INTERVAL DAY TO SECOND,
   last_elem         IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETINTERVALYM(
   self              IN OUT NOCOPY ANYDATASET,
   inv               IN INTERVAL YEAR TO MONTH,
   last_elem         IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETNCHAR(
   self              IN OUT NOCOPY ANYDATASET,
   nc                IN NCHAR, 
   last_elem IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETNCLOB(
  self              IN OUT NOCOPY ANYDATASET,
  nc                IN NClob, 
  last_elem         IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETNUMBER(
   self              IN OUT NOCOPY ANYDATASET,
   num               IN NUMBER,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETNVARCHAR2(
   self             IN OUT NOCOPY ANYDATASET,
   nc               IN NVarchar2, 
   last_elem        IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETOBJECT(
   self              IN OUT NOCOPY ANYDATASET,
   obj               IN "<object_type>", 
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETRAW(
   self              IN OUT NOCOPY ANYDATASET,
   r                 IN RAW,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETREF(
   self              IN OUT NOCOPY ANYDATASET,
   rf                IN REF "<object_type>",
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETTIMESTAMP(
   self              IN OUT NOCOPY ANYDATASET, 
   ts                IN TIMESTAMP,
   last_elem IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETTIMESTAMPLTZ(
   self             IN OUT NOCOPY ANYDATASET,
   ts               IN TIMESTAMP WITH LOCAL TIME ZONE,
   last_elem        IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETTIMESTAMPTZ(
   self             IN OUT NOCOPY ANYDATASET, 
   ts               IN TIMESTAMP WITH TIME ZONE,
   last_elem        IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETUROWID(
   self              IN OUT NOCOPY ANYDATASET, 
   rid               IN UROWID,
   last_elem IN BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETVARCHAR(
   self              IN OUT NOCOPY ANYDATASET,
   c                 IN VARCHAR,
   last_elem BOOLEAN DEFAULT FALSE);

MEMBER PROCEDURE SETVARCHAR2(
   self              IN OUT NOCOPY ANYDATASET,
   c                 IN VARCHAR2,
   last_elem BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | The ANYDATASET being accessed. |
| num | NUMBER | IN | The number, and associated information, that is to be set. |
| last_elem | BOOLEAN | IN | Relevant only if PIECEWISE has been already called (for a collection). Set to TRUE if it is the last element of the collection, FALSE otherwise. |

## Usage Notes

The type of the current data value depends on the MODE with which we are constructing (depending on how we have invoked the PIECEWISE call). The type of the current data should be the type of the ANYDATASET if PIECEWISE has NOT been called. The type should be the type of the attribute at the current position if PIECEWISE has been called. Syntax MEMBER PROCEDURE SETBDOUBLE( self IN OUT NOCOPY ANYDATASET, dbl IN BINARY_DOUBLE, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETBFLOAT( self IN OUT NOCOPY ANYDATASET, fl IN BINARY_FLOAT, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETBFILE( self IN OUT NOCOPY ANYDATASET, b IN BFILE, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETBLOB( self IN OUT NOCOPY ANYDATASET, b IN BLOB, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETCHAR( self IN OUT NOCOPY ANYDATASET, c IN CHAR, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETCLOB( self IN OUT NOCOPY ANYDATASET, c IN CLOB, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETCOLLECTION( self IN OUT NOCOPY ANYDATASET, col IN "<collection_type>", last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETDATE( self IN OUT NOCOPY ANYDATASET, dat IN DATE, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETINTERVALDS( self IN OUT NOCOPY ANYDATASET, inv IN INTERVAL DAY TO SECOND, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETINTERVALYM( self IN OUT NOCOPY ANYDATASET, inv IN INTERVAL YEAR TO MONTH, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETNCHAR( self IN OUT NOCOPY ANYDATASET, nc IN NCHAR, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETNCLOB( self IN OUT NOCOPY ANYDATASET, nc IN NClob, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETNUMBER( self IN OUT NOCOPY ANYDATASET, num IN NUMBER, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETNVARCHAR2( self IN OUT NOCOPY ANYDATASET, nc IN NVarchar2, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETOBJECT( self IN OUT NOCOPY ANYDATASET, obj IN "<object_type>", last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETRAW( self IN OUT NOCOPY ANYDATASET, r IN RAW, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETREF( self IN OUT NOCOPY ANYDATASET, rf IN REF "<object_type>", last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETTIMESTAMP( self IN OUT NOCOPY ANYDATASET, ts IN TIMESTAMP, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETTIMESTAMPLTZ( self IN OUT NOCOPY ANYDATASET, ts IN TIMESTAMP WITH LOCAL TIME ZONE, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETTIMESTAMPTZ( self IN OUT NOCOPY ANYDATASET, ts IN TIMESTAMP WITH TIME ZONE, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETUROWID( self IN OUT NOCOPY ANYDATASET, rid IN UROWID, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETVARCHAR( self IN OUT NOCOPY ANYDATASET, c IN VARCHAR, last_elem BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETVARCHAR2( self IN OUT NOCOPY ANYDATASET, c IN VARCHAR2, last_elem BOOLEAN DEFAULT FALSE); Parameters Table 281-11 SET* Procedure Parameters Parameter Description self The ANYDATASET being accessed. num The number, and associated information, that is to be set. last_elem Relevant only if PIECEWISE has been already called (for a collection). Set to TRUE if it is the last element of the collection, FALSE otherwise. Exceptions DBMS_TYPES.INVALID_PARAMETERS : Invalid parameters (if it is not appropriate to add a number at this point in the creation process). DBMS_TYPES.INCORRECT_USAGE : Incorrect usage. DBMS_TYPES.TYPE_MISMATCH : When the expected type is different from the passed in type.