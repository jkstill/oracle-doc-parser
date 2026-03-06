---
id: 19c__DBMS_XMLSTORE.SETKEYCOLUMN
name: DBMS_XMLSTORE.SETKEYCOLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORE
tags: [dbms_xmlstore]
source_file: DBMS_XMLSTORE.html
---

# DBMS_XMLSTORE.SETKEYCOLUMN

This method adds a column to the "key column list".

## Syntax

```sql
PROCEDURE setKeyColumn( 
   ctxHdl IN ctxType,
   colName IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| colName | VARCHAR2) | IN | (IN) |

## Usage Notes

The value for the column cannot be NULL . In case of update or delete, the columns in the key column list make up the WHERE clause of the statement. The key columns list must be specified before updates can complete; this is optional for delete operations PROCEDURE setKeyColumn( ctxHdl IN ctxType, colName IN VARCHAR2);