---
id: 19c__DBMS_DBFS_CONTENT.PROPRAW
name: DBMS_DBFS_CONTENT.PROPRAW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.PROPRAW

This function is a constructor that takes a RAW and returns a PROPERTY_T .

## Syntax

```sql
DBMS_DBFS_CONTENT.PROPRAW (
   val      IN      RAW)
RETURN PROPERTY_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| val | RAW) | IN | Value |

**Returns:** `PROPERTY_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.PROPRAW ( val IN RAW) RETURN PROPERTY_T; Parameters Table 52-56 PROPRAW Function Parameters Parameter Description val Value Return Values PROPERTY_T Record Type