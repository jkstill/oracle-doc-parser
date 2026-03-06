---
id: 19c__DBMS_BLOCKCHAIN_TABLE.SIGN_ROW
name: DBMS_BLOCKCHAIN_TABLE.SIGN_ROW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_BLOCKCHAIN_TABLE
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE.SIGN_ROW

This procedure can be used by the current user to provide a signature on row content of a previously inserted row. The transaction that inserted the row into the blockchain table must have committed before the SIGN_ROW procedure is called.

## Syntax

```sql
DBMS_BLOCKCHAIN_TABLE.SIGN_ROW(
   schema_name               IN VARCHAR2,
   table_name                IN VARCHAR2,
   instance_id               IN NUMBER, 
   chain_id 		   IN NUMBER,
   sequence_id               IN NUMBER,
   hash                      IN RAW DEFAULT NULL,
   signature                 IN RAW,
   certificate_guid          IN RAW,
   signature_algo            IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the blockchain table. |
| instance_id | NUMBER | IN | The instance on which the row was inserted. |
| chain_id | NUMBER | IN | The chain containing the row to be signed. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| sequence_id | NUMBER | IN | The position of the row on the chain. Valid values are 1 , 2 , and so on. |
| hash | RAW | IN | If non-NULL , the expected value of the hash in the row to be signed. If NULL , the hash in the row to be signed is not checked. |
| signature | RAW | IN | The user's digital signature on the hash value stored in the row. |
| certificate_guid | RAW | IN | A unique identifier for the certificate stored in the database that may be used to verify the digital signature. |
| signature_algo | NUMBER) | IN | The algorithm used to create the digital signature. The algorithm must be one of the following constants defined in the DBMS_BLOCKCHAIN_TABLE package: SIGN_ALGO_RSA_SHA2_256 SIGN_ALGO_RSA_SHA2_384 SIGN_ALGO_RSA_SHA2_512 |

## Usage Notes

Syntax DBMS_BLOCKCHAIN_TABLE.SIGN_ROW( schema_name IN VARCHAR2, table_name IN VARCHAR2, instance_id IN NUMBER, chain_id IN NUMBER, sequence_id IN NUMBER, hash IN RAW DEFAULT NULL, signature IN RAW, certificate_guid IN RAW, signature_algo IN NUMBER); Parameters Table 34-6 SIGN_ROW Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the blockchain table. instance_id The instance on which the row was inserted. chain_id The chain containing the row to be signed. There are 32 chains in each instance, and they are numbered from 0 to 31. sequence_id The position of the row on the chain. Valid values are 1 , 2 , and so on. hash If non-NULL , the expected value of the hash in the row to be signed. If NULL , the hash in the row to be signed is not checked. signature The user's digital signature on the hash value stored in the row. certificate_guid A unique identifier for the certificate stored in the database that may be used to verify the digital signature. signature_algo The algorithm used to create the digital signature. The algorithm must be one of the following constants defined in the DBMS_BLOCKCHAIN_TABLE package: SIGN_ALGO_RSA_SHA2_256 SIGN_ALGO_RSA_SHA2_384 SIGN_ALGO_RSA_SHA2_512 Note: For information on hidden columns in blockchain tables, see Hidden Columns in Blockchain Tables Note: For information on hidden columns in blockchain tables, see Hidden Columns in Blockchain Tables Usage Notes All parameters are required input parameters except for hash . The database will verify that: the current user’s obj# matches the user# hidden column value (ensures that the user owns the row) the user has insert privileges for the blockchain table ‘schema_name’.’table_name’ the hash (if provided) matches the hash column content for the row the signature column value for the specific row identified by ‘instance_id’ , ‘chain_id’ , and ‘sequence_id’ is NULL if the verification succeeds, the signature value is stored for the row.