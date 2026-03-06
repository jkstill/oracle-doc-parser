---
id: 19c__DBMS_XDB_VERSION.GETCONTENTSCLOBBYRESID
name: DBMS_XDB_VERSION.GETCONTENTSCLOBBYRESID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.GETCONTENTSCLOBBYRESID

This function obtains contents as a CLOB .

## Syntax

```sql
DBMS_XDB_VERSION.GETCONTENTSCLOBYRESID(
   resid     DBMS_XDB.resid_type)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| resid | DBMS_XDB.resid_type) | IN | The resource id. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_XDB_VERSION.GETCONTENTSCLOBYRESID( resid DBMS_XDB.resid_type) RETURN CLOB; Parameters Table 199-5 GETCONTENTSCLOBYRESID Function Parameters Parameter Description resid The resource id.