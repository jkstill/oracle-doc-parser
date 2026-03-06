---
id: 19c__DBMS_REFRESH.REFRESH
name: DBMS_REFRESH.REFRESH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REFRESH
tags: [dbms_refresh]
source_file: DBMS_REFRESH.html
---

# DBMS_REFRESH.REFRESH

This procedure manually refreshes a refresh group.

## Syntax

```sql
DBMS_REFRESH.REFRESH (
   name   IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | Name of the refresh group that you want to refresh manually. |

## Usage Notes

Syntax DBMS_REFRESH.REFRESH ( name IN VARCHAR2); Parameters Table 139-6 REFRESH Procedure Parameters Parameter Description name Name of the refresh group that you want to refresh manually.