---
id: 19c__DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_HASH
name: DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_HASH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_BLOCKCHAIN_TABLE
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_HASH

This procedure returns the bytes in column_data that the database hashed to get the hash value for the row identified by parameters instance_id , chain_id , and sequence_id . These bytes are a concatenation of metadata and data bytes for each column of the table in column position order, followed by the hash value for the previous row in the chain.

## Syntax

```sql
DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_HASH(
   schema_name 		 IN VARCHAR2,
   table_name 	         IN VARCHAR2, 
   instance_id 		 IN NUMBER, 
   chain_id                  IN NUMBER,
   sequence_id 	        IN NUMBER,
   data_format 	        IN NUMBER, 
   row_data 	           IN OUT BLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the blockchain table. |
| instance_id | NUMBER | IN | The instance that inserted the row. Valid values are 1 , 2 , and so on. |
| chain_id | NUMBER | IN | The chain containing the row. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| sequence_id | NUMBER | IN | The position of the row on the specified chain. |
| data_format | NUMBER | IN | The version of the data layout for the hash in the specified row. Must be 1 in this release. |
| row_data | BLOB) | IN OUT | The bytes for the specified row in the specified data format that can be input to the cryptographic hash function to verify the value of the hash in the row. Any bytes in the BLOB are overwritten. |

## Usage Notes

Syntax DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_HASH( schema_name IN VARCHAR2, table_name IN VARCHAR2, instance_id IN NUMBER, chain_id IN NUMBER, sequence_id IN NUMBER, data_format IN NUMBER, row_data IN OUT BLOB); Parameters Table 34-3 GET_BYTES_FOR_ROW_HASH Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the blockchain table. instance_id The instance that inserted the row. Valid values are 1 , 2 , and so on. chain_id The chain containing the row. There are 32 chains in each instance, and they are numbered from 0 to 31. sequence_id The position of the row on the specified chain. data_format The version of the data layout for the hash in the specified row. Must be 1 in this release. row_data The bytes for the specified row in the specified data format that can be input to the cryptographic hash function to verify the value of the hash in the row. Any bytes in the BLOB are overwritten. Usage Notes All parameters are required input parameters. The metadata bytes for a column are 20 bytes that encode the blockchain algorithm version used to hash the row, the column position, the column data type, whether the column value is NULL , and the actual length of the column value in bytes. The column data bytes are the actual bytes representing the column value on disk for non-character columns. For character columns, the values are normalized to specific character sets. For CHAR and NCHAR columns, blank trimming is also done. Few metadata bytes are reserved for future use.