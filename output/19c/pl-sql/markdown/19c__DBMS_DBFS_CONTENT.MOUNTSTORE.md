---
id: 19c__DBMS_DBFS_CONTENT.MOUNTSTORE
name: DBMS_DBFS_CONTENT.MOUNTSTORE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.MOUNTSTORE

This procedure mounts a previously registered store and binds it to the mount point.

## Syntax

```sql
DBMS_DBFS_CONTENT.MOUNTSTORE (
   store_mount    in      VARCHAR2   DEFAULT NULL,
   singleton      in      BOOLEAN    DEFAULT FALSE,
   principal      in      VARCHAR2   DEFAULT NULL,
   owner          in      VARCHAR2   DEFAULT NULL,
   acl            in      VARCHAR2   DEFAULT NULL,
   asof           in      TIMESTAMP  DEFAULT NULL,
   read_only      in      BOOLEAN    DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_mount | VARCHAR2 | in | Path name to use to mount this store |
| singleton | BOOLEAN | in | Whether the mount is a single backend store on the system |
| principal | VARCHAR2 | in | Agent (principal) invoking the current operation |
| owner | VARCHAR2 | in | Owner for new elements created (implicitly or explicitly) by the current operation |
| acl | VARCHAR2 | in | ACL for all new elements created (implicitly or explicitly) by the current operation |
| asof | TIMESTAMP | in | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |
| read_only | BOOLEAN | in | Whether the mount is read-only |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.MOUNTSTORE ( store_mount in VARCHAR2 DEFAULT NULL, singleton in BOOLEAN DEFAULT FALSE, principal in VARCHAR2 DEFAULT NULL, owner in VARCHAR2 DEFAULT NULL, acl in VARCHAR2 DEFAULT NULL, asof in TIMESTAMP DEFAULT NULL, read_only in BOOLEAN DEFAULT FALSE); Parameters Table 52-50 MOUNTSTORE Procedure Parameters Parameter Description store_mount Path name to use to mount this store singleton Whether the mount is a single backend store on the system principal Agent (principal) invoking the current operation owner Owner for new elements created (implicitly or explicitly) by the current operation acl ACL for all new elements created (implicitly or explicitly) by the current operation asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes read_only Whether the mount is read-only Usage Notes See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for information on mounting a registered store See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for information on mounting a registered store