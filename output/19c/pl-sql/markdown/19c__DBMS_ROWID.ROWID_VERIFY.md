---
id: 19c__DBMS_ROWID.ROWID_VERIFY
name: DBMS_ROWID.ROWID_VERIFY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_VERIFY

This function verifies the ROWID .

## Syntax

```sql
DBMS_ROWID.ROWID_VERIFY (
   rowid_in        IN ROWID,
   schema_name     IN VARCHAR2,
   object_name     IN VARCHAR2,
   conversion_type IN INTEGER
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rowid_in | ROWID | IN | ROWID to be verified |
| schema_name | VARCHAR2 | IN | Name of the schema which contains the table |
| object_name | VARCHAR2 | IN | Table name |
| conversion_type | INTEGER | IN | The following constants are defined: ROWID_CONVERT_INTERNAL (:=0) ROWID_CONVERT_EXTERNAL (:=1) |

**Returns:** `NUMBER`

## Usage Notes

It returns 0 if the input restricted ROWID can be converted to extended format, given the input schema name and table name, and it returns 1 if the conversion is not possible. Note: You can use this function in a WHERE clause of a SQL statement, as shown in the example. Note: You can use this function in a WHERE clause of a SQL statement, as shown in the example. Syntax DBMS_ROWID.ROWID_VERIFY ( rowid_in IN ROWID, schema_name IN VARCHAR2, object_name IN VARCHAR2, conversion_type IN INTEGER RETURN NUMBER; Pragmas pragma RESTRICT_REFERENCES(rowid_verify,WNDS,WNPS,RNPS); Parameters Table 148-16 ROWID_VERIFY Function Parameters Parameter Description rowid_in ROWID to be verified schema_name Name of the schema which contains the table object_name Table name conversion_type The following constants are defined: ROWID_CONVERT_INTERNAL (:=0) ROWID_CONVERT_EXTERNAL (:=1)