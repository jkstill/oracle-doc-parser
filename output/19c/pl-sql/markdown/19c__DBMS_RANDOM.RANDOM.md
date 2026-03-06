---
id: 19c__DBMS_RANDOM.RANDOM
name: DBMS_RANDOM.RANDOM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RANDOM
tags: [dbms_random]
source_file: DBMS_RANDOM.html
---

# DBMS_RANDOM.RANDOM

This deprecated procedure generates a random number.

## Syntax

```sql
DBMS_RANDOM.RANDOM
   RETURN binary_integer;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| binary_integer |  |  | Returns a random integer greater or equal to -power(2,31) and less than power(2,31) |

**Returns:** `binary_integer`

## Usage Notes

Note: This function is deprecated with Release 11gR1 and, although currently supported, it should not be used. Note: This function is deprecated with Release 11gR1 and, although currently supported, it should not be used. Syntax DBMS_RANDOM.RANDOM RETURN binary_integer; Pragmas PRAGMA restrict_references (random, WNDS); Return Values Table 136-4 RANDOM Function Parameters Parameter Description binary_integer Returns a random integer greater or equal to -power(2,31) and less than power(2,31)