---
id: 19c__DBMS_UTILITY.GET_SQL_HASH
name: DBMS_UTILITY.GET_SQL_HASH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_SQL_HASH

This function computes a hash value for the given string using MD5 algorithm.

## Syntax

```sql
Dbms_utility.get_sql_hash (
   name          IN   VARCHAR2,    
   hash          OUT  RAW,    
   pre10ihash    OUT  NUMBER) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | String to be hashed |
| hash | RAW | OUT | Stores all 16 bytes of returned hash value |
| pre10ihash | NUMBER) | OUT | Stores the pre 10i database version hash value |

**Returns:** `NUMBER`

## Usage Notes

Syntax Dbms_utility.get_sql_hash ( name IN VARCHAR2, hash OUT RAW, pre10ihash OUT NUMBER) RETURN NUMBER; Pragmas Pragma Restrict_references( Get_sql_hash , Wnds , Rnds , Wnps , Rnps ); Parameters Table 187-23 GET_SQL_HASH Procedure Parameters Parameter Description name String to be hashed hash Stores all 16 bytes of returned hash value pre10ihash Stores the pre 10i database version hash value Return Values A hash value (last 4 bytes) based on the input string. the MD5 hash algorithm computes a 16 byte hash value, but we only return the last 4 bytes so that we can return an actual number. Use the hash parameter to get all 16 bytes and pre10 i hash parameter to store the pre 10 i hash value of 4 bytes.