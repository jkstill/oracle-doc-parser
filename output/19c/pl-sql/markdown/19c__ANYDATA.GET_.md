---
id: 19c__ANYDATA.GET_
name: ANYDATA.GET*
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATA
tags: [anydata]
source_file: ANYDATA-TYPE.html
---

# ANYDATA.GET*

These functions get the current data value (which should be of appropriate type).

## Syntax

```sql
MEMBER FUNCTION GetBDouble(
   self         IN ANYDATA,
   dbl          OUT NOCOPY BINARY_DOUBLE)
RETURN PLS_INTEGER;

MEMBER FUNCTION GetBfile(
   self         IN ANYDATA,
   b            OUT NOCOPY BFILE)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetBFloat(
   self         IN ANYDATA,
   fl           OUT NOCOPY BINARY_FLOAT)
RETURN PLS_INTEGER;

MEMBER FUNCTION GetBlob(
   self         IN ANYDATA,
   b            OUT NOCOPY BLOB)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetChar(
   self         IN ANYDATA,
   c            OUT NOCOPY CHAR)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetClob(
   self         IN ANYDATA,
   c            OUT NOCOPY CLOB)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetCollection(
   self         IN ANYDATA,
   col          OUT NOCOPY "<collection_type>")
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetDate(
   self         IN ANYDATA,
   dat          OUT NOCOPY DATE)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetIntervalDS(
   self         IN ANYDATA,
   inv          OUT NOCOPY INTERVAL DAY TO SECOND) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetIntervalYM(
   self         IN ANYDATA,
   inv          OUT NOCOPY INTERVAL YEAR TO MONTH) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetNchar(
   self         IN ANYDATA, 
   nc           OUT NOCOPY NCHAR) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetNClob(
   self         IN ANYDATA, 
   nc           OUT NOCOPY NCLOB) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetNumber(
   self         IN ANYDATA,
   num          OUT NOCOPY NUMBER)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetNVarchar2(
   self         IN ANYDATA, 
   nc           OUT NOCOPY NVARCHAR2) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetObject(
   self         IN ANYDATA,
   obj          OUT NOCOPY "<object_type>")
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetRaw(
   self         IN ANYDATA,
   r            OUT NOCOPY RAW)
   RETURN       PLS_INTEGER;

MMEMBER FUNCTION GetRef(
   self         IN ANYDATA,
   rf           OUT NOCOPY REF "<object_type>")
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetTimestamp(
   self         IN ANYDATA, 
   ts           OUT NOCOPY TIMESTAMP)
 RETURN PLS_INTEGER;

MEMBER FUNCTION GetTimestampTZ(
   self         IN ANYDATA, 
   ts           OUT NOCOPY TIMESTAMP WITH TIME ZONE) 
 RETURN PLS_INTEGER;

MEMBER FUNCTION GetTimestampLTZ(
   self         IN ANYDATA,
   ts           OUT NOCOPY TIMESTAMP WITH LOCAL TIME ZONE) 
 RETURN PLS_INTEGER;

MEMBER FUNCTION GetVarchar(
   self         IN ANYDATA,
   c            OUT NOCOPY VARCHAR)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetVarchar2(
   self         IN ANYDATA,
   c            OUT NOCOPY VARCHAR2)
   RETURN       PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | ANYDATA | IN | An ANYDATA. |
| num | NOCOPY | OUT | The number to be obtained. |

**Returns:** `PLS_INTEGER`

## Usage Notes

The type of the current data value depends on the MODE by which it is accessed (depending on whether the PIECEWISE call is invoked). If PIECEWISE has NOT been called, the ANYDATA is accessed in its entirety and the type of the data value should match the type of the ANYDATA . If PIECEWISE has been called, the ANYDATA is accessed piece-wise. The type of the data value should match the type of the attribute (or collection element) at the current position. Syntax MEMBER FUNCTION GetBDouble( self IN ANYDATA, dbl OUT NOCOPY BINARY_DOUBLE) RETURN PLS_INTEGER; MEMBER FUNCTION GetBfile( self IN ANYDATA, b OUT NOCOPY BFILE) RETURN PLS_INTEGER; MEMBER FUNCTION GetBFloat( self IN ANYDATA, fl OUT NOCOPY BINARY_FLOAT) RETURN PLS_INTEGER; MEMBER FUNCTION GetBlob( self IN ANYDATA, b OUT NOCOPY BLOB) RETURN PLS_INTEGER; MEMBER FUNCTION GetChar( self IN ANYDATA, c OUT NOCOPY CHAR) RETURN PLS_INTEGER; MEMBER FUNCTION GetClob( self IN ANYDATA, c OUT NOCOPY CLOB) RETURN PLS_INTEGER; MEMBER FUNCTION GetCollection( self IN ANYDATA, col OUT NOCOPY "<collection_type>") RETURN PLS_INTEGER; MEMBER FUNCTION GetDate( self IN ANYDATA, dat OUT NOCOPY DATE) RETURN PLS_INTEGER; MEMBER FUNCTION GetIntervalDS( self IN ANYDATA, inv OUT NOCOPY INTERVAL DAY TO SECOND) RETURN PLS_INTEGER; MEMBER FUNCTION GetIntervalYM( self IN ANYDATA, inv OUT NOCOPY INTERVAL YEAR TO MONTH) RETURN PLS_INTEGER; MEMBER FUNCTION GetNchar( self IN ANYDATA, nc OUT NOCOPY NCHAR) RETURN PLS_INTEGER; MEMBER FUNCTION GetNClob( self IN ANYDATA, nc OUT NOCOPY NCLOB) RETURN PLS_INTEGER; MEMBER FUNCTION GetNumber( self IN ANYDATA, num OUT NOCOPY NUMBER) RETURN PLS_INTEGER; MEMBER FUNCTION GetNVarchar2( self IN ANYDATA, nc OUT NOCOPY NVARCHAR2) RETURN PLS_INTEGER; MEMBER FUNCTION GetObject( self IN ANYDATA, obj OUT NOCOPY "<object_type>") RETURN PLS_INTEGER; MEMBER FUNCTION GetRaw( self IN ANYDATA, r OUT NOCOPY RAW) RETURN PLS_INTEGER; MMEMBER FUNCTION GetRef( self IN ANYDATA, rf OUT NOCOPY REF "<object_type>") RETURN PLS_INTEGER; MEMBER FUNCTION GetTimestamp( self IN ANYDATA, ts OUT NOCOPY TIMESTAMP) RETURN PLS_INTEGER; MEMBER FUNCTION GetTimestampTZ( self IN ANYDATA, ts OUT NOCOPY TIMESTAMP WITH TIME ZONE) RETURN PLS_INTEGER; MEMBER FUNCTION GetTimestampLTZ( self IN ANYDATA, ts OUT NOCOPY TIMESTAMP WITH LOCAL TIME ZONE) RETURN PLS_INTEGER; MEMBER FUNCTION GetVarchar( self IN ANYDATA, c OUT NOCOPY VARCHAR) RETURN PLS_INTEGER; MEMBER FUNCTION GetVarchar2( self IN ANYDATA, c OUT NOCOPY VARCHAR2) RETURN PLS_INTEGER; Parameters Table 280-4 GET* Function Parameter Parameter Description self An ANYDATA. num The number to be obtained. Return Values DBMS_TYPES . SUCCESS or DBMS_TYPES . NO_DATA The return value is relevant only if PIECEWISE has been already called (for a collection). In such a case, DBMS_TYPES.NO_DATA signifies the end of the collection when all elements have been accessed. Exceptions DBMS_TYPES.TYPE_MISMATCH : When the expected type is different from the passed in type. DBMS_TYPES.INVALID_PARAMETERS : Invalid Parameters (if it is not appropriate to add a number at this point in the creation process). DBMS_TYPES.INCORRECT_USAGE : Incorrect usage.