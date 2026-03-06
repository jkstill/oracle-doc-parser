---
id: 19c__DBMS_IMMUTABLE_TABLE.DELETE_EXPIRED_ROWS
name: DBMS_IMMUTABLE_TABLE.DELETE_EXPIRED_ROWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_IMMUTABLE_TABLE
tags: [dbms_immutable_table]
source_file: dbms_immutable_table.html
---

# DBMS_IMMUTABLE_TABLE.DELETE_EXPIRED_ROWS

This procedure deletes some or all of the expired rows from the immutable table. This procedure does not commit.

## Syntax

```sql
DBMS_IMMUTABLE_TABLE.DELETE_EXPIRED_ROWS(
   schema_name                  IN VARCHAR2,
   table_name                   IN VARCHAR2, 
   before_timestamp             IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   number_of_rows_deleted       OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the immutable table. |
| before_timestamp | TIMESTAMP | IN | If the parameter is NULL , all expired rows in the table are deleted. If the parameter is not NULL and older than the timestamp calculated based on current time and row retention time, rows with timestamps less than the parameter value are deleted. If the parameter is younger than the timestamp calculated based on the current time and row retention time, the calculated timestamp is used, and all expired rows are deleted. The default value is NULL . |
| number_of_rows_deleted | NUMBER) | OUT | The number of rows deleted. |

## Usage Notes

Syntax DBMS_IMMUTABLE_TABLE.DELETE_EXPIRED_ROWS( schema_name IN VARCHAR2, table_name IN VARCHAR2, before_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, number_of_rows_deleted OUT NUMBER); Parameters Table 88-2 DELETE_EXPIRED_ROWS Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the immutable table. before_timestamp If the parameter is NULL , all expired rows in the table are deleted. If the parameter is not NULL and older than the timestamp calculated based on current time and row retention time, rows with timestamps less than the parameter value are deleted. If the parameter is younger than the timestamp calculated based on the current time and row retention time, the calculated timestamp is used, and all expired rows are deleted. The default value is NULL . number_of_rows_deleted The number of rows deleted.