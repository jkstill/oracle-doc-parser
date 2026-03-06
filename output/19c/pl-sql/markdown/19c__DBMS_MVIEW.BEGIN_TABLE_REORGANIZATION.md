---
id: 19c__DBMS_MVIEW.BEGIN_TABLE_REORGANIZATION
name: DBMS_MVIEW.BEGIN_TABLE_REORGANIZATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.BEGIN_TABLE_REORGANIZATION

This procedure performs a process to preserve materialized view data needed for refresh. It must be called before a master table is reorganized.

## Syntax

```sql
DBMS_MVIEW.BEGIN_TABLE_REORGANIZATION (
   tabowner    IN   VARCHAR2,
   tabname     IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tabowner | VARCHAR2 | IN | Owner of the table being reorganized |
| tabname | VARCHAR2) | IN | Name of the table being reorganized |

## Usage Notes

Syntax DBMS_MVIEW.BEGIN_TABLE_REORGANIZATION ( tabowner IN VARCHAR2, tabname IN VARCHAR2); Parameters Table 113-2 BEGIN_TABLE_REORGANIZATION Procedure Parameters Parameter Description tabowner Owner of the table being reorganized tabname Name of the table being reorganized