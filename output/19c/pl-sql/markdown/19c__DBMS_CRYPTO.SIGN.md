---
id: 19c__DBMS_CRYPTO.SIGN
name: DBMS_CRYPTO.SIGN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.SIGN

This function signs RAW data using a private key assisted with key algorithm and sign algorithm, and returns a signature.

## Syntax

```sql
DBMS_CRYPTO.SIGN(
   src IN RAW,
   prv_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   sign_alg IN BINARY_INTEGER)
 RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax DBMS_CRYPTO.SIGN( src IN RAW, prv_key IN RAW, pubkey_alg IN BINARY_INTEGER, sign_alg IN BINARY_INTEGER) RETURN RAW; Parameters Table 42-20 SIGN Function Parameters Parameter Name Description src RAW data to be signed. prv_key Private key. pubkey_alg Specify the KEY_TYPE_RSA RSA key type. sign_alg Specify one of the algorithms that are listed in the Usage Notes. Usage Notes Table 42-21 SHA Hash Algorithms Hash Algorithm Description SIGN_SHA1_RSA SHA1 hash function with RSA SIGN_SHA1_RSA_X931 SHA1 hash function with RSA and X931 padding SIGN_SHA224_RSA SHA 224 bit hash function with RSA SIGN_SHA256_RSA SHA 256 bit hash function with RSA SIGN_SHA256_RSA_X931 SHA 256 bit hash function with RSA and X931 padding SIGN_SHA384_RSA SHA 384 bit hash function with RSA SIGN_SHA384_RSA_X931 SHA 384 bit hash function with RSA and X931 padding SIGN_SHA512_RSA SHA 384 bit hash function with RSA SIGN_SHA512_RSA_X931 SHA 384 bit hash function with RSA and X931 padding