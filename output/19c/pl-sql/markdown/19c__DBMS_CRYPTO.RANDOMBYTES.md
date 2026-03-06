---
id: 19c__DBMS_CRYPTO.RANDOMBYTES
name: DBMS_CRYPTO.RANDOMBYTES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.RANDOMBYTES

This function returns a RAW value containing a cryptographically secure pseudo-random sequence of bytes, which can be used to generate random material for encryption keys.

## Syntax

```sql
DBMS_CRYPTO.RANDOMBYTES (
   number_bytes IN POSITIVE)
 RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

The RANDOMBYTES function is based on the RSA X9.31 PRNG (Pseudo-Random Number Generator). Syntax DBMS_CRYPTO.RANDOMBYTES ( number_bytes IN POSITIVE) RETURN RAW; Pragmas pragma restrict_references(randombytes,WNDS,RNDS,WNPS,RNPS); Parameters Table 42-19 RANDOMBYTES Function Parameter Parameter Name Description number_bytes The number of pseudo-random bytes to be generated. Usage Note The number_bytes value should not exceed the maximum length of a RAW variable.