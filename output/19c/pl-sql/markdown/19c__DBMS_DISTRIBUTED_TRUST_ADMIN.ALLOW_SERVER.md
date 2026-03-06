---
id: 19c__DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_SERVER
name: DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_SERVER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DISTRIBUTED_TRUST_ADMIN
tags: [dbms_distributed_trust_admin]
source_file: DBMS_DISTRIBUTED_TRUST_ADMIN.html
---

# DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_SERVER

This procedure ensures that the specified server is considered trusted (even if you have previously specified " deny all ").

## Syntax

```sql
DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_SERVER (
   server IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server | VARCHAR2) | IN | Unique, fully-qualified name of the server to be trusted. |

## Usage Notes

Syntax DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_SERVER ( server IN VARCHAR2); Parameters Table 63-2 ALLOW_SERVER Procedure Parameters Parameter Description server Unique, fully-qualified name of the server to be trusted. Usage Notes If the Trusted Servers List contains the entry " deny all ", then this procedure adds a specification indicating that a specific database (for example, DBx ) is to be trusted. If the Trusted Servers List contains the entry " allow all ", and if there is no " deny DBx " entry in the list, then executing this procedure causes no change. If the Trusted Servers List contains the entry " allow all ", and if there is a " deny DBx " entry in the list, then that entry is deleted.