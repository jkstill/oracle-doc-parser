---
id: 19c__DBMS_MVIEW.ESTIMATE_MVIEW_SIZE
name: DBMS_MVIEW.ESTIMATE_MVIEW_SIZE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.ESTIMATE_MVIEW_SIZE

This procedure estimates the size of a materialized view that you might create, in bytes and number of rows.

## Syntax

```sql
DBMS_MVIEW.ESTIMATE_MVIEW_SIZE (
   stmt_id       IN  VARCHAR2,
   select_clause IN  VARCHAR2,
   num_rows      OUT NUMBER,
   num_bytes     OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stmt_id | VARCHAR2 | IN | Arbitrary string used to identify the statement in an EXPLAIN PLAN |
| select_clause | VARCHAR2 | IN | The SELECT statement to be analyzed |
| num_rows | NUMBER | OUT | Estimated cardinality |
| num_bytes | NUMBER) | OUT | Estimated number of bytes |

## Usage Notes

Syntax DBMS_MVIEW.ESTIMATE_MVIEW_SIZE ( stmt_id IN VARCHAR2, select_clause IN VARCHAR2, num_rows OUT NUMBER, num_bytes OUT NUMBER); Parameters Table 113-4 ESTIMATE_MVIEW_SIZE Procedure Parameters Parameter Description stmt_id Arbitrary string used to identify the statement in an EXPLAIN PLAN select_clause The SELECT statement to be analyzed num_rows Estimated cardinality num_bytes Estimated number of bytes