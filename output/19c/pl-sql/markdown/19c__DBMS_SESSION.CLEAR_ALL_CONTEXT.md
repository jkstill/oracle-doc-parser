---
id: 19c__DBMS_SESSION.CLEAR_ALL_CONTEXT
name: DBMS_SESSION.CLEAR_ALL_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.CLEAR_ALL_CONTEXT

This procedure clears application context information in the specified namespace.

## Syntax

```sql
DBMS_SESSION.CLEAR_ALL_CONTEXT
   namespace         VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| namespace | VARCHAR2) | IN | The namespace where the application context information is to be cleared. Required. |

## Usage Notes

Syntax DBMS_SESSION.CLEAR_ALL_CONTEXT namespace VARCHAR2); Parameters Table 154-3 CLEAR_ALL_CONTEXT Procedure Parameters Parameter Description namespace The namespace where the application context information is to be cleared. Required. Usage Notes This procedure must be invoked directly or indirectly by the trusted package. Any changes in context value are reflected immediately and subsequent calls to access the value through SYS_CONTEXT return the most recent value.