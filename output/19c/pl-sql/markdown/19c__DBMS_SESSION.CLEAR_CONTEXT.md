---
id: 19c__DBMS_SESSION.CLEAR_CONTEXT
name: DBMS_SESSION.CLEAR_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.CLEAR_CONTEXT

This procedure clears application context in the specified namespace.

## Syntax

```sql
DBMS_SESSION.CLEAR_CONTEXT
   namespace         VARCHAR2,
   client_identifier VARCHAR2
   attribute         VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| namespace | VARCHAR2 | IN | Namespace in which the application context is to be cleared. Required. For a session-local context, namespace must be specified. If namespace is defined as Session Local Context , then client_identifier is optional since it is only associated with a globally accessed context. For a globally accessed context, namespace must be specified. NULL is a valid value for client_identifier because a session with no identifier set can see a context that looks like the ( namespace, attribute, value, username, null ) set using SET_CONTEXT . |
| client_identifier | VARCHAR2 | IN | Applies to a global context and is optional for other types of contexts; 64-byte maximum |
| attribute | VARCHAR2) | IN | Specific attribute in the namespace to be cleared. Optional. the default is NULL . If you specify attribute as NULL , then ( namespace, attribute, value ) for that namespace are cleared from the session. If attribute is not specified, then all context information that has the namespace and client_identifier arguments is cleared. |

## Usage Notes

Syntax DBMS_SESSION.CLEAR_CONTEXT namespace VARCHAR2, client_identifier VARCHAR2 attribute VARCHAR2); Parameters Table 154-4 CLEAR_CONTEXT Procedure Parameters Parameter Description namespace Namespace in which the application context is to be cleared. Required. For a session-local context, namespace must be specified. If namespace is defined as Session Local Context , then client_identifier is optional since it is only associated with a globally accessed context. For a globally accessed context, namespace must be specified. NULL is a valid value for client_identifier because a session with no identifier set can see a context that looks like the ( namespace, attribute, value, username, null ) set using SET_CONTEXT . client_identifier Applies to a global context and is optional for other types of contexts; 64-byte maximum attribute Specific attribute in the namespace to be cleared. Optional. the default is NULL . If you specify attribute as NULL , then ( namespace, attribute, value ) for that namespace are cleared from the session. If attribute is not specified, then all context information that has the namespace and client_identifier arguments is cleared. Usage Notes This procedure must be invoked directly or indirectly by the trusted package. Any changes in context value are reflected immediately and subsequent calls to access the value through SYS_CONTEXT return the most recent value.