---
id: 19c__DBMS_MONITOR.DATABASE_TRACE_DISABLE
name: DBMS_MONITOR.DATABASE_TRACE_DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.DATABASE_TRACE_DISABLE

This procedure disables SQL trace for the whole database or a specific instance.

## Syntax

```sql
DBMS_MONITOR.DATABASE_TRACE_DISABLE(
   instance_name  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| instance_name | VARCHAR2 | IN | Disables tracing for the named instance |

## Usage Notes

Syntax DBMS_MONITOR.DATABASE_TRACE_DISABLE( instance_name IN VARCHAR2 DEFAULT NULL); Parameters Table 112-6 DATABASE_TRACE_DISABLE Procedure Parameters Parameter Description instance_name Disables tracing for the named instance