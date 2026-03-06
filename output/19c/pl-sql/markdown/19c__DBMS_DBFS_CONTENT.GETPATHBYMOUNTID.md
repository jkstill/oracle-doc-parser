---
id: 19c__DBMS_DBFS_CONTENT.GETPATHBYMOUNTID
name: DBMS_DBFS_CONTENT.GETPATHBYMOUNTID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETPATHBYMOUNTID

If the underlying GUID is found in the underlying store, this function returns the full absolute path name.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETPATHBYMOUNTID (
   store_mount         IN      VARCHAR2,
   guid                IN      INTEGER)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_mount | VARCHAR2 | IN | Mount point in which the path item with guid resides |
| guid | INTEGER) | IN | Unique ID for the path item |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETPATHBYMOUNTID ( store_mount IN VARCHAR2, guid IN INTEGER) RETURN VARCHAR2; Parameters Table 52-40 GETPATHBYMOUNTID Function Parameters Parameter Description store_mount Mount point in which the path item with guid resides guid Unique ID for the path item Usage Notes If the GUID is unknown, a NULL value is returned. Clients are expected to handle this as appropriate. Return Values Path of the path item represented by GUID in store_mount