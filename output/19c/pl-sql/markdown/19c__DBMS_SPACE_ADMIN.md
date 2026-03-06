---
id: 19c__DBMS_SPACE_ADMIN
name: DBMS_SPACE_ADMIN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN

Before migrating the SYSTEM tablespace, certain conditions must be met. These conditions are enforced by the TABLESPACE_MIGRATE_TO_LOCAL procedure, except for the cold backup.

## Usage Notes

The database must have a default temporary tablespace that is not SYSTEM . Dictionary-managed tablespaces cannot have any rollback segments. A locally managed tablespace must have at least one online rollback segment. If you are using automatic undo management, then an undo tablespace must be online. All tablespaces—except the tablespace containing the rollback segment or the undo tablespace—must be read-only. You must have a cold backup of the database. The system must be in restricted mode.