---
id: 19c__DBMS_ROWID.ROWID_TO_RESTRICTED
name: DBMS_ROWID.ROWID_TO_RESTRICTED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_TO_RESTRICTED

This function converts an extended ROWID into restricted ROWID format.

## Syntax

```sql
DBMS_ROWID.ROWID_TO_RESTRICTED (
   old_rowid       IN ROWID,
   conversion_type IN INTEGER)
  RETURN ROWID;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| old_rowid | ROWID | IN | ROWID to be converted |
| conversion_type | INTEGER) | IN | The following constants are defined: ROWID_CONVERT_INTERNAL (:=0) ROWID_CONVERT_EXTERNAL (:=1) |

**Returns:** `ROWID`

## Usage Notes

Syntax DBMS_ROWID.ROWID_TO_RESTRICTED ( old_rowid IN ROWID, conversion_type IN INTEGER) RETURN ROWID; Pragmas pragma RESTRICT_REFERENCES(rowid_to_restricted,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-14 ROWID_TO_RESTRICTED Function Parameters Parameter Description old_rowid ROWID to be converted conversion_type The following constants are defined: ROWID_CONVERT_INTERNAL (:=0) ROWID_CONVERT_EXTERNAL (:=1)