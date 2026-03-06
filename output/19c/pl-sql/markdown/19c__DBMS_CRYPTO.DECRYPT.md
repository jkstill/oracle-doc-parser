---
id: 19c__DBMS_CRYPTO.DECRYPT
name: DBMS_CRYPTO.DECRYPT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.DECRYPT

These procedures decrypt LOB data using a stream or block cipher with a user supplied key and optional IV (initialization vector).

## Syntax

```sql
DBMS_CRYPTO.DECRYPT(
   dst IN OUT NOCOPY BLOB,
   src IN            BLOB,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);

DBMS_CRYPT.DECRYPT(
   dst IN OUT NOCOPY CLOB         CHARACTER SET ANY_CS,
   src IN            BLOB,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);
```

## Usage Notes

Syntax DBMS_CRYPTO.DECRYPT( dst IN OUT NOCOPY BLOB, src IN BLOB, typ IN PLS_INTEGER, key IN RAW, iv IN RAW DEFAULT NULL); DBMS_CRYPT.DECRYPT( dst IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, src IN BLOB, typ IN PLS_INTEGER, key IN RAW, iv IN RAW DEFAULT NULL); Pragmas pragma restrict_references(decrypt,WNDS,RNDS,WNPS,RNPS); Parameters Table 42-12 DECRYPT Procedure Parameters Parameter Name Description dst LOB locator of output data. The value in the output LOB < dst > will be overwritten. src LOB locator of input data. typ Stream or block cipher type and modifiers to be used. key Key to be used for decryption. iv Optional initialization vector for block ciphers. Default is all zeroes.