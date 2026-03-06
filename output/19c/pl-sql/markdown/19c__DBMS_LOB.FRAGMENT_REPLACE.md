---
id: 19c__DBMS_LOB.FRAGMENT_REPLACE
name: DBMS_LOB.FRAGMENT_REPLACE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FRAGMENT_REPLACE

This procedure replaces the data at the specified offset with the specified data (not to exceed 32k).

## Syntax

```sql
DBMS_LOB.FRAGMENT_REPLACE (
   lob_loc     IN OUT NOCOPY BLOB,
   old_amount  IN            INTEGER,
   new_amount  IN            INTEGER,
   offset      IN            INTEGER,
   buffer      IN            RAW);

DBMS_LOB.FRAGMENT_REPLACE (
   lob_loc     IN OUT NOCOPY CLOB CHARACTER SET ANY_CS,   old_amount  IN           INTEGER,
   new_amount  IN           INTEGER,
   offset      IN           INTEGER,
   buffer      IN           VARCHAR2 CHARACTER SET lob_loc%CHARSET);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator. For more information, see Operational Notes . |
| old_amount | INTEGER | IN | Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to be replaced in the LOB |
| new_amount | INTEGER | IN | Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to written to the LOB |
| offset | INTEGER | IN | Beginning offset into the LOB in bytes (BLOB) or characters ( CLOB / NCLOB ) to put the data |
| buffer | RAW) | IN | Data to insert into the LOB |

## Usage Notes

Syntax DBMS_LOB.FRAGMENT_REPLACE ( lob_loc IN OUT NOCOPY BLOB, old_amount IN INTEGER, new_amount IN INTEGER, offset IN INTEGER, buffer IN RAW); DBMS_LOB.FRAGMENT_REPLACE ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, old_amount IN INTEGER, new_amount IN INTEGER, offset IN INTEGER, buffer IN VARCHAR2 CHARACTER SET lob_loc%CHARSET); Parameters Table 99-51 FRAGMENT_REPLACE Function Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . old_amount Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to be replaced in the LOB new_amount Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to written to the LOB offset Beginning offset into the LOB in bytes (BLOB) or characters ( CLOB / NCLOB ) to put the data buffer Data to insert into the LOB Exceptions Table 99-52 FRAGMENT_REPLACE Procedure Exceptions Exception Description INVALID_ARGVAL A parameter value was invalid QUERY_WRITE Cannot perform operation during a query BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled SECUREFILE_BADLOB A non- SECUREFILE LOB was used in a SECUREFILE LOB only call SECUREFILE_OUTOFBOUNDS Attempted to perform a FRAGMENT_* operation past LOB end Usage Notes Invoking this procedure is equivalent to deleting the old amount of bytes/characters at offset and then inserting the new amount of bytes/characters at offset. FRAGMENT_REPLACE gets the LOB, if necessary, before performing operations on the LOB.