---
id: 19c__DBMS_INMEMORY_ADMIN.FASTSTART_MIGRATE_STORAGE
name: DBMS_INMEMORY_ADMIN.FASTSTART_MIGRATE_STORAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_INMEMORY_ADMIN
tags: [dbms_inmemory_admin]
source_file: DBMS_INMEMORY_ADMIN.html
---

# DBMS_INMEMORY_ADMIN.FASTSTART_MIGRATE_STORAGE

This procedure moves the In-Memory FastStart (IM FastStart) data and catalogs from the current tablespace to a new tablespace.

## Syntax

```sql
DBMS_INMEMORY_ADMIN.FASTSTART_MIGRATE_STORAGE( 
   tbs_name    IN    VARCHAR2 );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tbs_name | VARCHAR2 | IN | The name of the new ASSM tablespace for the IM FastStart area. |

## Usage Notes

Syntax DBMS_INMEMORY_ADMIN.FASTSTART_MIGRATE_STORAGE( tbs_name IN VARCHAR2 ); Parameters Table 90-3 FASTSTART_MIGRATE_STORAGE Procedure Parameters Parameter Description tbs_name The name of the new ASSM tablespace for the IM FastStart area. Security Model DBA privileges are required to execute this procedure. Usage Notes When you execute the procedure, the database executes the following actions: Waits until all IM FastStart operations complete Disables the IM FastStart feature Copies IM FastStart data and metadata to the new tablespace, leaving the old tablespace intact Re-enables IM FastStart the feature Examples The following program obtains the name of the IM FastStart tablespace, if one exists, and prints the result (sample output included): VARIABLE b_fstbs VARCHAR2(20) BEGIN :b_fstbs := DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE; END; / PRINT b_fstbs B_FSTBS ----------------------------- FS_TBS The following statements create a new tablespace named fs_tbs2 , and then migrate the IM FastStart area to this tablespace: CREATE TABLESPACE fs_tbs2 DATAFILE 'fs_tbs2.dbf' SIZE 500M EXTENT MANAGEMENT LOCAL SEGMENT SPACE MANAGEMENT AUTO; EXEC DBMS_INMEMORY_ADMIN.FASTSTART_MIGRATE_STORAGE('fs_tbs2'); The following program prints the name of the current IM FastStart tablespace (sample output included): BEGIN :b_fstbs := DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE; END; / PRINT b_fstbs B_FSTBS ----------------------------- FS_TBS2