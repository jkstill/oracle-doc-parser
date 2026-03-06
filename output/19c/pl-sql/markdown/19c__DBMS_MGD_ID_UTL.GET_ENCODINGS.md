---
id: 19c__DBMS_MGD_ID_UTL.GET_ENCODINGS
name: DBMS_MGD_ID_UTL.GET_ENCODINGS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.GET_ENCODINGS

This function returns a list of semicolon (;) separated encodings (formats) for the specified scheme.

## Syntax

```sql
DBMS_MGD_ID_UTL.GET_ENCODINGS (
   category_id IN VARCHAR2,
   scheme_name IN VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_id | VARCHAR2 | IN | Category ID |
| scheme_name | VARCHAR2) | IN | Name of scheme |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.GET_ENCODINGS ( category_id IN VARCHAR2, scheme_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 109-10 GET_ENCODINGS Function Parameters Parameter Description category_id Category ID scheme_name Name of scheme Usage Notes The return value contains the encodings separated by a semicolon (;) for the specified scheme. Examples See the GET_COMPONENTS Function for an example.