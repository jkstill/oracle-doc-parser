---
id: 19c__DBMS_MGD_ID_UTL.CREATE_CATEGORY
name: DBMS_MGD_ID_UTL.CREATE_CATEGORY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.CREATE_CATEGORY

This function creates a new category or a new version of a category.

## Syntax

```sql
DBMS_MGD_ID_UTL.CREATE_CATEGORY (
   category_name    IN  VARCHAR2,
   category_version IN  VARCHAR2,
   agency           IN  VARCHAR2,
   URI              IN  VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_name | VARCHAR2 | IN | Name of category |
| category_version | VARCHAR2 | IN | Category version |
| agency | VARCHAR2 | IN | Organization that owns the category. For example, EPCglobal owns the category EPC . |
| URI | VARCHAR2) | IN | URI that provides additional information about the category |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_MGD_ID_UTL.CREATE_CATEGORY ( category_name IN VARCHAR2, category_version IN VARCHAR2, agency IN VARCHAR2, URI IN VARCHAR2) RETURN VARCHAR2; Parameters Table 109-6 CREATE_CATEGORY Function Parameters Parameter Description category_name Name of category category_version Category version agency Organization that owns the category. For example, EPCglobal owns the category EPC . URI URI that provides additional information about the category Usage Notes The return value is the category ID. Examples See the ADD_SCHEME Procedure for an example of creating the MGD_SAMPLE_CATEGORY category.