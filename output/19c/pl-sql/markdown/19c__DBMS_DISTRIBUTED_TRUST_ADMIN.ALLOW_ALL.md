---
id: 19c__DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_ALL
name: DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_ALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DISTRIBUTED_TRUST_ADMIN
tags: [dbms_distributed_trust_admin]
source_file: DBMS_DISTRIBUTED_TRUST_ADMIN.html
---

# DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_ALL

This procedure empties the Trusted Servers List and specifies that all servers that are members of a trusted domain in an enterprise directory service and that are in the same domain are allowed access.

## Syntax

```sql
DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_ALL;
```

## Usage Notes

The view TRUSTED_SERVERS will show " TRUSTED ALL " indicating that the database trusts all servers that are currently trusted by the enterprise directory service. Syntax DBMS_DISTRIBUTED_TRUST_ADMIN.ALLOW_ALL; Usage Notes ALLOW_ALL only applies to servers listed as trusted in the enterprise directory service and in the same enterprise domain.