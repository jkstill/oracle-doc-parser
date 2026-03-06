---
id: 19c__DBMS_MGD_ID_UTL.REMOVE_CATEGORY
name: DBMS_MGD_ID_UTL.REMOVE_CATEGORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.REMOVE_CATEGORY

This procedure removes a category including all the related TDT XML.

## Syntax

```sql
DBMS_MGD_ID_UTL.REMOVE_CATEGORY (
   category_id  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_id | VARCHAR2) | IN | Category ID |
| category_name |  |  | Name of category |
| category_version |  |  | Category version |

## Usage Notes

This procedure is overloaded. The different functionality of each form of syntax is presented along with the definitions. Syntax Removes a category based on the specified category ID. DBMS_MGD_ID_UTL.REMOVE_CATEGORY ( category_id IN VARCHAR2); Removes a category based on the specified category name and category version. DBMS_MGD_ID_UTL.REMOVE_CATEGORY ( category_name IN VARCHAR2, category_version IN VARCHAR2); Parameters Table 109-14 REMOVE_CATEGORY Procedure Parameters Parameter Description category_id Category ID category_name Name of category category_version Category version Usage Notes If the value of category_version is NULL, all versions for the specified category will be removed. Examples See the ADD_SCHEME Procedure for an example of removing a category.