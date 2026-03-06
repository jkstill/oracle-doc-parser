---
id: 19c__DBMS_LOB.GETOPTIONS
name: DBMS_LOB.GETOPTIONS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.GETOPTIONS

This function obtains compression, deduplication, and encryption settings corresponding to the option_type field for a particular LOB.

## Syntax

```sql
DBMS_LOB.GETOPTIONS (
   lob_loc             IN     BLOB,
   option_types        IN     PLS_INTEGER) 
 RETURN PLS_INTEGER;
 
DBMS_LOB.GETOPTIONS (
  lob_loc             IN     CLOB CHARACTER SET ANY_CS,
  option_types        IN     PLS_INTEGER) 
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | Locator for the LOB to be examined. For more information, see Operational Notes . |
| option_type |  |  | See Table 99-2 |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_LOB.GETOPTIONS ( lob_loc IN BLOB, option_types IN PLS_INTEGER) RETURN PLS_INTEGER; DBMS_LOB.GETOPTIONS ( lob_loc IN CLOB CHARACTER SET ANY_CS, option_types IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 99-65 GETOPTIONS Function Parameter Parameter Description lob_loc Locator for the LOB to be examined. For more information, see Operational Notes . option_type See Table 99-2 Return Values The return values are a combination of COMPRESS_ON , ENCRYPT_ON and DEDUPLICATE_ON (see Table 99-3 ) depending on which option types (see Table 99-2 ) are passed in. Exceptions Table 99-66 GETOPTIONS Procedure Exceptions Exception Description INVALID_ARGVAL A parameter value was invalid QUERY_WRITE Cannot perform operation during a query BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled SECUREFILE_BADLOB A non- SECUREFILE LOB was used in a SECUREFILE LOB only call Usage Notes You cannot turn compression or deduplication on or off for a SecureFile column that does not have those features on. The GetOptions Functions and SETOPTIONS Procedures work on individual SecureFiles. You can turn off a feature on a particular SecureFile and turn on a feature that has already been turned off by SetOptions, but you cannot turn on an option that has not been given to the SecureFile when the table was created.