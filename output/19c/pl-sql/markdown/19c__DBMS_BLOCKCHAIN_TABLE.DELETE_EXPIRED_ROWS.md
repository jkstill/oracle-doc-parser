---
id: 19c__DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS
name: DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_BLOCKCHAIN_TABLE
tags: [dbms_blockchain_table]
source_file: dbms_blockchain_table.html
---

# DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS

This procedure deletes rows outside the retention window created before_timestamp if the time stamp is specified; otherwise, deletes all rows outside the retention window. The number of rows deleted is returned in number_of_rows_deleted parameter.

## Syntax

```sql
DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS(
   schema_name 		 IN VARCHAR2,
   table_name 	         IN VARCHAR2, 
   before_timestamp 	   IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   number_of_rows_deleted     OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. |
| table_name | VARCHAR2 | IN | The name of the blockchain table. |
| before_timestamp | TIMESTAMP | IN | The end time for the range of rows deleted by the procedure, subject to the row retention time currently associated with the blockchain table. This is an optional parameter. The default value is NULL . |
| number_of_rows_deleted | NUMBER) | OUT | The count of the number of rows deleted. |

## Usage Notes

Syntax DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS( schema_name IN VARCHAR2, table_name IN VARCHAR2, before_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, number_of_rows_deleted OUT NUMBER); Parameters Table 34-2 DELETE_EXPIRED_ROWS Procedure Parameters Parameter Description schema_name The name of the schema. table_name The name of the blockchain table. before_timestamp The end time for the range of rows deleted by the procedure, subject to the row retention time currently associated with the blockchain table. This is an optional parameter. The default value is NULL . number_of_rows_deleted The count of the number of rows deleted.