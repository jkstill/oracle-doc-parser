---
id: 19c__DBMS_INMEMORY_ADMIN.FASTSTART_DISABLE
name: DBMS_INMEMORY_ADMIN.FASTSTART_DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_INMEMORY_ADMIN
tags: [dbms_inmemory_admin]
source_file: DBMS_INMEMORY_ADMIN.html
---

# DBMS_INMEMORY_ADMIN.FASTSTART_DISABLE

This procedure disables the In-Memory FastStart (IM FastStart) feature.

## Syntax

```sql
DBMS_INMEMORY_ADMIN.FASTSTART_DISABLE();
```

## Usage Notes

Syntax DBMS_INMEMORY_ADMIN.FASTSTART_DISABLE(); Security Model Administrator privileges are required to execute this procedure. Usage Notes When you execute the procedure, the database executes the following actions: Waits until all IM FastStart operations complete Disables the IM FastStart feature, and performs the following operations: Cleans the IM FastStart area Deletes IM FastStart metadata stored in the SYSAUX tablespace Releases the IM FastStart tablespace (but does not delete it) This procedure does not interrupt or affect any concurrent IM column store operations. Examples The following PL/SQL program disables the IM FastStart feature: EXEC DBMS_INMEMORY_ADMIN.FASTSTART_DISABLE; The following query shows that the LOB for the IM FastStart tablespace has been deleted (sample output included): COL OWNER FORMAT a5 COL SEGMENT_NAME FORMAT a20 SELECT l.OWNER, l.SEGMENT_NAME, SUM(s.BYTES)/1024/1024 MB FROM DBA_LOBS l, DBA_SEGMENTS s WHERE l.SEGMENT_NAME = s.SEGMENT_NAME AND l.TABLESPACE_NAME = 'FS_TBS' GROUP BY l.OWNER, l.SEGMENT_NAME; no rows selected