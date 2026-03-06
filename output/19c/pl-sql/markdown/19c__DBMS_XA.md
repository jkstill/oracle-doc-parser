---
id: 19c__DBMS_XA
name: DBMS_XA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XA
tags: [dbms_xa]
source_file: DBMS_XA.html
---

# DBMS_XA

The DBMS_XA package uses this OBJECT type and associated TABLE type.

## Syntax

```sql
TYPE DBMS_XA_XID IS OBJECT(
  formatid      NUMBER,
  gtrid         RAW(64),
  bqual         RAW(64),
  constructor function DBMS_XA_XID(
       gtrid     IN   NUMBER)
    RETURN SELF AS RESULT,
  constructor function DBMS_XA_XID (
       gtrid     IN   RAW, 
       bqual     IN   RAW)
    RETURN SELF AS RESULT,
  constructor function DBMS_XA_XID(
       formatid  IN   NUMBER,
       gtrid     IN   RAW,
       bqual     IN   RAW DEFAULT HEXTORAW('00000000000000000000000000000001'))
    RETURN SELF AS RESULT)
```

**Returns:** `SELF`

## Usage Notes

OBJECT Types DBMS_XA_XID Object Type TABLE Types DBMS_XA_XID_ARRAY Table Type Note: For more information, see "Distributed Transaction Processing: The XA Specification" in the public XA Standard. Note: For more information, see "Distributed Transaction Processing: The XA Specification" in the public XA Standard. Syntax TYPE DBMS_XA_XID IS OBJECT( formatid NUMBER, gtrid RAW(64), bqual RAW(64), constructor function DBMS_XA_XID( gtrid IN NUMBER) RETURN SELF AS RESULT, constructor function DBMS_XA_XID ( gtrid IN RAW, bqual IN RAW) RETURN SELF AS RESULT , constructor function DBMS_XA_XID( formatid IN NUMBER, gtrid IN RAW, bqual IN RAW DEFAULT HEXTORAW('00000000000000000000000000000001')) RETURN SELF AS RESULT )