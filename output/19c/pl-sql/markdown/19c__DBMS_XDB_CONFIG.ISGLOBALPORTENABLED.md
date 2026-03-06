---
id: 19c__DBMS_XDB_CONFIG.ISGLOBALPORTENABLED
name: DBMS_XDB_CONFIG.ISGLOBALPORTENABLED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ISGLOBALPORTENABLED

This procedure returns the value of the GlobalPortEnabled setting.

## Syntax

```sql
DBMS_XDB_CONFIG.ISGLOBALPORTENABLED RETURN BOOLEAN;
```

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDB_CONFIG.ISGLOBALPORTENABLED RETURN BOOLEAN; Usage Notes This procedure returns TRUE if GlobalPortEnabled has been set to TRUE ; otherwise it returns FALSE . In a multitenant environment, you can execute this function in both the CDB root and PDBs.