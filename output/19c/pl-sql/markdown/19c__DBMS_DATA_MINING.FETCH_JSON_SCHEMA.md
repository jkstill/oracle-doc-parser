---
id: 19c__DBMS_DATA_MINING.FETCH_JSON_SCHEMA
name: DBMS_DATA_MINING.FETCH_JSON_SCHEMA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.FETCH_JSON_SCHEMA

User can fetch and read JSON schema from the ALL_MINING_ALGORITHMS view. This function returns the pre-registered JSON schema for R extensible algorithms.

## Syntax

```sql
DBMS_DATA_MINING.FETCH_JSON_SCHEMA RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| RETURN | CLOB | IN | This function returns the pre-registered JSON schema for R extensibility. The default value is CLOB . |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_DATA_MINING.FETCH_JSON_SCHEMA RETURN CLOB; Parameters Table 47-70 FETCH_JSON_SCHEMA Procedure Parameters Parameter Description RETURN This function returns the pre-registered JSON schema for R extensibility. The default value is CLOB . Usage Note If a user wants to register a new algorithm using the algorithm registration function, they must fetch and follow the pre-registered JSON schema using this function, when they create the required JSON object metadata, and then pass it to the registration function.