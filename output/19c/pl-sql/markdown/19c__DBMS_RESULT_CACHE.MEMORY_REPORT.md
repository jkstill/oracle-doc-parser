---
id: 19c__DBMS_RESULT_CACHE.MEMORY_REPORT
name: DBMS_RESULT_CACHE.MEMORY_REPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESULT_CACHE
tags: [dbms_result_cache]
source_file: DBMS_RESULT_CACHE.html
---

# DBMS_RESULT_CACHE.MEMORY_REPORT

This procedure produces the memory usage report for the Result Cache.

## Syntax

```sql
DBMS_RESULT_CACHE.MEMORY_REPORT (
   detailed   IN   BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| detailed | BOOLEAN | IN | TRUE => produces a more detailed report FALSE (default) => produces the standard report |

## Usage Notes

Syntax DBMS_RESULT_CACHE.MEMORY_REPORT ( detailed IN BOOLEAN DEFAULT FALSE); Parameters Table 144-10 MEMORY_REPORT Procedure Parameters Parameter Description detailed TRUE => produces a more detailed report FALSE (default) => produces the standard report Usage Notes Invoking this procedure from SQL*Plus requires that the serveroutput be turned on. Examples SET SERVEROUTPUT ON EXECUTE DBMS_RESULT_CACHE.MEMORY_REPORT;