---
id: 19c__DBMS_DBFS_CONTENT.LISTALLPROPERTIES
name: DBMS_DBFS_CONTENT.LISTALLPROPERTIES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.LISTALLPROPERTIES

This function returns a table of all properties for all path items in all mounts.

## Syntax

```sql
DBMS_DBFS_CONTENT.LISTALLPROPERTIES 
  RETURN  PROP_ITEMS_T PIPELINED;
```

**Returns:** `PROP_ITEMS_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.LISTALLPROPERTIES RETURN PROP_ITEMS_T PIPELINED; Return Values PROP_ITEMS_T Table Type