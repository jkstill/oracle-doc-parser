---
id: 19c__DBMS_SESSION.CURRENT_IS_ROLE_ENABLED
name: DBMS_SESSION.CURRENT_IS_ROLE_ENABLED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.CURRENT_IS_ROLE_ENABLED

This function determines if the named role is currently enabled.

## Syntax

```sql
DBMS_SESSION.CURRENT_IS_ROLE_ENABLED (
   rolename    VARCHAR2) 
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rolename | VARCHAR2) | IN | Name of the role. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_SESSION.CURRENT_IS_ROLE_ENABLED ( rolename VARCHAR2) RETURN BOOLEAN; Parameters Table 154-6 CURRENT_IS_ROLE_ENABLED Function Parameters Parameter Description rolename Name of the role. Return Values TRUE -if the role is enabled. FALSE -if the role is not enabled.