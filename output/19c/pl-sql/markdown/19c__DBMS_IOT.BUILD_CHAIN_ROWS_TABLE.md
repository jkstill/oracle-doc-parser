---
id: 19c__DBMS_IOT.BUILD_CHAIN_ROWS_TABLE
name: DBMS_IOT.BUILD_CHAIN_ROWS_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_IOT
tags: [dbms_iot]
source_file: DBMS_IOT.html
---

# DBMS_IOT.BUILD_CHAIN_ROWS_TABLE

This procedure creates a table into which references to the chained rows for an index-organized table can be placed using the ANALYZE command.

## Syntax

```sql
DBMS_IOT.BUILD_CHAIN_ROWS_TABLE (
   owner               IN VARCHAR2,
   iot_name            IN VARCHAR2,
   chainrow_table_name IN VARCHAR2 default 'IOT_CHAINED_ROWS');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Owner of the index-organized table. |
| iot_name | VARCHAR2 | IN | Index-organized table name. |
| chainrow_table_name | VARCHAR2 | IN | Intended name for the chained-rows table. |

## Usage Notes

Syntax DBMS_IOT.BUILD_CHAIN_ROWS_TABLE ( owner IN VARCHAR2, iot_name IN VARCHAR2, chainrow_table_name IN VARCHAR2 default 'IOT_CHAINED_ROWS'); Parameters Table 91-2 BUILD_CHAIN_ROWS_TABLE Procedure Parameters Parameter Description owner Owner of the index-organized table. iot_name Index-organized table name. chainrow_table_name Intended name for the chained-rows table. Usage Notes You should create a separate chained-rows table for each index-organized table to accommodate its primary key. Examples CREATE TABLE l(a char(16),b char(16), c char(16), d char(240), PRIMARY KEY(a,b,c)) ORGANIZATION INDEX pctthreshold 10 overflow; EXECUTE DBMS_IOT.BUILD_CHAIN_ROWS_TABLE('SYS','L','LC'); A chained-row table is created with the following columns: Column Name Null? Type ------------------------------ -------- ---- OWNER_NAME VARCHAR2(30) TABLE_NAME VARCHAR2(30) CLUSTER_NAME VARCHAR2(30) PARTITION_NAME VARCHAR2(30) SUBPARTITION_NAME VARCHAR2(30) HEAD_ROWID ROWID TIMESTAMP DATE A CHAR(16) B CHAR(16) C CHAR(16)