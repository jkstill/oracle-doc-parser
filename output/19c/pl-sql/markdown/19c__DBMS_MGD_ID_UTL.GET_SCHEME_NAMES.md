---
id: 19c__DBMS_MGD_ID_UTL.GET_SCHEME_NAMES
name: DBMS_MGD_ID_UTL.GET_SCHEME_NAMES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.GET_SCHEME_NAMES

This function returns a list of semicolon (;) separated scheme names for the specified category.

## Syntax

```sql
DBMS_MGD_ID_UTL.GET_SCHEME_NAMES (
   category_id IN VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_id | VARCHAR2) | IN | Category ID |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.GET_SCHEME_NAMES ( category_id IN VARCHAR2) RETURN VARCHAR2; Parameters Table 109-11 GET_SCHEME_NAMES Function Parameters Parameter Description category_id Category ID Usage Notes The return value contains the scheme names for the specified category ID. Examples See the GET_COMPONENTS Function for an example.