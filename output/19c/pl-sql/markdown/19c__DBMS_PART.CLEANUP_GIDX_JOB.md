---
id: 19c__DBMS_PART.CLEANUP_GIDX_JOB
name: DBMS_PART.CLEANUP_GIDX_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PART
tags: [dbms_part]
source_file: DBMS_PART.html
---

# DBMS_PART.CLEANUP_GIDX_JOB

This procedure will identify and cleanup these global indexes to ensure efficiency in terms of storage and performance.

## Syntax

```sql
DBMS_PART.CLEANUP_GIDX_JOB (
   parallel          IN   VARCHAR2 DEFAULT NULL,
   options           IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parallel | VARCHAR2 | IN | The parallel degree to use for the ALTER INDEX DDLs. |
| options | VARCHAR2 | IN | The following options are supported: CLEANUP_ORPHANS : implies that 'cleanup only' mechanism is used. COALESCE : implies that coalesce cleanup mechanism is used. |

## Usage Notes

Syntax DBMS_PART.CLEANUP_GIDX_JOB ( parallel IN VARCHAR2 DEFAULT NULL, options IN VARCHAR2 DEFAULT NULL); Parameters Table 122-3 CLEANUP_GIDX_JOB Function Parameters Parameter Description parallel The parallel degree to use for the ALTER INDEX DDLs. options The following options are supported: CLEANUP_ORPHANS : implies that 'cleanup only' mechanism is used. COALESCE : implies that coalesce cleanup mechanism is used.