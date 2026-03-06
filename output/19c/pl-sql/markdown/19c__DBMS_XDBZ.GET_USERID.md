---
id: 19c__DBMS_XDBZ.GET_USERID
name: DBMS_XDBZ.GET_USERID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBZ
tags: [dbms_xdbz]
source_file: DBMS_XDBZ.html
---

# DBMS_XDBZ.GET_USERID

This function retrieves the user ID for the specified user name. The local database is searched first, and if found, the USERID is returned in 4-byte database format. Otherwise, the LDAP directory is searched, if available, and if found, the USERID is returned in 4-byte database format.

## Syntax

```sql
DBMS_XDBZ.GET_USERID(
   username IN  VARCHAR2,
   userid   OUT RAW,
   format   IN  BINARY_INTEGER := NAME_FORMAT_SHORT)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| username | VARCHAR2 | IN | Name of the database or LDAP user. |
| userid | RAW | OUT | Return parameter for the matching user id. |
| format | BINARY_INTEGER | IN | Format of the specified user name; valid options are: DBMS_XDBZ.NAME_FORMAT_SHORT (default) -- DB user name or LDAP nickname DBMS_XDBZ.NAME_FORMAT_DISTINGUISHIED -- LDAP distinguished name. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBZ.GET_USERID( username IN VARCHAR2, userid OUT RAW, format IN BINARY_INTEGER := NAME_FORMAT_SHORT) RETURN BOOLEAN; Parameters Table 202-8 GET_USERID Function Parameters Parameter Description username Name of the database or LDAP user. userid Return parameter for the matching user id. format Format of the specified user name; valid options are: DBMS_XDBZ.NAME_FORMAT_SHORT (default) -- DB user name or LDAP nickname DBMS_XDBZ.NAME_FORMAT_DISTINGUISHIED -- LDAP distinguished name. Return Values Returns TRUE if successful.