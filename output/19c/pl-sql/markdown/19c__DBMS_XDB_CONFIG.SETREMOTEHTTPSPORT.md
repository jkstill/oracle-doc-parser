---
id: 19c__DBMS_XDB_CONFIG.SETREMOTEHTTPSPORT
name: DBMS_XDB_CONFIG.SETREMOTEHTTPSPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.SETREMOTEHTTPSPORT

This procedure sets a remote HTTPS port to a new value.

## Syntax

```sql
DBMS_XDB_CONFIG.SETREMOTEHTTPSPORT (
   new_port  IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| new_port | NUMBER) | IN | Value to which the remote HTTPS port is set |

## Usage Notes

Syntax DBMS_XDB_CONFIG.SETREMOTEHTTPSPORT ( new_port IN NUMBER); Parameters Table 196-27 SETREMOTEHTTPSPORT Procedure Parameters Parameter Description new_port Value to which the remote HTTPS port is set