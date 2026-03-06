---
id: 19c__ANYDATA.SET_
name: ANYDATA.SET*
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATA
tags: [anydata]
source_file: ANYDATA-TYPE.html
---

# ANYDATA.SET*

This procedure sets the current data value.

## Syntax

```sql
MEMBER PROCEDURE SETBDOUBLE(
   self        IN OUT NOCOPY ANYDATA,
   dbl         IN BINARY_DOUBLE,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETBFILE(
   self        IN OUT NOCOPY ANYDATA,
   b           IN BFILE,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETBFLOAT(
   self        IN OUT NOCOPY ANYDATA, 
   fl          IN            BINARY_FLOAT,
   last_elem   IN            boolean DEFAULT FALSE);

MEMBER PROCEDURE SETBLOB(
   self        IN OUT NOCOPY ANYDATA, 
   b           IN BLOB,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETCHAR(
   self        IN OUT NOCOPY ANYDATA, 
   c           IN CHAR,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETCLOB(
   self        IN OUT NOCOPY ANYDATA,
   c           IN CLOB,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETCOLLECTION(
   self        IN OUT NOCOPY ANYDATA,
   col         IN "<collectyion_type>",
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETDATE(
   self        IN OUT NOCOPY ANYDATA, 
   dat         IN DATE,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETINTERVALDS(
   self        IN OUT NOCOPY ANYDATA,
   inv         IN INTERVAL DAY TO SECOND,
   last_elem IN boolean DEFAULT FALSE);
  
MEMBER PROCEDURE SETINTERVALYM(
   self        IN OUT NOCOPY ANYDATA,
   inv         IN INTERVAL YEAR TO MONTH,
   last_elem   IN boolean DEFAULT FALSE);
  
MEMBER PROCEDURE SETNCHAR(
   self        IN OUT NOCOPY ANYDATA,
   nc          IN NCHAR, 
   last_elem   IN boolean DEFAULT FALSE);
  
MEMBER PROCEDURE SETNCLOB(
   self        IN OUT NOCOPY ANYDATA,
   nc          IN NClob, 
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETNUMBER(
   self        IN OUT NOCOPY ANYDATA, 
   num         IN NUMBER,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETNVARCHAR2(
   self        IN OUT NOCOPY ANYDATA,
   nc          IN NVarchar2, 
   last_elem   IN boolean DEFAULT FALSE),
  
MEMBER PROCEDURE SETOBJECT(
   self        IN OUT NOCOPY ANYDATA,
   obj         IN "<object_type>",
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETRAW(
   self        IN OUT NOCOPY ANYDATA, 
   r           IN RAW,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETREF(
   self        IN OUT NOCOPY ANYDATA,
   rf          IN REF "<object_type>",
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETTIMESTAMP(
   self       IN OUT NOCOPY ANYDATA, 
   ts         IN TIMESTAMP,
   last_elem  IN BOOLEAN DEFAULT FALSE);
  
MEMBER PROCEDURE SETTIMESTAMPTZ(self IN OUT NOCOPY ANYDATA, 
   ts          IN TIMESTAMP WITH TIME ZONE,
   last_elem   IN BOOLEAN DEFAULT FALSE);
  
MEMBER PROCEDURE SETTIMESTAMPLTZ(
   self IN OUT NOCOPY ANYDATA,
   ts IN TIMESTAMP WITH LOCAL TIME ZONE,
   last_elem IN boolean DEFAULT FALSE),
  
MEMBER PROCEDURE SETVARCHAR(
   self        IN OUT NOCOPY ANYDATA, 
   c           IN VARCHAR,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETVARCHAR2(
   self        IN OUT NOCOPY ANYDATA,
   c           IN VARCHAR2, 
   last_elem   IN boolean DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | An ANYDATA . |
| num | NUMBER | IN | The number, and associated information, that is to be set. |
| last_elem | boolean | IN | Relevant only if ANYDATA represents a collection. Set to TRUE if it is the last element of the collection, FALSE otherwise. |

## Usage Notes

This is a list of procedures that should be called depending on the type of the current data value. The type of the data value should be the type of the attribute at the current position during the piece-wise construction process. Syntax MEMBER PROCEDURE SETBDOUBLE( self IN OUT NOCOPY ANYDATA, dbl IN BINARY_DOUBLE, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETBFILE( self IN OUT NOCOPY ANYDATA, b IN BFILE, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETBFLOAT( self IN OUT NOCOPY ANYDATA, fl IN BINARY_FLOAT, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETBLOB( self IN OUT NOCOPY ANYDATA, b IN BLOB, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETCHAR( self IN OUT NOCOPY ANYDATA, c IN CHAR, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETCLOB( self IN OUT NOCOPY ANYDATA, c IN CLOB, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETCOLLECTION( self IN OUT NOCOPY ANYDATA, col IN "<collectyion_type>", last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETDATE( self IN OUT NOCOPY ANYDATA, dat IN DATE, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETINTERVALDS( self IN OUT NOCOPY ANYDATA, inv IN INTERVAL DAY TO SECOND, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETINTERVALYM( self IN OUT NOCOPY ANYDATA, inv IN INTERVAL YEAR TO MONTH, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETNCHAR( self IN OUT NOCOPY ANYDATA, nc IN NCHAR, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETNCLOB( self IN OUT NOCOPY ANYDATA, nc IN NClob, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETNUMBER( self IN OUT NOCOPY ANYDATA, num IN NUMBER, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETNVARCHAR2( self IN OUT NOCOPY ANYDATA, nc IN NVarchar2, last_elem IN boolean DEFAULT FALSE), MEMBER PROCEDURE SETOBJECT( self IN OUT NOCOPY ANYDATA, obj IN "<object_type>", last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETRAW( self IN OUT NOCOPY ANYDATA, r IN RAW, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETREF( self IN OUT NOCOPY ANYDATA, rf IN REF "<object_type>", last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETTIMESTAMP( self IN OUT NOCOPY ANYDATA, ts IN TIMESTAMP, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETTIMESTAMPTZ(self IN OUT NOCOPY ANYDATA, ts IN TIMESTAMP WITH TIME ZONE, last_elem IN BOOLEAN DEFAULT FALSE); MEMBER PROCEDURE SETTIMESTAMPLTZ( self IN OUT NOCOPY ANYDATA, ts IN TIMESTAMP WITH LOCAL TIME ZONE, last_elem IN boolean DEFAULT FALSE), MEMBER PROCEDURE SETVARCHAR( self IN OUT NOCOPY ANYDATA, c IN VARCHAR, last_elem IN boolean DEFAULT FALSE); MEMBER PROCEDURE SETVARCHAR2( self IN OUT NOCOPY ANYDATA, c IN VARCHAR2, last_elem IN boolean DEFAULT FALSE); Parameters Table 280-8 SET* Procedure Parameters Parameter Description self An ANYDATA . num The number, and associated information, that is to be set. last_elem Relevant only if ANYDATA represents a collection. Set to TRUE if it is the last element of the collection, FALSE otherwise. Exceptions DBMS_TYPES.INVALID_PARAMETERS : Invalid Parameters (if it is not appropriate to add a number at this point in the creation process). DBMS_TYPES.INCORRECT_USAGE : Incorrect usage. DBMS_TYPES.TYPE_MISMATCH : When the expected type is different from the passed in type. Usage Notes When BEGINCREATE is called, construction has already begun in a piece-wise fashion. Subsequent calls to SET* will set the successive attribute values. If the ANYDATA is a standalone collection, the SET* call will set the successive collection elements.