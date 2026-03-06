---
id: 19c__DBMS_SESSION.SET_CONTEXT
name: DBMS_SESSION.SET_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SET_CONTEXT

This procedure sets the context, of which there are four types: session local, globally initialized, externally initialized, and globally accessed.

## Syntax

```sql
DBMS_SESSION.SET_CONTEXT (
   namespace VARCHAR2,
   attribute VARCHAR2,
   value     VARCHAR2,
   username  VARCHAR2,
   client_id VARCHAR2 );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| namespace | VARCHAR2 | IN | The namespace of the application context to be set, limited to 128 bytes. Exceeding the maximum permissible length will result in an error during the execution of the procedure. |
| attribute | VARCHAR2 | IN | The attribute of the application context to be set, limited to 128 bytes. Exceeding the maximum permissible length will result in an error during the execution of the procedure. |
| value | VARCHAR2 | IN | Value of the application context to be set, limited to 4 kilobytes. |
| username | VARCHAR2 | IN | Database username attribute of the application context, limited to 128 bytes. Exceeding the maximum permissible length will result in an error during the execution of the procedure. The default value is NULL . |
| client_id | VARCHAR2 | IN | Application-specific client_id attribute of the application context, limited to 64 bytes. The default value is NULL . |

## Usage Notes

Of the five parameters, only the first three are required; the final two parameters are optional, used only in globally accessed contexts. Further parameter information appears in the parameter table and the usage notes. Syntax DBMS_SESSION.SET_CONTEXT ( namespace VARCHAR2, attribute VARCHAR2, value VARCHAR2, username VARCHAR2, client_id VARCHAR2 ); Parameters Table 154-18 SET_CONTEXT Procedure Parameters Parameter Description namespace The namespace of the application context to be set, limited to 128 bytes. Exceeding the maximum permissible length will result in an error during the execution of the procedure. attribute The attribute of the application context to be set, limited to 128 bytes. Exceeding the maximum permissible length will result in an error during the execution of the procedure. value Value of the application context to be set, limited to 4 kilobytes. username Database username attribute of the application context, limited to 128 bytes. Exceeding the maximum permissible length will result in an error during the execution of the procedure. The default value is NULL . client_id Application-specific client_id attribute of the application context, limited to 64 bytes. The default value is NULL . Usage Notes The first three parameters are required for all types of context. The username parameter must be a valid SQL identifier. The client_id parameter must be a string of at most 64 bytes. It is case-sensitive and must match the argument provided for set_identifier . If the namespace parameter is a global context namespace, then the username parameter is matched against the current database user name in the session, and the client_id parameter is matched against the current client_id in the session. If these parameters are not set, NULL is assumed, enabling any user to see the context values. This procedure must be invoked directly or indirectly by the trusted package. The caller of SET_CONTEXT must be in the calling stack of a procedure that has been associated to the context namespace through a CREATE CONTEXT statement. The checking of the calling stack does not cross a DBMS boundary. No limit applies to the number of attributes that can be set in a namespace. An attribute retains its value during the user's session unless it is reset by the user. If the value of the parameter in the namespace has been set, SET_CONTEXT overwrites this value. Any changes in context value are reflected immediately and subsequent calls to access the value through SYS_CONTEXT return the most recent value. See Also: Oracle Database Security Guide for more information about "Setting the username and client ID" "Example: Creating a Global Application Context that Uses a Client Session ID" See Also: Oracle Database Security Guide for more information about "Setting the username and client ID" "Example: Creating a Global Application Context that Uses a Client Session ID"