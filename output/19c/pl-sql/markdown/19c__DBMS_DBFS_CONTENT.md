---
id: 19c__DBMS_DBFS_CONTENT
name: DBMS_DBFS_CONTENT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT

The DBMS_DBFS_CONTENT package defines RECORD types and TABLE types.

## Syntax

```sql
TYPE feature_t IS RECORD (
   feature_name    VARCHAR2(32),
   feature_mask    INTEGER,
   feature_state   VARCHAR2(3));
```

## Usage Notes

RECORD Types FEATURE_T Record Type MOUNT_T Record Type PATH_ITEM_T Record Type PROP_ITEM_T Record Type PROPERTY_T Record Type STORE_T Record Type TABLE Types FEATURES_T Table Type MOUNTS_T Table Type PATH_ITEMS_T Table Type PROP_ITEMS_T Table Type PROPERTIES_T Table Type STORES_T Table Type Usage Notes There is an approximate correspondence between DBMS_DBFS_CONTENT_PROPERTY_T and PROPERTY_T — the former is a SQL object type that describes the full property tuple, while the latter is a PL/SQL record type that describes only the property value component. Likewise, there is an approximate correspondence between DBMS_DBFS_CONTENT_PROPERTIES_T and PROPERTIES_T — the former is a SQL nested table type, while the latter is a PL/SQL hash table type. Dynamic SQL calling conventions force the use of SQL types, but PL/SQL code may be implemented more conveniently in terms of the hash-table types. The DBMS_DBFS_CONTENT interface provides convenient utility functions to convert between DBMS_DBFS_CONTENT_PROPERTIES_T and PROPERTIES_T (see propertiesT2H and propertiesH2T). Clients can query the DBMS_DBFS_CONTENT interface for the list of available stores, determine which store is to handle access to a given path name, and determine the feature set for the store. Syntax TYPE feature_t IS RECORD ( feature_name VARCHAR2(32), feature_mask INTEGER, feature_state VARCHAR2(3)); Fields Table 52-13 MOUNT_T Fields Field Description feature_name Name of feature feature_mask Value used to mask off all other bits other than this feature in the feature value feature_state ' YES ' or ' NO ' depending on whether the feature is supported on this store