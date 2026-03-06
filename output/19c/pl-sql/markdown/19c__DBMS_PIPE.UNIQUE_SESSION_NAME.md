---
id: 19c__DBMS_PIPE.UNIQUE_SESSION_NAME
name: DBMS_PIPE.UNIQUE_SESSION_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.UNIQUE_SESSION_NAME

This function receives a name that is unique among all of the sessions that are currently connected to a database.

## Syntax

```sql
DBMS_PIPE.UNIQUE_SESSION_NAME 
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Multiple calls to this function from the same session always return the same value. You might find it useful to use this function to supply the PIPENAME parameter for your SEND_MESSAGE and RECEIVE_MESSAGE calls. Syntax DBMS_PIPE.UNIQUE_SESSION_NAME RETURN VARCHAR2; Pragmas pragma restrict_references(unique_session_name,WNDS,RNDS,WNPS); Return Values This function returns a unique name. The returned name can be up to 30 bytes.