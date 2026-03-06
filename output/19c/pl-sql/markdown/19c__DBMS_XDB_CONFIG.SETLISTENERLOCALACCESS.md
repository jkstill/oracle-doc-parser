---
id: 19c__DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS
name: DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS

This procedure restricts all listener end points of the XML DB HTTP server to listen either only on the localhost interface (when l_access is set to TRUE ) or to listen on both localhost and non-localhost interfaces (when l_access is set to FALSE ).

## Syntax

```sql
DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS (
   l_access   BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| l_access . |  |  | TRUE or FALSE . |

## Usage Notes

Syntax DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS ( l_access BOOLEAN); Parameters Table 196-25 SETLISTENERLOCALACCESS Procedure Parameters Parameter Description l_access . TRUE or FALSE .