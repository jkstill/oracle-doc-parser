---
id: 19c__DBMS_LOB.CREATETEMPORARY
name: DBMS_LOB.CREATETEMPORARY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.CREATETEMPORARY

This procedure creates a temporary BLOB or CLOB and its corresponding index in your default temporary tablespace.

## Syntax

```sql
DBMS_LOB.CREATETEMPORARY (
   lob_loc IN OUT NOCOPY BLOB,
   cache   IN            BOOLEAN,
   dur     IN            PLS_INTEGER := DBMS_LOB.SESSION);
  
DBMS_LOB.CREATETEMPORARY (
   lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS,
   cache   IN            BOOLEAN,
   dur     IN            PLS_INTEGER := 10);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator. For more information, see Operational Notes . |
| cache | BOOLEAN | IN | Specifies if LOB should be read into buffer cache or not. |
| dur | PLS_INTEGER | IN | 1 of 2 predefined duration values ( SESSION or CALL ) which specifies a hint as to whether the temporary LOB is cleaned up at the end of the session or call. If dur is omitted, then the session duration is used. |

## Usage Notes

Syntax DBMS_LOB.CREATETEMPORARY ( lob_loc IN OUT NOCOPY BLOB, cache IN BOOLEAN, dur IN PLS_INTEGER := DBMS_LOB.SESSION); DBMS_LOB.CREATETEMPORARY ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, cache IN BOOLEAN, dur IN PLS_INTEGER := 10); Parameters Table 99-28 CREATETEMPORARY Procedure Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . cache Specifies if LOB should be read into buffer cache or not. dur 1 of 2 predefined duration values ( SESSION or CALL ) which specifies a hint as to whether the temporary LOB is cleaned up at the end of the session or call. If dur is omitted, then the session duration is used. See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure Oracle Database PL/SQL Language Reference for more information about NOCOPY and passing temporary lobs as parameters See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure Oracle Database PL/SQL Language Reference for more information about NOCOPY and passing temporary lobs as parameters