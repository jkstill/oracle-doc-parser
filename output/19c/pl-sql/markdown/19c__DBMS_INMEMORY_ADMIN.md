---
id: 19c__DBMS_INMEMORY_ADMIN
name: DBMS_INMEMORY_ADMIN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_INMEMORY_ADMIN
tags: [dbms_inmemory_admin]
source_file: DBMS_INMEMORY_ADMIN.html
---

# DBMS_INMEMORY_ADMIN

It is possible for a DBMS_INMEMORY_ADMIN FastStart operation to fail or be interrupted.

## Usage Notes

In a failure or interruption scenario, the following rules determine which subprograms you can use: If FASTSTART_ENABLE does not succeed, then the only permitted operation is re-executing FASTSTART_ENABLE . If FASTSTART_MIGRATE_STORAGE does not succeed, then the only permitted operation is re-executing FASTSTART_MIGRATE_STORAGE . If FASTSTART_DISABLE does not succeed, then all DBMS_INMEMORY_ADMIN operations are permitted.