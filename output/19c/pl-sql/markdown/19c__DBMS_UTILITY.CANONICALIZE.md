---
id: 19c__DBMS_UTILITY.CANONICALIZE
name: DBMS_UTILITY.CANONICALIZE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.CANONICALIZE

This procedure canonicalizes the given string. The procedure handles a single reserved or key word (such as 'table'), and strips off white spaces for a single identifier so that ' table ' becomes TABLE.

## Syntax

```sql
DBMS_UTILITY.CANONICALIZE(
   name           IN    VARCHAR2,
   canon_name     OUT   VARCHAR2,
   canon_len      IN    BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | String to be canonicalized |
| canon_name | VARCHAR2 | OUT | Canonicalized string |
| canon_len | BINARY_INTEGER) | IN | Length of the string (in bytes) to canonicalize |

## Usage Notes

Syntax DBMS_UTILITY.CANONICALIZE( name IN VARCHAR2, canon_name OUT VARCHAR2, canon_len IN BINARY_INTEGER); Parameters Table 187-9 CANONICALIZE Procedure Parameters Parameter Description name String to be canonicalized canon_name Canonicalized string canon_len Length of the string (in bytes) to canonicalize Return Values Returns the first canon_len bytes in canon_name . Usage Notes If name is NULL, canon_name becomes NULL. If name is not a dotted name, and if name begins and ends with a double quote, remove both quotes. Alternatively, convert to upper case with NLS_UPPER. Note that this case does not include a name with special characters, such as a space, but is not doubly quoted. If name is a dotted name (such as a."b".c), for each component in the dotted name in the case in which the component begins and ends with a double quote, no transformation will be performed on this component. Alternatively, convert to upper case with NLS_UPPER and apply begin and end double quotes to the capitalized form of this component. In such a case, each canonicalized component will be concatenated together in the input position, separated by ".". Any other character after a[.b]* will be ignored. The procedure does not handle cases like 'A B.' Examples a becomes A "a" becomes a "a".b becomes "a"."B" "a".b,c.f becomes "a"."B" with ",c.f" ignored.