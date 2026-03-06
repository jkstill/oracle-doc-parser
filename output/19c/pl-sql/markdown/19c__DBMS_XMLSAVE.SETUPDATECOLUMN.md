---
id: 19c__DBMS_XMLSAVE.SETUPDATECOLUMN
name: DBMS_XMLSAVE.SETUPDATECOLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETUPDATECOLUMN

SETUPDATECOLUMN adds a column to the update column list.

## Syntax

```sql
PROCEDURE setUpdateColumn( 
   ctxHdl IN ctxType,
   colName IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| colName | VARCHAR2) | IN | (IN) |

## Usage Notes

In case of insert, the default is to insert values to all the columns in the table. In case of updates, the default is to only update the columns corresponding to the tags present in the ROW element of the XML document. When the update column list is specified, the columns making up this list alone will get updated or inserted into. Syntax PROCEDURE setUpdateColumn( ctxHdl IN ctxType, colName IN VARCHAR2); Parameters Table 209-22 SETUPDATECOLUMN Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. colName (IN) Column to be added to the update column list.