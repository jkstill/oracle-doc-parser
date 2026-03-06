---
id: 19c__DBMS_STATS.PUBLISH_PENDING_STATS
name: DBMS_STATS.PUBLISH_PENDING_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.PUBLISH_PENDING_STATS

This procedure is used to publish the statistics gathered and stored as pending.

## Syntax

```sql
DBMS_STATS.PUBLISH_PENDING_STATS (
    ownname         IN  VARCHAR2 DEFAULT USER,
    tabname         IN  VARCHAR2,
    no_invalidate       BOOLEAN DEFAULT 
       TO_NO_INVALIDATE_TYPE(GET_PARAM('NO_INVALIDATE')),
    force           IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name |
| tabname | VARCHAR2 | IN | Table name |
| no_invalidate | BOOLEAN | IN | Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |
| force | BOOLEAN | IN | If TRUE , will override the lock |

## Usage Notes

Syntax DBMS_STATS.PUBLISH_PENDING_STATS ( ownname IN VARCHAR2 DEFAULT USER, tabname IN VARCHAR2, no_invalidate BOOLEAN DEFAULT TO_NO_INVALIDATE_TYPE(GET_PARAM('NO_INVALIDATE')), force IN BOOLEAN DEFAULT FALSE); Parameters Table 171-95 PUBLISH_PENDING_STATS Procedure Parameters Parameter Description ownname Owner name tabname Table name no_invalidate Controls the invalidation of dependent cursors when statistics are gathered. The parameter takes the following values: TRUE : Dependent cursors are not invalidated. FALSE : Dependent cursors are marked for immediate invalidation. AUTO : This is the default value. Rolling invalidation is used to invalidate all dependent cursors over a period of time. The performance impact on the database is reduced especially in cases where a large number of cursors are invalidated. You can change the default using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . force If TRUE , will override the lock Security Model To run this procedure, you must have the same privilege for gathering statistics on the tables that will be touched by this procedure. Exceptions ORA-20000 : Insufficient privileges Usage Notes If the parameter tabname is NULL then publish applies to all tables of the specified schema. The default owner/schema is the user who runs the procedure.