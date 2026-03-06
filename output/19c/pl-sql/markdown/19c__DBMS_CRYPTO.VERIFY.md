---
id: 19c__DBMS_CRYPTO.VERIFY
name: DBMS_CRYPTO.VERIFY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.VERIFY

This function verifies RAW data using the signature, public key assisted with key algorithm, and sign algorithm. It returns TRUE if the signature was verified.

## Syntax

```sql
DBMS_CRYPTO.VERIFY(
   src IN RAW,
   sign IN RAW,
   pub_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   sign_alg  IN BINARY_INTEGER)
 RETURN BOOLEAN;
```

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_CRYPTO.VERIFY( src IN RAW, sign IN RAW, pub_key IN RAW, pubkey_alg IN BINARY_INTEGER, sign_alg IN BINARY_INTEGER) RETURN BOOLEAN; Parameters Table 42-22 VERIFY Function Parameters Parameter Name Description src RAW data to be verified. sign Message signature. pub_key Public key. pubkey_alg Specify the KEY_TYPE_RSA RSA key type. sign_alg Specify one of the algorithms that are listed the Usage Notes. Usage Notes Table 42-23 SHA Hash Algorithms Hash Algorithm Description SIGN_SHA1_RSA SHA hash function with RSA SIGN_SHA1_RSA_X931 SHA hash function with RSA and X931 padding SIGN_SHA224_RSA SHA 224 bit hash function with RSA SIGN_SHA256_RSA SHA 256 bit hash function with RSA SIGN_SHA256_RSA_X931 SHA 256 bit hash function with RSA and X931 padding SIGN_SHA384_RSA SHA 384 bit hash function with RSA SIGN_SHA384_RSA_X931 SHA 384 bit hash function with RSA and X931 padding SIGN_SHA512_RSA SHA 384 bit hash function with RSA SIGN_SHA512_RSA_X931 SHA 384 bit hash function with RSA and X931 padding