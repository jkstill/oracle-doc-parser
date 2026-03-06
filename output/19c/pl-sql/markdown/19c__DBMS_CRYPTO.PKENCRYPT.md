---
id: 19c__DBMS_CRYPTO.PKENCRYPT
name: DBMS_CRYPTO.PKENCRYPT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.PKENCRYPT

This function encrypts RAW data using a public key assisted with key algorithm and encryption algorithm and returns encrypted data.

## Syntax

```sql
DBMS_CRYPTO.PKENCRYPT(
   src IN RAW,
   pub_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   enc_alg  IN BINARY_INTEGER)
 RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax DBMS_CRYPTO.PKENCRYPT( src IN RAW, pub_key IN RAW, pubkey_alg IN BINARY_INTEGER, enc_alg IN BINARY_INTEGER) RETURN RAW; Parameters Table 42-18 PKENCRYPT Function Parameters Parameter Name Description src RAW data to be encrypted. pub_key Public key. pubkey_alg Specify the KEY_TYPE_RSA RSA key type. enc_alg Specify the algorithm PKENCRYPT_RSA_PKCS1_OAEP, for RSA Public Key Cryptosystem with PKCS1 and OAEP padding.