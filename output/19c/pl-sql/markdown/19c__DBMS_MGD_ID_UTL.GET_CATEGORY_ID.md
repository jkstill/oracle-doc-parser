---
id: 19c__DBMS_MGD_ID_UTL.GET_CATEGORY_ID
name: DBMS_MGD_ID_UTL.GET_CATEGORY_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.GET_CATEGORY_ID

This function returns the category ID for a given category name and category version.

## Syntax

```sql
DBMS_MGD_ID_UTL.GET_CATEGORY_ID (
   category name     IN  VARCHAR2,
   category_version  IN  VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_name |  |  | Name of category |
| category_version | VARCHAR2) | IN | Category version |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.GET_CATEGORY_ID ( category name IN VARCHAR2, category_version IN VARCHAR2) RETURN VARCHAR2; Parameters Table 109-8 GET_CATEGORY_ID Function Parameters Parameter Description category_name Name of category category_version Category version Usage Notes If the value of category_version is NULL, then the ID of the latest version of the specified category is returned. The return value is the category ID for the specified category name. Examples The following example returns a category ID given a category name and its version: -- Contents of get_category1.sql file SELECT DBMS_MGD_ID_UTL.get_category_id('EPC', NULL) FROM DUAL; SQL> @get_category1.sql . . . DBMS_MGD_ID_UTL.GET_CATEGORY_ID('EPC',NULL)--------------------------------------------------------------------------------1 . . .