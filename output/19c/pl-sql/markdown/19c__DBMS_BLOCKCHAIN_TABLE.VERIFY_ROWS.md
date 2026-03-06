---
id: 19c__DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS
name: DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_BLOCKCHAIN_TABLE
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS

Verifies all rows on all applicable chains for integrity of HASH column value and optionally the SIGNATURE column value for rows created in the range of low_timestamp to high_timestamp . An appropriate exception is thrown if the integrity of chains is compromised.

## Syntax

```sql
DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS(
   schema_name                  IN VARCHAR2,
   table_name                   IN VARCHAR2, 
   low_timestamp                IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   high_timestamp               IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, 
   instance_id                  IN NUMBER DEFAULT NULL, 
   chain_id                     IN NUMBER DEFAULT NULL,
   number_of_rows_verified      OUT NUMBER,
   verify_signature             IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the blockchain table. |
| low_timestamp | TIMESTAMP | IN | If specified, the low end of the time range for verifying rows. The default value is NULL . |
| high_timestamp | TIMESTAMP | IN | If specified, the high end of the time range for verifying rows. The default value is NULL . |
| instance_id | NUMBER | IN | If specified, restricts row verification to rows inserted on the specified instance. |
| chain_id | NUMBER | IN | If specified, restricts row verification to rows on the specified chain. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| number_of_rows_verified | NUMBER | OUT | The number of rows verified. |
| verify_signature | BOOLEAN | IN | If verify_signature is TRUE , both the hash on each row and any signature on the row are verified. If verify_signature is FALSE , only the hash on each row is verified. The default value is TRUE . |

## Usage Notes

Syntax DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS( schema_name IN VARCHAR2, table_name IN VARCHAR2, low_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, high_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, instance_id IN NUMBER DEFAULT NULL, chain_id IN NUMBER DEFAULT NULL, number_of_rows_verified OUT NUMBER, verify_signature IN BOOLEAN DEFAULT TRUE); Parameters Table 34-7 VERIFY_ROWS Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the blockchain table. low_timestamp If specified, the low end of the time range for verifying rows. The default value is NULL . high_timestamp If specified, the high end of the time range for verifying rows. The default value is NULL . instance_id If specified, restricts row verification to rows inserted on the specified instance. chain_id If specified, restricts row verification to rows on the specified chain. There are 32 chains in each instance, and they are numbered from 0 to 31. number_of_rows_verified The number of rows verified. verify_signature If verify_signature is TRUE , both the hash on each row and any signature on the row are verified. If verify_signature is FALSE , only the hash on each row is verified. The default value is TRUE . Usage Notes The hash on the first element in the time range for verifying rows in a chain is verified only if its sequence number is 1 . schema_name and table_name are required input parameters All others input parameters are optional, with the following exceptions: If chain_id is specified, instance_id must be specified Valid values for instance_id are 1, 2, … etc. If neither instance_id , nor chain_id is specified, then it implies *all* chains. If only instance_id is specified, then it implies *all* chains on that instance. If both are specified, it implies the specific chain provided by the combination. If both low_timestamp and high_timestamp are specified, then high_timestamp must be later than low_timestamp . If low_timestamp is not specified, then the range is the oldest row in the blockchain to high_timestamp . If high_timestamp is not specified then the range is low_timestamp to the timestamp of the last row inserted in the table.