---
id: 19c__DBMS_DBFS_CONTENT.SETSTATS
name: DBMS_DBFS_CONTENT.SETSTATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETSTATS

This procedure enables and disables statistics collection.

## Syntax

```sql
DBMS_DBFS_CONTENT.SETSTATS (
   enable          IN    BOOLEAN,
   flush_time      IN    INTEGER,
   flush_count     IN    INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN | IN | If TRUE , enable statistics collection. If FALSE , disable statistics collection. |
| flush_time | INTEGER | IN | How often to flush the statistics to disk in centiseconds |
| flush_count | INTEGER) | IN | Number of operations to allow between statistics flushes |

## Usage Notes

The client can optionally control the flush settings by specifying non- NULL values for the time, count or both parameters. Syntax DBMS_DBFS_CONTENT.SETSTATS ( enable IN BOOLEAN, flush_time IN INTEGER, flush_count IN INTEGER); Parameters Table 52-72 SETSTATS Procedure Parameters Parameter Description enable If TRUE , enable statistics collection. If FALSE , disable statistics collection. flush_time How often to flush the statistics to disk in centiseconds flush_count Number of operations to allow between statistics flushes Usage Notes The SETSTATS Procedure buffers statistics in-memory for a maximum of flush_time centiseconds or a maximum of flush_count operations (whichever limit is reached first), or both, at which time the buffers are implicitly flushed to disk.