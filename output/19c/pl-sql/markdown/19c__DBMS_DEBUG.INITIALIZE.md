---
id: 19c__DBMS_DEBUG.INITIALIZE
name: DBMS_DEBUG.INITIALIZE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.INITIALIZE

This function initializes the target session for debugging.

## Syntax

```sql
DBMS_DEBUG.INITIALIZE (
   debug_session_id  IN VARCHAR2       := NULL, 
   diagnostics       IN BINARY_INTEGER := 0)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| debug_session_id | VARCHAR2 | IN | Name of session ID. If NULL , then a unique ID is generated. |
| diagnostics | BINARY_INTEGER | IN | Indicates whether to dump diagnostic output to the tracefile: 0 = (default) no diagnostics 1 = print diagnostics |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_DEBUG.INITIALIZE ( debug_session_id IN VARCHAR2 := NULL, diagnostics IN BINARY_INTEGER := 0) RETURN VARCHAR2; Parameters Table 57-37 INITIALIZE Function Parameters Parameter Description debug_session_id Name of session ID. If NULL , then a unique ID is generated. diagnostics Indicates whether to dump diagnostic output to the tracefile: 0 = (default) no diagnostics 1 = print diagnostics Return Values The newly-registered debug session ID (debugID) Usage Notes You cannot use DBMS_DEBUG and the JDWP-based debugging interface simultaneously. This call will either fail with an ORA-30677 error if the session is currently being debugged with the JDWP-based debugging interface or, if the call succeeds, any further use of the JDWP-based interface to debug this session will be disallowed. Calls to DBMS_DEBUG will succeed only if either the caller or the specified debug role carries the DEBUG CONNECT SESSION privilege. Failing that, an ORA-1031 error will be raised. Other exceptions are also possible if a debug role is specified but the password does not match, or if the calling user has not been granted the role, or the role is application-enabled and this call does not originate from within the role-enabling package. The CREATE ANY PROCEDURE privilege does not affect the visibility of routines through the debugger. A privilege DEBUG for each object has been introduced with a corresponding DEBUG ANY PROCEDURE variant. These are required in order to see routines owned by users other than the session's login user. Authentication of the debug role and the check for DEBUG CONNECT SESSION privilege will be done in the context of the caller to this routine. If the caller is a definer's rights routine or has been called from one, only privileges granted to the defining user, the debug role, or PUBLIC will be used to check for DEBUG CONNECT SESSION . If this call is from within a definer's rights routine, the debug role, if specified, must be one that has been granted to that definer, but it need not also have been granted to the session login user or be enabled in the calling session at the time the call is made. The checks made by the debugger after this call is made looking for the DEBUG privilege on individual procedures will be done in the context of the session's login user, the roles that were enabled at session level at the moment this call was made (even if those roles were not available within a definer's rights environment of the call), and the debug role.