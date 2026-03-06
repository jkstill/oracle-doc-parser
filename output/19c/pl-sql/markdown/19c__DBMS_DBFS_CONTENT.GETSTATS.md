---
id: 19c__DBMS_DBFS_CONTENT.GETSTATS
name: DBMS_DBFS_CONTENT.GETSTATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETSTATS

This procedure returns information about DBMS_DBFS_CONTENT statistics collection.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETSTATS (
   enabled         OUT    BOOLEAN,
   flush_time      OUT    INTEGER,
   flush_count     OUT    INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enabled | BOOLEAN | OUT | Whether statistics collection is enabled |
| flush_time | INTEGER | OUT | How often to flush the statistics to disk in centiseconds |
| flush_count | INTEGER) | OUT | Number of operations to allow between statistics flushes |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETSTATS ( enabled OUT BOOLEAN, flush_time OUT INTEGER, flush_count OUT INTEGER); Parameters Table 52-46 GETSTATS Procedure Parameters Parameter Description enabled Whether statistics collection is enabled flush_time How often to flush the statistics to disk in centiseconds flush_count Number of operations to allow between statistics flushes