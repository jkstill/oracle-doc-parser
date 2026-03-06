---
id: 19c__DBMS_SESSION.IS_SESSION_ALIVE
name: DBMS_SESSION.IS_SESSION_ALIVE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.IS_SESSION_ALIVE

This function determines if the specified session is active.

## Syntax

```sql
DBMS_SESSION.IS_SESSION_ALIVE (
   uniqueid VARCHAR2) 
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uniqueid | VARCHAR2) | IN | Unique ID of the session: This is the same one as returned by UNIQUE_SESSION_ID . |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_SESSION.IS_SESSION_ALIVE ( uniqueid VARCHAR2) RETURN BOOLEAN; Parameters Table 154-10 IS_SESSION_ALIVE Function Parameters Parameter Description uniqueid Unique ID of the session: This is the same one as returned by UNIQUE_SESSION_ID . Return Values Table 154-11 IS_SESSION_ALIVE Function Return Values Return Description is_session_alive TRUE or FALSE , depending on whether the session is active