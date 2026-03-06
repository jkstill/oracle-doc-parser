---
id: 19c__DBMS_CRYPTO.HASH
name: DBMS_CRYPTO.HASH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.HASH

A one-way hash function takes a variable-length input string, the data, and converts it to a fixed-length (generally smaller) output string called a hash value . The hash value serves as a unique identifier (like a fingerprint) of the input data. You can use the hash value to verify whether data has been changed or not.

## Syntax

```sql
DBMS_CRYPTO.Hash (
   src IN RAW,
   typ IN PLS_INTEGER)
 RETURN RAW;

DBMS_CRYPTO.Hash (
   src IN BLOB,
   typ IN PLS_INTEGER)
 RETURN RAW;

DBMS_CRYPTO.Hash (
   src IN CLOB CHARACTER SET ANY_CS,
   typ IN PLS_INTEGER)
 RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Note that a one-way hash function is a hash function that works in one direction. It is easy to compute a hash value from the input data, but it is hard to generate data that hashes to a particular value. Consequently, one-way hash functions work well to ensure data integrity. Refer to “When to Use Hash or Message Authentication Code (MAC) Functions” in DBMS_CRYPTO Operational Notes for more information about using one-way hash functions. This function applies to data one of the supported cryptographic hash algorithms listed in Table 42-3 . Syntax DBMS_CRYPTO.Hash ( src IN RAW, typ IN PLS_INTEGER) RETURN RAW; DBMS_CRYPTO.Hash ( src IN BLOB, typ IN PLS_INTEGER) RETURN RAW; DBMS_CRYPTO.Hash ( src IN CLOB CHARACTER SET ANY_CS, typ IN PLS_INTEGER) RETURN RAW; Pragmas pragma restrict_references(hash,WNDS,RNDS,WNPS,RNPS); Parameters Table 42-15 HASH Function Parameters Parameter Name Description src The source data to be hashed. typ The hash algorithm to be used. Usage Note Oracle recommends that you use the SHA-1 (Secure Hash Algorithm) or SHA-2 because it is more resistant to brute-force attacks than MD4 or MD5. If you must use a Message Digest algorithm, then MD5 provides greater security than MD4.