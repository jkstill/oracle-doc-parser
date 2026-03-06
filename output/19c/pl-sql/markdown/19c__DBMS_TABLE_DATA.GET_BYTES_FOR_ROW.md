---
id: 19c__DBMS_TABLE_DATA.GET_BYTES_FOR_ROW
name: DBMS_TABLE_DATA.GET_BYTES_FOR_ROW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TABLE_DATA
tags: [dbms_table_data]
source_file: dbms_table_data.html
---

# DBMS_TABLE_DATA.GET_BYTES_FOR_ROW

This procedure returns a concatenated array of column byte values in column_data in the order of column positions for the particular row identified by row_id .

## Syntax

```sql
DBMS_TABLE_DATA.GET_BYTES_FOR_ROW(
   schema_name 		 IN VARCHAR2,
   table_name 	         IN VARCHAR2, 
   row_id 	             IN ROWID,
   column_data 	        IN OUT BLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| row_id | ROWID | IN | The row id. |
| column_data | BLOB) | IN OUT | The data in the row. |

## Usage Notes

Syntax DBMS_TABLE_DATA.GET_BYTES_FOR_ROW( schema_name IN VARCHAR2, table_name IN VARCHAR2, row_id IN ROWID, column_data IN OUT BLOB); Parameters Table 174-4 GET_BYTES_FOR_ROW Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the table. row_id The row id. column_data The data in the row. Usage Notes All arguments are required.