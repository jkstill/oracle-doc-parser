---
id: 19c__DBMS_XDB_CONFIG.ADDSERVLETSECROLE
name: DBMS_XDB_CONFIG.ADDSERVLETSECROLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ADDSERVLETSECROLE

This procedure adds the security role REF to a specified servlet in XDB configuration.

## Syntax

```sql
<security-role-ref>
     <role-name>rolename</role-name>
     <role-link>rolelink</role-link>
     <description>descript</description>
</security-role-ref>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| servname |  |  | Sservlet name |
| rolename |  |  | Role name |
| rolelink |  |  | Role link |
| descript |  |  | Description |

## Usage Notes

It adds the following security role as shown in the following: <security-role-ref> <role-name>rolename</role-name> <role-link>rolelink</role-link> <description>descript</description> </security-role-ref> Syntax DBMS_XDB_CONFIG.ADDSERVLETSECROLE( servname IN VARCHAR2, rolename IN VARCHAR2, rolelink IN VARCHAR2, descript IN VARCHAR2 := NULL); Parameters Table 196-8 ADDSERVLETSECROLE Procedure Parameters Parameter Description servname Sservlet name rolename Role name rolelink Role link descript Description