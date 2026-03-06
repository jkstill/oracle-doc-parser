---
id: 19c__DBMS_SESSION.SET_IDENTIFIER
name: DBMS_SESSION.SET_IDENTIFIER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SET_IDENTIFIER

This procedure sets the client ID in the session.

## Syntax

```sql
DBMS_SESSION.SET_IDENTIFIER (
   client_id VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_id | VARCHAR2) | IN | Case-sensitive application-specific identifier of the current database session. The maximum number of bytes for this parameter is 64 bytes. If the input exceeds 64 bytes, the additional bytes are truncated. |

## Usage Notes

Syntax DBMS_SESSION.SET_IDENTIFIER ( client_id VARCHAR2); Parameters Table 154-20 SET_IDENTIFIER Procedure Parameters Parameter Description client_id Case-sensitive application-specific identifier of the current database session. The maximum number of bytes for this parameter is 64 bytes. If the input exceeds 64 bytes, the additional bytes are truncated. Usage Notes SET_IDENTIFIER sets the session's client id to the given value. This value can be used to identify sessions in v$session by means of v$session.client_identifier . It can also be used to identify sessions by means of sys_context('USERENV','CLIENT_IDENTIFIER'). This procedure is executable by PUBLIC .