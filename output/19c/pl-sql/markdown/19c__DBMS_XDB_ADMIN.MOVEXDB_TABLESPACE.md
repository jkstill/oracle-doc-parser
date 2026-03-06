---
id: 19c__DBMS_XDB_ADMIN.MOVEXDB_TABLESPACE
name: DBMS_XDB_ADMIN.MOVEXDB_TABLESPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_ADMIN
tags: [dbms_xdb_admin]
source_file: DBMS_XDB_ADMIN.html
---

# DBMS_XDB_ADMIN.MOVEXDB_TABLESPACE

This procedure moves the XDB (user) to the specified tablespace.

## Syntax

```sql
DBMS_XDB_ADMIN.MOVEXDB_TABLESPACE(
   new_tablespace   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| new_tablespace | VARCHAR2) | IN | Name of the tablespace to where the XDB is moved |

## Usage Notes

Syntax DBMS_XDB_ADMIN.MOVEXDB_TABLESPACE( new_tablespace IN VARCHAR2); Parameters Table 195-2 MOVEXDB_TABLESPACE Procedure Parameters Parameter Description new_tablespace Name of the tablespace to where the XDB is moved Usage Notes This operation waits for all concurrent XDB sessions to exit. If MOVEXDB_TABLESPACE fails, the user should restart the database before issuing any further command.Failure to do so will result into unexpected behavior from the database. The XDB repository by default resides in the SYSAUX tablespace. Using this procedure it can be moved to another tablespace. As a best practice we recommend to create a dedicated tablespace for the XDB repository only and not share it with other objects (such as tables). The tablespace containing the XDB repository should never be set to READ ONLY because this might affect various XML operations being executed.