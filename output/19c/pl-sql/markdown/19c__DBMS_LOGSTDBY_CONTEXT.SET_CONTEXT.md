---
id: 19c__DBMS_LOGSTDBY_CONTEXT.SET_CONTEXT
name: DBMS_LOGSTDBY_CONTEXT.SET_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY_CONTEXT
tags: [dbms_logstdby_context]
source_file: DBMS_LOGSTDBY_CONTEXT.html
---

# DBMS_LOGSTDBY_CONTEXT.SET_CONTEXT

This procedure sets the named parameter with the specified value.

## Syntax

```sql
DBMS_LOGSTDBY_CONTEXT.SET_CONTEXT (
   name            IN VARCHAR2
   value           IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the parameter to be set. |
| value | VARCHAR2) | IN | Value to be assigned to the parameter being set. |

## Usage Notes

Syntax DBMS_LOGSTDBY_CONTEXT.SET_CONTEXT ( name IN VARCHAR2 value IN VARCHAR2); Parameters Table 104-5 SET_CONTEXT Procedure Parameters Parameter Description name Name of the parameter to be set. value Value to be assigned to the parameter being set.