---
id: 19c__DBMS_DBFS_CONTENT.FEATURENAME
name: DBMS_DBFS_CONTENT.FEATURENAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.FEATURENAME

Given a feature bit, this function returns a VARCHAR2 of that feature's name.

## Syntax

```sql
DBMS_DBFS_CONTENT.FEATURENAME (
   featureBit          IN      INTEGER)
  RETURN VARCHAR2 DETERMINISTIC;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| featureBit | INTEGER) | IN | Bit representation of the feature (see Table 52-5 ) |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.FEATURENAME ( featureBit IN INTEGER) RETURN VARCHAR2 DETERMINISTIC; Parameters Table 52-30 FEATURENAME Function Parameters Parameter Description featureBit Bit representation of the feature (see Table 52-5 ) Return Values Name of the feature