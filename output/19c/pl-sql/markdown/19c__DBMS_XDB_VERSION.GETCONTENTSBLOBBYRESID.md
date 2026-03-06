---
id: 19c__DBMS_XDB_VERSION.GETCONTENTSBLOBBYRESID
name: DBMS_XDB_VERSION.GETCONTENTSBLOBBYRESID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.GETCONTENTSBLOBBYRESID

This function obtain contents as a BLOB .

## Syntax

```sql
DBMS_XDB_VERSION.GETCONTENTSBLOBYRESID(
   resid      DBMS_XDB.resid_type)
 RETURN BLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| resid | DBMS_XDB.resid_type) | IN | The resource id. |

**Returns:** `BLOB`

## Usage Notes

Syntax DBMS_XDB_VERSION.GETCONTENTSBLOBYRESID( resid DBMS_XDB.resid_type) RETURN BLOB; Parameters Table 199-4 GETCONTENTSBLOBYRESID Function Parameters Parameter Description resid The resource id.