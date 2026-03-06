---
id: 19c__DBMS_XMLSAVE.SETKEYCOLUMN
name: DBMS_XMLSAVE.SETKEYCOLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETKEYCOLUMN

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

The value for the column cannot be NULL . In case of update or delete, the columns in the key column list make up the WHERE clause of the statement. The key columns list must be specified before updates can complete; this is optional for delete operations. Syntax PROCEDURE setKeyColumn( ctxHdl IN ctxType, colName IN VARCHAR2); Parameters Table 209-18 SETKEYCOLUMN Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. colName (IN) Column to be added to the key column list; cannot be NULL .