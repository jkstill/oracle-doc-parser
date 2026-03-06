---
id: 19c__DBMS_MGD_ID_UTL.REMOVE_SCHEME
name: DBMS_MGD_ID_UTL.REMOVE_SCHEME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGD_ID_UTL
tags: [dbms_mgd_id_utl]
source_file: DBMS_MGD_ID_UTL.html
---

# DBMS_MGD_ID_UTL.REMOVE_SCHEME

This procedure removes a tag data translation scheme from a category.

## Syntax

```sql
DBMS_MGD_ID_UTL.REMOVE_SCHEME (
   category_id  IN  VARCHAR2,
   scheme_name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_id | VARCHAR2 | IN | Category ID |
| scheme_name | VARCHAR2) | IN | Name of scheme |

## Usage Notes

Syntax DBMS_MGD_ID_UTL.REMOVE_SCHEME ( category_id IN VARCHAR2, scheme_name IN VARCHAR2); Parameters Table 109-15 REMOVE_SCHEME Procedure Parameters Parameter Description category_id Category ID scheme_name Name of scheme Examples See the ADD_SCHEME Procedure for an example of removing a scheme.