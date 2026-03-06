---
id: 19c__DBMS_TABLE_DATA.GET_BYTES_FOR_COLUMN
name: DBMS_TABLE_DATA.GET_BYTES_FOR_COLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TABLE_DATA
tags: [dbms_table_data]
source_file: dbms_table_data.html
---

# DBMS_TABLE_DATA.GET_BYTES_FOR_COLUMN

This procedure returns the column_data in bytes for the particular column with name column_name for row_id row in the particular table identified by schema_name.table_name .

## Syntax

```sql
DBMS_TABLE_DATA.GET_BYTES_FOR_COLUMN(
   schema_name 		 IN VARCHAR2,
   table_name 	         IN VARCHAR2, 
   row_id 	             IN ROWID,
   column_name 	        IN VARCHAR2, 
   column_data 	        IN OUT BLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| row_id | ROWID | IN | The row id. |
| column_name | VARCHAR2 | IN | The column name. |
| column_data | BLOB) | IN OUT | The data in the column. |

## Usage Notes

Syntax DBMS_TABLE_DATA.GET_BYTES_FOR_COLUMN( schema_name IN VARCHAR2, table_name IN VARCHAR2, row_id IN ROWID, column_name IN VARCHAR2, column_data IN OUT BLOB); Parameters Table 174-2 GET_BYTES_FOR_COLUMN Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the table. row_id The row id. column_name The column name. column_data The data in the column. Usage Notes All arguments are required.