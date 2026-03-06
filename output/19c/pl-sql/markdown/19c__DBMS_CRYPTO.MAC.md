---
id: 19c__DBMS_CRYPTO.MAC
name: DBMS_CRYPTO.MAC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CRYPTO
tags: [dbms_crypto]
source_file: DBMS_CRYPTO.html
---

# DBMS_CRYPTO.MAC

This function applies Message Authentication Code (MAC) algorithms to data to provide keyed message protection.

## Syntax

```sql
DBMS_CRYPTO.MAC (
   src IN RAW,
   typ IN PLS_INTEGER,
   key IN RAW)
 RETURN RAW;

DBMS_CRYPTO.MAC (
   src IN BLOB,
   typ IN PLS_INTEGER
   key IN RAW)
 RETURN RAW;

DBMS_CRYPTO.MAC (
   src IN CLOB CHARACTER SET ANY_CS,
   typ IN PLS_INTEGER
   key IN RAW)
 RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

A MAC is a key-dependent one-way hash function. MACs have the same properties as the one-way hash function described in HASH Function , but they also include a key. Only someone with the identical key can verify the hash. Also refer to “When to Use Hash or Message Authentication Code (MAC) Functions” in DBMS_CRYPTO Operational Notes for more information about using MACs. See Table 42-4 for a list of MAC algorithms that have been defined for this package. Syntax DBMS_CRYPTO.MAC ( src IN RAW, typ IN PLS_INTEGER, key IN RAW) RETURN RAW; DBMS_CRYPTO.MAC ( src IN BLOB, typ IN PLS_INTEGER key IN RAW) RETURN RAW; DBMS_CRYPTO.MAC ( src IN CLOB CHARACTER SET ANY_CS, typ IN PLS_INTEGER key IN RAW) RETURN RAW; Pragmas pragma restrict_references(mac,WNDS,RNDS,WNPS,RNPS); Parameters Table 42-16 MAC Function Parameters Parameter Name Description src Source data to which MAC algorithms are to be applied. typ MAC algorithm to be used. key Key to be used for MAC algorithm.