---
id: 19c__DBMS_CRYPTO.ENCRYPT
name: DBMS_CRYPTO.ENCRYPT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.ENCRYPT

These procedures encrypt LOB data using a stream or block cipher with a user supplied key and optional IV (initialization vector).

## Syntax

```sql
DBMS_CRYPTO.ENCRYPT(
   dst IN OUT NOCOPY BLOB,
   src IN            BLOB,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);

DBMS_CRYPTO.ENCRYPT(
   dst IN OUT NOCOPY BLOB,
   src IN            CLOB         CHARACTER SET ANY_CS,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);
```

## Usage Notes

Syntax DBMS_CRYPTO.ENCRYPT( dst IN OUT NOCOPY BLOB, src IN BLOB, typ IN PLS_INTEGER, key IN RAW, iv IN RAW DEFAULT NULL); DBMS_CRYPTO.ENCRYPT( dst IN OUT NOCOPY BLOB, src IN CLOB CHARACTER SET ANY_CS, typ IN PLS_INTEGER, key IN RAW, iv IN RAW DEFAULT NULL); Pragmas pragma restrict_references(encrypt,WNDS,RNDS,WNPS,RNPS); Parameters Table 42-14 ENCRYPT Procedure Parameters Parameter Name Description dst LOB locator of output data. The value in the output LOB < dst > will be overwritten. src LOB locator of input data. typ Stream or block cipher type and modifiers to be used. key Encryption key to be used for encrypting data. iv Optional initialization vector for block ciphers. Default is NULL . Usage Notes See DBMS_DEBUG Operational Notes for more information about the conversion rules for the ENCRYPT procedure.