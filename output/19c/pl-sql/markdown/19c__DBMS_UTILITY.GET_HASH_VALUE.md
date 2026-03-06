---
id: 19c__DBMS_UTILITY.GET_HASH_VALUE
name: DBMS_UTILITY.GET_HASH_VALUE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_HASH_VALUE

This function computes a hash value for the given string.

## Syntax

```sql
DBMS_UTILITY.GET_HASH_VALUE (
   name      VARCHAR2, 
   base      NUMBER, 
   hash_size NUMBER)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | String to be hashed. |
| base | NUMBER | IN | Base value for the returned hash value at which to start |
| hash_size | NUMBER) | IN | Desired size of the hash table |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.GET_HASH_VALUE ( name VARCHAR2, base NUMBER, hash_size NUMBER) RETURN NUMBER; Parameters Table 187-21 GET_HASH_VALUE Function Parameters Parameter Description name String to be hashed. base Base value for the returned hash value at which to start hash_size Desired size of the hash table Pragmas pragma restrict_references(get_hash_value, WNDS, RNDS, WNPS, RNPS); Return Values A hash value based on the input string. For example, to get a hash value on a string where the hash value should be between 1000 and 3047, use 1000 as the base value and 2048 as the hash_size value. Using a power of 2 for the hash_size parameter works best.