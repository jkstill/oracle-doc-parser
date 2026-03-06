---
id: 19c__DBMS_LOB.FRAGMENT_INSERT
name: DBMS_LOB.FRAGMENT_INSERT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FRAGMENT_INSERT

This procedure inserts the specified data (limited to 32K) into the LOB at the specified offset.

## Syntax

```sql
DBMS_LOB.FRAGMENT_INSERT (
   lob_loc     IN OUT NOCOPY BLOB,
   amount      IN            INTEGER,
   offset      IN            INTEGER,
   buffer      IN            RAW);

DBMS_LOB.FRAGMENT_INSERT (
   lob_loc     IN OUT NOCOPY CLOB CHARACTER SET ANY_CS,
   amount      IN            INTEGER,
   offset      IN            INTEGER,
   buffer      IN            VARCHAR2 CHARACTER SET lob_loc%CHARSET);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator.For more information, see Operational Notes . |
| amount | INTEGER | IN | Number of bytes (BLOB) or characters (CLOB/NCLOB) to be inserted into the LOB |
| offset | INTEGER | IN | Offset into the LOB in bytes (BLOB) or characters (CLOB/NCLOB) to begin the insertion |
| buffer | RAW) | IN | Data to insert into the LOB |

## Usage Notes

Syntax DBMS_LOB.FRAGMENT_INSERT ( lob_loc IN OUT NOCOPY BLOB, amount IN INTEGER, offset IN INTEGER, buffer IN RAW); DBMS_LOB.FRAGMENT_INSERT ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, amount IN INTEGER, offset IN INTEGER, buffer IN VARCHAR2 CHARACTER SET lob_loc%CHARSET); Parameters Table 99-47 FRAGMENT_INSERT Procedure Parameters Parameter Description lob_loc LOB locator.For more information, see Operational Notes . amount Number of bytes (BLOB) or characters (CLOB/NCLOB) to be inserted into the LOB offset Offset into the LOB in bytes (BLOB) or characters (CLOB/NCLOB) to begin the insertion buffer Data to insert into the LOB Exceptions Table 99-48 FRAGMENT_INSERT Procedure Exceptions Exception Description INVALID_ARGVAL A parameter value was invalid QUERY_WRITE Cannot perform operation during a query BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled SECUREFILE_BADLOB A non- SECUREFILE LOB was used in a SECUREFILE LOB only call SECUREFILE_OUTOFBOUNDS Attempted to perform a FRAGMENT_* operation past LOB end Usage Notes FRAGMENT_INSERT gets the LOB, if necessary, before performing operations on the LOB.