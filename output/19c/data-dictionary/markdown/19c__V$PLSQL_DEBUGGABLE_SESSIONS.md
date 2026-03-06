---
id: 19c__V$PLSQL_DEBUGGABLE_SESSIONS
name: V$PLSQL_DEBUGGABLE_SESSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-PLSQL_DEBUGGABLE_SESSIONS.html
---

# V$PLSQL_DEBUGGABLE_SESSIONS

V$PLSQL_DEBUGGABLE_SESSIONS shows the current sessions of all users that the current user has privileges to debug with a PL/SQL debugger.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| LOGON_TIME | DATE |  |
| USER# | NUMBER |  |
| USERNAME | VARCHAR2(128) |  |
| OSUSER | VARCHAR2(128) |  |
| PROCESS | VARCHAR2(24) |  |
| MACHINE | VARCHAR2(64) |  |
| PORT | NUMBER |  |
| TERMINAL | VARCHAR2(30) |  |
| PROGRAM | VARCHAR2(48) |  |
| TYPE | VARCHAR2(10) |  |
| SERVICE_NAME | VARCHAR2(64) |  |
| PLSQL_DEBUGGER_CONNECTED | VARCHAR2(5) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content