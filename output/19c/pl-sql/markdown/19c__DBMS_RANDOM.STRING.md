---
id: 19c__DBMS_RANDOM.STRING
name: DBMS_RANDOM.STRING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RANDOM
tags: [dbms_random]
source_file: DBMS_RANDOM.html
---

# DBMS_RANDOM.STRING

This function gets a random string.

## Syntax

```sql
DBMS_RANDOM.STRING
   opt  IN  CHAR,
   len  IN  NUMBER)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| opt | CHAR | IN | Specifies what the returning string looks like: 'u', 'U' - returning string in uppercase alpha characters 'l', 'L' - returning string in lowercase alpha characters 'a', 'A' - returning string in mixed case alpha characters 'x', 'X' - returning string in uppercase alpha-numeric characters 'p', 'P' - returning string in any printable characters. Otherwise the returning string is in uppercase alpha characters. |
| len | NUMBER) | IN | Length of the returning string |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_RANDOM.STRING opt IN CHAR, len IN NUMBER) RETURN VARCHAR2; Pragmas PRAGMA restrict_references (string, WNDS); Parameters Table 136-6 STRING Function Parameters Parameter Description opt Specifies what the returning string looks like: 'u', 'U' - returning string in uppercase alpha characters 'l', 'L' - returning string in lowercase alpha characters 'a', 'A' - returning string in mixed case alpha characters 'x', 'X' - returning string in uppercase alpha-numeric characters 'p', 'P' - returning string in any printable characters. Otherwise the returning string is in uppercase alpha characters. len Length of the returning string Return Values Table 136-7 STRING Function Return Values Parameter Description VARCHAR2 Returns a VARCHAR2