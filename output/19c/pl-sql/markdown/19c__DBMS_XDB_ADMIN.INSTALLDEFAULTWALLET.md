---
id: 19c__DBMS_XDB_ADMIN.INSTALLDEFAULTWALLET
name: DBMS_XDB_ADMIN.INSTALLDEFAULTWALLET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_ADMIN
tags: [dbms_xdb_admin]
source_file: DBMS_XDB_ADMIN.html
---

# DBMS_XDB_ADMIN.INSTALLDEFAULTWALLET

This procedure installs the default XDB wallet in the default XDB wallet directory.

## Syntax

```sql
DBMS_XDB_ADMIN.INSTALLDEFAULTWALLET;
```

## Usage Notes

The directory name where the XDB wallet is stored is prefixed either by ORACLE_BASE when it is defined, or ORACLE_HOME . It is then followed by /admin/ db_name /xdb_wallet where db_name is the unique database name. Syntax DBMS_XDB_ADMIN.INSTALLDEFAULTWALLET; Usage Notes Only SYS can install or replace the default wallet.