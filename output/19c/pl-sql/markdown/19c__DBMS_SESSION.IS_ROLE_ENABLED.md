---
id: 19c__DBMS_SESSION.IS_ROLE_ENABLED
name: DBMS_SESSION.IS_ROLE_ENABLED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.IS_ROLE_ENABLED

This function determines if the named role is enabled for this session.

## Syntax

```sql
DBMS_SESSION.IS_ROLE_ENABLED (
   rolename    VARCHAR2) 
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rolename | VARCHAR2) | IN | Name of the role.\ |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax Note: This function is deprecated starting in Oracle Database 19c. Use DBMS_SESSION.CURRENT_IS_ROLE_ENABLED or DBMS_SESSION.SESSION_IS_ROLE_ENABLED instead. DBMS_SESSION.IS_ROLE_ENABLED ( rolename VARCHAR2) RETURN BOOLEAN; Note: This function is deprecated starting in Oracle Database 19c. Use DBMS_SESSION.CURRENT_IS_ROLE_ENABLED or DBMS_SESSION.SESSION_IS_ROLE_ENABLED instead. Parameters Table 154-8 IS_ROLE_ENABLED Function Parameters Parameter Description rolename Name of the role.\ Return Values Table 154-9 IS_ROLE_ENABLED Function Return Values Return Description is_role_enabled TRUE or FALSE , depending on whether the role is enabled