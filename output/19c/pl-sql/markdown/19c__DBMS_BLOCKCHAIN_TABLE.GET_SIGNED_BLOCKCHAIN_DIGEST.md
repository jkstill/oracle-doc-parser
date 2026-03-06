---
id: 19c__DBMS_BLOCKCHAIN_TABLE.GET_SIGNED_BLOCKCHAIN_DIGEST
name: DBMS_BLOCKCHAIN_TABLE.GET_SIGNED_BLOCKCHAIN_DIGEST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_BLOCKCHAIN_TABLE
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE.GET_SIGNED_BLOCKCHAIN_DIGEST

This function generates and returns the signed digest on specified blockchain table using schema user's certificate. The signed_bytes , signed_row_indexes , and schema_certificate_guid are also returned.

## Syntax

```sql
DBMS_BLOCKCHAIN_TABLE.GET_SIGNED_BLOCKCHAIN_DIGEST(
   schema_name 		   IN      VARCHAR2,
   table_name 	           IN      VARCHAR2, 
   signed_bytes               IN OUT  BLOB,
   signed_rows_indexes        OUT     ORABCTAB_ROW_ARRAY_T,
   schema_certificate_guid    OUT     RAW,
   signature_algo             IN      NUMBER default SIGN_ALGO_DEFAULT)
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the blockchain table. |
| signed_bytes | BLOB | IN OUT | The BLOB value that contains a header followed by an array of row-info. The caller must pass an empty BLOB for this parameter. |
| signed_rows_indexes | ORABCTAB_ROW_ARRAY_T | OUT | This parameter specifies the rows in the blockchain that were digitally signed. |
| schema_certificate_guid | RAW | OUT | The PKI certificate of the owner of the blockchain table that was used to produce the digital signature. |
| signature_algo | NUMBER | IN | The digital signature the algorithm must use. The parameter must be one of the following package constants: SIGN_ALGO_RSA_SHA2_256 , SIGN_ALGO_RSA_SHA2_384 , or SIGN_ALGO_RSA_SHA2_512 . |

**Returns:** `RAW`

## Usage Notes

Syntax DBMS_BLOCKCHAIN_TABLE.GET_SIGNED_BLOCKCHAIN_DIGEST( schema_name IN VARCHAR2, table_name IN VARCHAR2, signed_bytes IN OUT BLOB, signed_rows_indexes OUT ORABCTAB_ROW_ARRAY_T, schema_certificate_guid OUT RAW, signature_algo IN NUMBER default SIGN_ALGO_DEFAULT) RETURN RAW; Parameters Table 34-5 GET_SIGNED_BLOCKCHAIN_DIGEST Function Parameters Parameter Description schema_name The name of the schema. table_name The name of the blockchain table. signed_bytes The BLOB value that contains a header followed by an array of row-info. The caller must pass an empty BLOB for this parameter. signed_rows_indexes This parameter specifies the rows in the blockchain that were digitally signed. schema_certificate_guid The PKI certificate of the owner of the blockchain table that was used to produce the digital signature. signature_algo The digital signature the algorithm must use. The parameter must be one of the following package constants: SIGN_ALGO_RSA_SHA2_256 , SIGN_ALGO_RSA_SHA2_384 , or SIGN_ALGO_RSA_SHA2_512 . Usage Notes Database computes the signature on signed_bytes using PKI private key of blockchain table owner. The certificate of blockchain table owner must be added to database using DBMS_USER_CERTS.ADD_CERTIFICATE() . The PKI private key and certificate of blockchain table owner must exist in a wallet located under <WALLET_ROOT>/bctable/ directory for a non-container database. The PKI private key and certificate of blockchain table owner must exist in a wallet located under <WALLET_ROOT>/pdb_guid/bctable/ directory for a container database. A blockchain table digest created by the GET_SIGNED_BLOCKCHAIN_DIGEST function has table information specific to a pluggable database. Such a digest can be used only in the pluggable database in which the digest was created and only for the table that was used to create the digest. For DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN , these requirements mean that both blockchain table digests must have been generated in the current pluggable database for the same blockchain table. For example, suppose you create a digest for a blockchain table in pluggable database A, use Data Pump to export the blockchain table, and use Data Pump to import the blockchain table into pluggable database B. The blockchain table digest created in pluggable database A cannot be used in pluggable database B. You need to create a new blockchain table digest in pluggable database B. Note: The bctable subdirectory is the name of a database component that uses wallets. It is not the name of a blockchain table. See Also: Oracle Database Administrator’s Guide Note: The bctable subdirectory is the name of a database component that uses wallets. It is not the name of a blockchain table. See Also: Oracle Database Administrator’s Guide