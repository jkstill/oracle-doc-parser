---
id: 19c__DBMS_LOB.FRAGMENT_DELETE
name: DBMS_LOB.FRAGMENT_DELETE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FRAGMENT_DELETE

This procedure deletes the data at the specified offset for the specified length from the LOB without having to rewrite all the data in the LOB following the specified offset.

## Syntax

```sql
DBMS_LOB.FRAGMENT_DELETE (
   lob_loc     IN OUT NOCOPY BLOB,
   amount      IN            INTEGER,
   offset      IN            INTEGER);

DBMS_LOB.FRAGMENT_DELETE (
   lob_loc     IN OUT NOCOPY CLOB CHARACTER SET ANY_CS,
   amount      IN            INTEGER,
   offset      IN            INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB locator. For more information, see Operational Notes . |
| amount | INTEGER | IN | Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to be removed from the LOB |
| offset | INTEGER) | IN | Offset into the LOB in bytes ( BLOB ) or characters ( CLOB / NCLOB ) to begin the deletion |

## Usage Notes

Syntax DBMS_LOB.FRAGMENT_DELETE ( lob_loc IN OUT NOCOPY BLOB, amount IN INTEGER, offset IN INTEGER); DBMS_LOB.FRAGMENT_DELETE ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, amount IN INTEGER, offset IN INTEGER); Parameters Table 99-45 FRAGMENT_DELETE Procedure Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . amount Number of bytes ( BLOB ) or characters ( CLOB / NCLOB ) to be removed from the LOB offset Offset into the LOB in bytes ( BLOB ) or characters ( CLOB / NCLOB ) to begin the deletion Exceptions Table 99-46 FRAGMENT_DELETE Procedure Exceptions Exception Description INVALID_ARGVAL A parameter value was invalid QUERY_WRITE Cannot perform operation during a query BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled SECUREFILE_BADLOB A non- SECUREFILE LOB was used in a SECUREFILE LOB only call SECUREFILE_OUTOFBOUNDS Attempted to perform a FRAGMENT_* operation past LOB end