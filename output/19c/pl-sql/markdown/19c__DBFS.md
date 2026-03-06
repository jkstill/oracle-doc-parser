---
id: 19c__DBFS
name: DBFS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBFS
tags: [dbfs]
source_file: DBFS-Content-Interface-Types.html
---

# DBFS

Types that support the DBMS_DBFS_CONTENT interface include both Object and Table types.

## Syntax

```sql
CREATE OR REPLACE TYPE dbms_dbfs_content_context_t
    AUTHID DEFINER
AS OBJECT (
    principal     VARCHAR2(32),
    acl           VARCHAR2(1024),
    owner         VARCHAR2(32),
    asof          TIMESTAMP,
    read_only     INTEGER);
```

## Usage Notes

Object Types DBMS_DBFS_CONTENT_CONTEXT_T Object Type DBMS_DBFS_CONTENT_LIST_ITEM_T Object Type DBMS_DBFS_CONTENT_PROPERTY_T Object Type Table Types DBMS_DBFS_CONTENT_LIST_ITEMS_T Table Type DBMS_DBFS_CONTENT_PROPERTIES_T Table Type DBMS_DBFS_CONTENT_RAW_T Table Type Syntax CREATE OR REPLACE TYPE dbms_dbfs_content_context_t AUTHID DEFINER AS OBJECT ( principal VARCHAR2(32), acl VARCHAR2(1024), owner VARCHAR2(32), asof TIMESTAMP, read_only INTEGER); Fields Table 284-1 DBMS_DBFS_CONTENT_CONTEXT_T Fields Field Description principal File system user acl Access control list owner Path item owner asof Timestamp read_only Nonzero if the path item is read-only Syntax CREATE OR REPLACE TYPE dbms_dbfs_content_list_item_t AUTHID DEFINER AS OBJECT ( path VARCHAR2(1024), item_name VARCHAR2(256), item_type INTEGER);