---
id: 19c__DBMS_XMLSTORE.SETUPDATECOLUMN
name: DBMS_XMLSTORE.SETUPDATECOLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORE
tags: [dbms_xmlstore]
source_file: DBMS_XMLSTORE.html
---

# DBMS_XMLSTORE.SETUPDATECOLUMN

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

In case of insert, the default is to insert values to all the columns in the table. In case of updates, the default is to only update the columns corresponding to the tags present in the ROW element of the XML document. When the update column list is specified, the columns making up this list alone will get updated or inserted into. Note that if a user passes an XML file for INSERTXML to DBMS_XMLSTORE which contains extra elements (ones that do not match up to any columns in the table), Oracle will try to insert into those columns unless setUpdateColumn is used. The use of setUpdateColumn is optional only if the elements in the XML file match up to the columns in the table. PROCEDURE setUpdateColumn( ctxHdl IN ctxType, colName IN VARCHAR2);