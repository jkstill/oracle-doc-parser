---
id: 19c__DBMS_COMPRESSION.GET_COMPRESSION_TYPE
name: DBMS_COMPRESSION.GET_COMPRESSION_TYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPRESSION
tags: [dbms_compression]
source_file: DBMS_COMPRESSION.html
---

# DBMS_COMPRESSION.GET_COMPRESSION_TYPE

This function returns the compression type for a specified row. If the row is chained, the function returns the compression type of the head piece only, and does not examine the intermediate or the tail piece since head pieces can be differently compressed.

## Syntax

```sql
DBMS_COMPRESSION.GET_COMPRESSION_TYPE (
   ownname      IN    VARCHAR2, 
   tabname      IN    VARCHAR2, 
   row_id       IN    ROWID,
   subobjname   IN    VARCHAR2 DEFAULT NULL))
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Schema name of the table |
| tabname | VARCHAR2 | IN | Name of table |
| rowid |  |  | Rowid of the row |
| subobjname | VARCHAR2 | IN | Name of the table partition or subpartition |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_COMPRESSION.GET_COMPRESSION_TYPE ( ownname IN VARCHAR2, tabname IN VARCHAR2, row_id IN ROWID, subobjname IN VARCHAR2 DEFAULT NULL)) RETURN NUMBER; Parameters Table 38-5 GET_COMPRESSION_TYPE Function Parameters Parameter Description ownname Schema name of the table tabname Name of table rowid Rowid of the row subobjname Name of the table partition or subpartition Return Values Flag to indicate the compression type (see Table 38-1 ).