---
id: 19c__DBMS_UTILITY.IS_CLUSTER_DATABASE
name: DBMS_UTILITY.IS_CLUSTER_DATABASE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.IS_CLUSTER_DATABASE

This function finds out if this database is running in cluster database mode.

## Syntax

```sql
DBMS_UTILITY.IS_CLUSTER_DATABASE 
  RETURN BOOLEAN;
```

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_UTILITY.IS_CLUSTER_DATABASE RETURN BOOLEAN; Return Values This function returns TRUE if this instance was started in cluster database mode; FALSE otherwise.