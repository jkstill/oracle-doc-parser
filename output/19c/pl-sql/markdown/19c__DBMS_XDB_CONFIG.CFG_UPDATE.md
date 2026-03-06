---
id: 19c__DBMS_XDB_CONFIG.CFG_UPDATE
name: DBMS_XDB_CONFIG.CFG_UPDATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.CFG_UPDATE

This procedure updates the configuration information and commits the change.

## Syntax

```sql
DBMS_XDB_CONFIG.CFG_UPDATE(
   xdbconfig   IN  SYS.XMLTYPE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xdbconfig | SYS.XMLTYPE) | IN | The new configuration data |

## Usage Notes

Syntax DBMS_XDB_CONFIG.CFG_UPDATE( xdbconfig IN SYS.XMLTYPE); Parameters Table 196-10 CFG_UPDATE Procedure Parameters Parameter Description xdbconfig The new configuration data