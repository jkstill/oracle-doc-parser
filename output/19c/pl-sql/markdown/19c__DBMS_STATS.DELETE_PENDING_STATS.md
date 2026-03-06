---
id: 19c__DBMS_STATS.DELETE_PENDING_STATS
name: DBMS_STATS.DELETE_PENDING_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_PENDING_STATS

This procedure is used to delete the pending statistics that have been collected but have not been published.

## Syntax

```sql
DBMS_STATS.DELETE_PENDING_STATS (
    ownname    IN  VARCHAR2  DEFAULT USER,
    tabname    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name |
| tabname | VARCHAR2) | IN | Table name |

## Usage Notes

Syntax DBMS_STATS.DELETE_PENDING_STATS ( ownname IN VARCHAR2 DEFAULT USER, tabname IN VARCHAR2); Parameters Table 171-24 DELETE_PENDING_STATS Procedure Parameters Parameter Description ownname Owner name tabname Table name Security Model To run this procedure, you need to have the same privilege for gathering statistics on the tables that will be affected by this procedure. The default owner is the user who runs the procedure. Exceptions ORA-20000 : Insufficient privileges Usage Notes If the parameter tabname is NULL delete applies to all tables of the specified schema.