---
id: 19c__DBMS_XDB_CONFIG.DELETESERVLETMAPPING
name: DBMS_XDB_CONFIG.DELETESERVLETMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.DELETESERVLETMAPPING

This procedure deletes the servlet mapping for a specified servlet name from the XDB configuration.

## Syntax

```sql
DBMS_XDB_CONFIG.DELETESERVLETMAPPING(
     name      IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | Servlet name |

## Usage Notes

Syntax DBMS_XDB_CONFIG.DELETESERVLETMAPPING( name IN VARCHAR2); Parameters Table 196-15 DELETESERVLETMAPPING Procedure Parameters Parameter Description name Servlet name