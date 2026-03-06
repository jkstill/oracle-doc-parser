---
id: 19c__DBMS_DBFS_CONTENT.SETTRACE
name: DBMS_DBFS_CONTENT.SETTRACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETTRACE

This procedure sets the DBMS_DBFS_CONTENT tracing severity to the given level, 0 being "off".

## Syntax

```sql
DBMS_DBFS_CONTENT.SETTRACE
     trclvl      IN         INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| trclvl | INTEGER) | IN | Level of the tracing, higher values implying more tracing |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.SETTRACE trclvl IN INTEGER); Parameters Table 52-73 SETTRACE Procedure Parameters Parameter Description trclvl Level of the tracing, higher values implying more tracing