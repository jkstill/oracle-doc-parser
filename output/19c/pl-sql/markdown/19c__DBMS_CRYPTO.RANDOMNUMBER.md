---
id: 19c__DBMS_CRYPTO.RANDOMNUMBER
name: DBMS_CRYPTO.RANDOMNUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.RANDOMNUMBER

This function returns an integer in the Oracle NUMBER datatype in the range of [0..2**128-1].

## Syntax

```sql
DBMS_CRYPTO.RANDOMNUMBER
 RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_CRYPTO.RANDOMNUMBER RETURN NUMBER; Pragmas pragma restrict_references(randomnumber,WNDS,RNDS,WNPS,RNPS);