---
id: 19c__DBMS_DBFS_CONTENT.DECODEFEATURES
name: DBMS_DBFS_CONTENT.DECODEFEATURES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.DECODEFEATURES

Given a feature bit set integer value, this function returns a FEATURES_T table of the feature bits as FEATURE_T records.

## Syntax

```sql
DBMS_DBFS_CONTENT.DECODEFEATURES (
   featureSet          IN      INTEGER)
  RETURN FEATURES_T DETERMINISTIC PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| featureSet | INTEGER) | IN | Feature set |

**Returns:** `FEATURES_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.DECODEFEATURES ( featureSet IN INTEGER) RETURN FEATURES_T DETERMINISTIC PIPELINED; Parameters Table 52-26 DECODEFEATURES Function Parameters Parameter Description featureSet Feature set Return Values FEATURES_T Table Type