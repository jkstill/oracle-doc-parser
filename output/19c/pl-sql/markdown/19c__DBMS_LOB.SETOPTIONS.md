---
id: 19c__DBMS_LOB.SETOPTIONS
name: DBMS_LOB.SETOPTIONS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.SETOPTIONS

This procedure enables/disables compression and deduplication on a per-LOB basis, overriding the default LOB column settings.

## Syntax

```sql
DBMS_LOB.SETOPTIONS (
   lob_loc             IN     BLOB,
   option_types        IN     PLS_INTEGER,
   options             IN     PLS_INTEGER);
 
DBMS_LOB.SETOPTIONS (
  lob_loc             IN     CLOB CHARACTER SET ANY_CS,
  option_types        IN     PLS_INTEGER, 
  options             IN     PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | Locator for the LOB to be examined. For more information, see Operational Notes . |
| option_type |  |  | See Table 99-2 |
| options | PLS_INTEGER) | IN | See Table 99-3 |

## Usage Notes

Syntax DBMS_LOB.SETOPTIONS ( lob_loc IN BLOB, option_types IN PLS_INTEGER, options IN PLS_INTEGER); DBMS_LOB.SETOPTIONS ( lob_loc IN CLOB CHARACTER SET ANY_CS, option_types IN PLS_INTEGER, options IN PLS_INTEGER); Parameters Table 99-93 SETOPTIONS Procedure Parameter Parameter Description lob_loc Locator for the LOB to be examined. For more information, see Operational Notes . option_type See Table 99-2 options See Table 99-3 Exceptions Table 99-94 SETOPTIONS Procedure Exceptions Exception Description SECUREFILE_BADLOB Unsupported object type for the operation INVALID_ARGVAL A parameter value was invalid QUERY_WRITE Cannot perform operation during a query BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled Usage Notes DBMS_LOB.SETOPTIONS cannot be used to enable or disable encryption on individual LOBs. You cannot turn the compression or deduplication features on or off for a SecureFile column if they were not turned when the table was created. The GETOPTIONS Functions and SETOPTIONS Procedures work on individual SecureFiles. You can turn off compression or deduplication on a particular SecureFiles LOB and turn on them on, if they have already been turned off by SETOPTIONS . This call incurs a round-trip to the server to make the changes persistent.