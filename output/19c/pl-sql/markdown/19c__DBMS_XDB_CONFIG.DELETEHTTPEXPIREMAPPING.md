---
id: 19c__DBMS_XDB_CONFIG.DELETEHTTPEXPIREMAPPING
name: DBMS_XDB_CONFIG.DELETEHTTPEXPIREMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.DELETEHTTPEXPIREMAPPING

This procedure deletes from XDB$CONFIG all mappings of the URL pattern to an expiration date.

## Syntax

```sql
DBMS_XDB_REPOS.DELETEHTTPEXPIREMAPPING(
     pattern  IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pattern | VARCHAR2) | IN | URL pattern (only * accepted as wildcards) |

## Usage Notes

Syntax DBMS_XDB_REPOS.DELETEHTTPEXPIREMAPPING( pattern IN VARCHAR2); Parameters Table 196-11 DELETEHTTPEXPIREMAPPING Procedure Parameters Parameter Description pattern URL pattern (only * accepted as wildcards)