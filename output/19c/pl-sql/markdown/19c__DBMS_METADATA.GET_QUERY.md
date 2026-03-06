---
id: 19c__DBMS_METADATA.GET_QUERY
name: DBMS_METADATA.GET_QUERY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.GET_QUERY

This function returns the text of the queries that are used by FETCH_xxx . This function assists in debugging.

## Syntax

```sql
DBMS_METADATA.GET_QUERY (
   handle  IN NUMBER)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER) | IN | The handle returned from OPEN . It cannot be the handle for a heterogeneous object type. |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database See Also: For more information about related subprograms: Subprograms for Retrieving Multiple Objects From the Database Syntax DBMS_METADATA.GET_QUERY ( handle IN NUMBER) RETURN VARCHAR2; Parameters Table 107-10 GET_QUERY Function Parameters Parameter Description handle The handle returned from OPEN . It cannot be the handle for a heterogeneous object type. Return Values The text of the queries that will be used by FETCH_xxx.