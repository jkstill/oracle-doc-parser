---
id: 19c__DBMS_SESSION.UNIQUE_SESSION_ID
name: DBMS_SESSION.UNIQUE_SESSION_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.UNIQUE_SESSION_ID

This function returns an identifier that is unique for all sessions currently connected to this database. Multiple calls to this function during the same session always return the same result.

## Syntax

```sql
DBMS_SESSION.UNIQUE_SESSION_ID 
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SESSION.UNIQUE_SESSION_ID RETURN VARCHAR2; Pragmas pragma restrict_references(unique_session_id,WNDS,RNDS,WNPS); Return Values Table 154-27 UNIQUE_SESSION_ID Function Return Values Return Description unique_session_id Returns up to 24 bytes