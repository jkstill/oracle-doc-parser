---
id: 19c__DBMS_DST.END_UPGRADE
name: DBMS_DST.END_UPGRADE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.END_UPGRADE

This procedure ends an upgrade window. An upgraded window is ended if all the affected user tables have been upgraded. Otherwise, the OUT parameter num_of_failures indicates how many tables have not been converted.

## Syntax

```sql
DBMS_DST.END_UPGRADE (
  num_of_failures    OUT  BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| num_of_failures | BINARY_INTEGER) | OUT | Number of tables that fail to complete |

## Usage Notes

Syntax DBMS_DST.END_UPGRADE ( num_of_failures OUT BINARY_INTEGER); Parameters Table 65-8 END_UPGRADE Procedure Parameters Parameter Description num_of_failures Number of tables that fail to complete