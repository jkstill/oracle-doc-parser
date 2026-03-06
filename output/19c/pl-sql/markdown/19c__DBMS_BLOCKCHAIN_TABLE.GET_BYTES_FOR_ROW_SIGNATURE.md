---
id: 19c__DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_SIGNATURE
name: DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_SIGNATURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_BLOCKCHAIN_TABLE
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_SIGNATURE

The routine returns in row_data the bytes in the hash in the row without any metadata. No other columns are involved either in the row or in the previous row.

## Syntax

```sql
DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_SIGNATURE(
   schema_name 		 IN VARCHAR2,
   table_name 	         IN VARCHAR2, 
   instance_id 		 IN NUMBER, 
   chain_id 		    IN NUMBER,
   sequence_id 	        IN NUMBER,
   data_format 	        IN NUMBER, 
   row_data                   IN OUT BLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the blockchain table. |
| instance_id | NUMBER | IN | The instance on which the row was inserted. Valid values are 1 , 2 , and so on. |
| chain_id | NUMBER | IN | The chain on which the row was inserted. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| sequence_id | NUMBER | IN | The position of the row on the chain. |
| data_format | NUMBER | IN | The format of the data in row_data . The value must be 1 in the DB20c release. |
| row_data | BLOB) | IN OUT | A sequence of bytes that must be signed. |

## Usage Notes

Syntax DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_SIGNATURE( schema_name IN VARCHAR2, table_name IN VARCHAR2, instance_id IN NUMBER, chain_id IN NUMBER, sequence_id IN NUMBER, data_format IN NUMBER, row_data IN OUT BLOB); Parameters Table 34-4 GET_BYTES_FOR_ROW_SIGNATURE Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the blockchain table. instance_id The instance on which the row was inserted. Valid values are 1 , 2 , and so on. chain_id The chain on which the row was inserted. There are 32 chains in each instance, and they are numbered from 0 to 31. sequence_id The position of the row on the chain. data_format The format of the data in row_data . The value must be 1 in the DB20c release. row_data A sequence of bytes that must be signed. Usage Notes All parameters are required input parameters.