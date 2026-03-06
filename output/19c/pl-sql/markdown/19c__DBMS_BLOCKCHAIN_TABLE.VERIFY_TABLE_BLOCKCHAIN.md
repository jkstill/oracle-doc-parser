---
id: 19c__DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN
name: DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_BLOCKCHAIN_TABLE
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN

This procedure verifies all rows whose creation-time fall between the minimum value for the row-creation time from signed_bytes_previous and the maximum value for row-creation time from signed_bytes_latest and returns the number of successfully verified rows.

## Syntax

```sql
DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN(
   signed_bytes_latest        IN    BLOB,
   signed_bytes_previous      IN    BLOB,
   number_of_rows_verified    OUT   NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| signed_bytes_latest | BLOB | IN | A BLOB created by a call to get_signed_blockchain_digest . |
| signed_bytes_previous | BLOB | IN | A BLOB created by a call to get_signed_blockchain_digest before the signed_bytes_latest BLOB was created. |
| number_of_rows_verified | NUMBER) | OUT | The count of the rows in the blockchain table that was verified. |

## Usage Notes

Syntax DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN( signed_bytes_latest IN BLOB, signed_bytes_previous IN BLOB, number_of_rows_verified OUT NUMBER); Parameters Table 34-8 VERIFY_TABLE_BLOCKCHAIN Procedure Parameters Parameter Description signed_bytes_latest A BLOB created by a call to get_signed_blockchain_digest . signed_bytes_previous A BLOB created by a call to get_signed_blockchain_digest before the signed_bytes_latest BLOB was created. number_of_rows_verified The count of the rows in the blockchain table that was verified. Usage Notes The BLOBs in signed_bytes_latest and signed_bytes_previous must be associated with the same blockchain table.