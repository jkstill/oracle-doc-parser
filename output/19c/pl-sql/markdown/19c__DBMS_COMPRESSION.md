---
id: 19c__DBMS_COMPRESSION
name: DBMS_COMPRESSION
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPRESSION
tags: [dbms_compression]
source_file: DBMS_COMPRESSION.html
---

# DBMS_COMPRESSION

The DBMS_COMPRESSION package defines a RECORD type and a TABLE type.

## Syntax

```sql
TYPE COMPREC IS RECORD(
  ownname           varchar2(255),
  objname           varchar2(255),
  blkcnt_cmp        PLS_INTEGER,
  blkcnt_uncmp      PLS_INTEGER,
  row_cmp           PLS_INTEGER,
  row_uncmp         PLS_INTEGER,
  cmp_ratio         NUMBER,
  objtype           PLS_INTEGER);
```

## Usage Notes

RECORD TYPES COMPREC Record Type TABLE TYPES COMPRECLIST Table Type Syntax TYPE COMPREC IS RECORD( ownname varchar2(255), objname varchar2(255), blkcnt_cmp PLS_INTEGER, blkcnt_uncmp PLS_INTEGER, row_cmp PLS_INTEGER, row_uncmp PLS_INTEGER, cmp_ratio NUMBER, objtype PLS_INTEGER); Fields Table 38-2 COMPREC Attributes Field Description ownname Schema of the object owner objname Name of the object blkcnt_cmp Number of blocks used by the compressed sample of the object blkcnt_uncmp Number of blocks used by the uncompressed sample of the object row_cmp Number of rows in a block in compressed sample of the object row_uncmp Number of rows in a block in uncompressed sample of the object cmp_ratio Compression ratio, blkcnt_uncmp divided by blkcnt_cmp objtype Type of the object Syntax TYPE compreclist IS TABLE OF comprec;