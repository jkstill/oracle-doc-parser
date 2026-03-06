---
id: 19c__DBMS_LOB.FRAGMENT_MOVE
name: DBMS_LOB.FRAGMENT_MOVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FRAGMENT_MOVE

This procedure moves the amount of bytes (BLOB) or characters (CLOB/NCLOB) from the specified offset to the new offset specified.

## Syntax

```sql
DBMS_LOB.FRAGMENT_MOVE (
   lob_loc       IN OUT NOCOPY BLOB,
   amount        IN            INTEGER,
   src_offset    IN            INTEGER,
   dest_offset   IN            INTEGER);

DBMS_LOB.FRAGMENT_MOVE (
   lob_loc       IN OUT NOCOPY CLOB CHARACTER SET ANY_CS,
   amount        IN            INTEGER,
   src_offset    IN            INTEGER,
   dest_offset   IN            INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator. For more information, see Operational Notes . |
| amount | INTEGER | IN | Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to be moved in the LOB |
| src_offset | INTEGER | IN | Beginning offset into the LOB in bytes ( BLOB ) or characters ( CLOB / NCLOB ) to put the data |
| dest_offset | INTEGER) | IN | Beginning offset into the LOB in bytes ( BLOB ) or characters ( CLOB / NCLOB ) to remove the data |

## Usage Notes

Syntax DBMS_LOB.FRAGMENT_MOVE ( lob_loc IN OUT NOCOPY BLOB, amount IN INTEGER, src_offset IN INTEGER, dest_offset IN INTEGER); DBMS_LOB.FRAGMENT_MOVE ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, amount IN INTEGER, src_offset IN INTEGER, dest_offset IN INTEGER); Parameters Table 99-49 FRAGMENT_MOVE Procedure Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . amount Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to be moved in the LOB src_offset Beginning offset into the LOB in bytes ( BLOB ) or characters ( CLOB / NCLOB ) to put the data dest_offset Beginning offset into the LOB in bytes ( BLOB ) or characters ( CLOB / NCLOB ) to remove the data Exceptions Table 99-50 FRAGMENT_MOVE Procedure Exceptions Exception Description INVALID_ARGVAL A parameter value was invalid QUERY_WRITE Cannot perform operation during a query BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled SECUREFILE_BADLOB A non- SECUREFILE LOB was used in a SECUREFILE LOB only call SECUREFILE_OUTOFBOUNDS Attempted to perform a FRAGMENT_* operation past LOB end Usage Notes All offsets are pre-move offsets. Offsets of more than 1 past the end of the LOB are not permitted. FRAGMENT_MOVE gets the LOB, if necessary, before performing operations on the LOB.