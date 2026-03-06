---
id: 19c__DBMS_XDB_CONFIG.DELETEXMLEXTENSION
name: DBMS_XDB_CONFIG.DELETEXMLEXTENSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.DELETEXMLEXTENSION

This procedure deletes the specified XML extension from the XDB configuration.

## Syntax

```sql
DBMS_XDB_CONFIG.DELETEXMLEXTENSION(
     extension    IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| extension | VARCHAR2) | IN | XML extension to be deleted |

## Usage Notes

Syntax DBMS_XDB_CONFIG.DELETEXMLEXTENSION( extension IN VARCHAR2); Parameters Table 196-17 DELETEXMLEXTENSION Procedure Parameters Parameter Description extension XML extension to be deleted