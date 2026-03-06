---
id: 19c__DBMS_REFRESH.DESTROY
name: DBMS_REFRESH.DESTROY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REFRESH
tags: [dbms_refresh]
source_file: DBMS_REFRESH.html
---

# DBMS_REFRESH.DESTROY

This procedure removes all of the materialized views from a refresh group and delete the refresh group.

## Syntax

```sql
DBMS_REFRESH.DESTROY (
   name   IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | Name of the refresh group that you want to destroy. |

## Usage Notes

Syntax DBMS_REFRESH.DESTROY ( name IN VARCHAR2); Parameters Table 139-4 DESTROY Procedure Parameters Parameter Description name Name of the refresh group that you want to destroy.