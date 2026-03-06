---
id: 19c__DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_ALL
name: DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_ALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DISTRIBUTED_TRUST_ADMIN
tags: [dbms_distributed_trust_admin]
source_file: DBMS_DISTRIBUTED_TRUST_ADMIN.html
---

# DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_ALL

This procedure empties the Trusted Servers List and specifies that all servers are denied access.

## Syntax

```sql
DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_ALL;
```

## Usage Notes

The view TRUSTED_SERVERS will show " UNTRUSTED ALL " indicating that no servers are currently trusted. Syntax DBMS_DISTRIBUTED_TRUST_ADMIN.DENY_ALL;