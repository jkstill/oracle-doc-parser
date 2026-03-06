---
id: 19c__DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_SERVER
name: DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_SERVER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DISTRIBUTED_TRUST_ADMIN
tags: [dbms_distributed_trust_admin]
source_file: DBMS_DISTRIBUTED_TRUST_ADMIN.html
---

# DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_SERVER

This procedure ensures that the specified server is considered untrusted (even if you have previously specified allow all ).

## Syntax

```sql
DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_SERVER (
   server IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| server | VARCHAR2) | IN | Unique, fully-qualified name of the server to be untrusted. |

## Usage Notes

Syntax DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_SERVER ( server IN VARCHAR2); Parameters Table 63-3 DENY_SERVER Procedure Parameters Parameter Description server Unique, fully-qualified name of the server to be untrusted. Usage Notes If the Trusted Servers List contains the entry allow all , then this procedure adds an entry indicating that the specified database (for example, DBx ) is not to be trusted. If the Trusted Servers List contains the entry " deny all ", and if there is no " allow DBx " entry in the list, then this procedure causes no change. If the Trusted Servers List contains the entry " deny all ", and if there is an " allow DBx " entry, then this procedure causes that entry to be deleted.