---
id: 19c__DBMS_CRYPTO.PKDECRYPT
name: DBMS_CRYPTO.PKDECRYPT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.PKDECRYPT

This function decrypts RAW data using a private key assisted with key algorithm and encryption algorithm and returns decrypted data.

## Syntax

```sql
DBMS_CRYPTO.PKDECRYPT(
   src IN RAW,
   prv_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   enc_alg  IN BINARY_INTEGER)
 RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax DBMS_CRYPTO.PKDECRYPT( src IN RAW, prv_key IN RAW, pubkey_alg IN BINARY_INTEGER, enc_alg IN BINARY_INTEGER) RETURN RAW; Parameters Table 42-17 PKDECRYPT Function Parameters Parameter Name Description src RAW data to be decrypted. prv_key Private key. pubkey_alg Specify the KEY_TYPE_RSA RSA key type. enc_alg Specify the algorithm PKENCRYPT_RSA_PKCS1_OAEP, for RSA Public Key Cryptosystem with PKCS1 and OAEP padding.