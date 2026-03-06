---
id: 19c__DBMS_XDB_CONFIG.DELETEMIMEMAPPING
name: DBMS_XDB_CONFIG.DELETEMIMEMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.DELETEMIMEMAPPING

This procedure deletes the mime mapping for a specified extension from the XDB configuration.

## Syntax

```sql
DBMS_XDB_CONFIG.DELETEMIMEMAPPING(
     extension    IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| extension | VARCHAR2) | IN | Extension for which a mime type is to be deleted |

## Usage Notes

Syntax DBMS_XDB_CONFIG.DELETEMIMEMAPPING( extension IN VARCHAR2); Parameters Table 196-12 DELETEMIMEMAPPING Procedure Parameters Parameter Description extension Extension for which a mime type is to be deleted