---
id: 19c__DBMS_LOGSTDBY_CONTEXT.GET_CONTEXT
name: DBMS_LOGSTDBY_CONTEXT.GET_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY_CONTEXT
tags: [dbms_logstdby_context]
source_file: DBMS_LOGSTDBY_CONTEXT.html
---

# DBMS_LOGSTDBY_CONTEXT.GET_CONTEXT

This procedure retrieves the value for the specified parameter.

## Syntax

```sql
DBMS_LOGSTDBY_CONTEXT.GET_CONTEXT (
   name            IN VARCHAR2,
   value           OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the parameter. |
| value | VARCHAR2) | OUT | The value retrieved for the parameter. |

## Usage Notes

Syntax DBMS_LOGSTDBY_CONTEXT.GET_CONTEXT ( name IN VARCHAR2, value OUT VARCHAR2); Parameters Table 104-4 GET_CONTEXT Procedure Parameters Parameter Description name Name of the parameter. value The value retrieved for the parameter.