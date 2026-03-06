---
id: 19c__DBMS_XDB_CONFIG.SETHTTPPORT
name: DBMS_XDB_CONFIG.SETHTTPPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.SETHTTPPORT

This procedure sets the HTTP port to a new value.

## Syntax

```sql
DBMS_XDB_CONFIG.SETHTTPPORT(
   new_port  IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| new_port | NUMBER) | IN | Value to which the HTTP port is set |

## Usage Notes

Syntax DBMS_XDB_CONFIG.SETHTTPPORT( new_port IN NUMBER); Parameters Table 196-21 SETHTTPPORT Procedure Parameters Parameter Description new_port Value to which the HTTP port is set