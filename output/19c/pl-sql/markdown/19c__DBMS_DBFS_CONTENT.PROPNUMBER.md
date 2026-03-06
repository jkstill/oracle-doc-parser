---
id: 19c__DBMS_DBFS_CONTENT.PROPNUMBER
name: DBMS_DBFS_CONTENT.PROPNUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.PROPNUMBER

This function is a constructor that takes a number and returns a PROPERTY_T .

## Syntax

```sql
DBMS_DBFS_CONTENT.PROPNUMBER (
   val      IN      NUMBER)
RETURN PROPERTY_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| val | NUMBER) | IN | Value |

**Returns:** `PROPERTY_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.PROPNUMBER ( val IN NUMBER) RETURN PROPERTY_T; Parameters Table 52-55 PROPNUMBER Function Parameters Parameter Description val Value Return Values PROPERTY_T Record Type