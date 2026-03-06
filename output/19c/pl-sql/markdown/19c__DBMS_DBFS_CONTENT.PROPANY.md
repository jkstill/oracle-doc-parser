---
id: 19c__DBMS_DBFS_CONTENT.PROPANY
name: DBMS_DBFS_CONTENT.PROPANY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.PROPANY

This function provides constructors that take one of a variety of types and return a PROPERTY_T.

## Syntax

```sql
DBMS_DBFS_CONTENT.PROPANY (
   val      IN      NUMBER)
RETURN PROPERTY_T;

DBMS_DBFS_CONTENT.PROPANY (
   val      IN      VARCHAR2)
RETURN PROPERTY_T;

DBMS_DBFS_CONTENT.PROPANY (
   val      IN      TIMESTAMP)
RETURN PROPERTY_T;

DBMS_DBFS_CONTENT.PROPANY (
   val      IN      RAW)
RETURN PROPERTY_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| val | NUMBER) | IN | Value |

**Returns:** `PROPERTY_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.PROPANY ( val IN NUMBER) RETURN PROPERTY_T; DBMS_DBFS_CONTENT.PROPANY ( val IN VARCHAR2) RETURN PROPERTY_T; DBMS_DBFS_CONTENT.PROPANY ( val IN TIMESTAMP) RETURN PROPERTY_T; DBMS_DBFS_CONTENT.PROPANY ( val IN RAW) RETURN PROPERTY_T; Parameters Table 52-52 PROPANY Function Parameters Parameter Description val Value Return Values PROPERTY_T Record Type