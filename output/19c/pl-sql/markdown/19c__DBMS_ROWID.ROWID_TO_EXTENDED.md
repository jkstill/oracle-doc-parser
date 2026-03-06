---
id: 19c__DBMS_ROWID.ROWID_TO_EXTENDED
name: DBMS_ROWID.ROWID_TO_EXTENDED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_TO_EXTENDED

This function translates a restricted ROWID that addresses a row in a schema and table that you specify to the extended ROWID format.

## Syntax

```sql
DBMS_ROWID.ROWID_TO_EXTENDED (
   old_rowid       IN ROWID,
   schema_name     IN VARCHAR2,   
   object_name     IN VARCHAR2,
   conversion_type IN INTEGER)
  RETURN ROWID;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| old_rowid | ROWID | IN | ROWID to be converted |
| schema_name | VARCHAR2 | IN | Name of the schema which contains the table (optional) |
| object_name | VARCHAR2 | IN | Table name (optional). |
| conversion_type | INTEGER) | IN | The following constants are defined: ROWID_CONVERT_INTERNAL (:=0) ROWID_CONVERT_EXTERNAL (:=1) |

**Returns:** `ROWID`

## Usage Notes

Later, it may be removed from this package into a different place. Syntax DBMS_ROWID.ROWID_TO_EXTENDED ( old_rowid IN ROWID, schema_name IN VARCHAR2, object_name IN VARCHAR2, conversion_type IN INTEGER) RETURN ROWID; Pragmas pragma RESTRICT_REFERENCES(rowid_to_extended,WNDS,WNPS,RNPS); Parameters Table 148-13 ROWID_TO_EXTENDED Function Parameters Parameter Description old_rowid ROWID to be converted schema_name Name of the schema which contains the table (optional) object_name Table name (optional). conversion_type The following constants are defined: ROWID_CONVERT_INTERNAL (:=0) ROWID_CONVERT_EXTERNAL (:=1) Return Values ROWID_TO_EXTENDED returns the ROWID in the extended character format. If the input ROWID is NULL , then the function returns NULL . If a zero-valued ROWID is supplied (00000000.0000.0000), then a zero-valued restricted ROWID is returned.