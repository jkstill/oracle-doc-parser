---
id: 19c__DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE
name: DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_INMEMORY_ADMIN
tags: [dbms_inmemory_admin]
source_file: DBMS_INMEMORY_ADMIN.html
---

# DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE

This function returns the tablespace assigned to In-Memory FastStart (IM FastStart). If the feature is disabled, then the function returns NOT ENABLED .

## Syntax

```sql
DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE();
```

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE(); Security Model DBA privileges are required to execute this function. Examples This program obtains the name of the IM FastStart tablespace, if one exists, and prints the result: VARIABLE b_fstbs VARCHAR2(20) BEGIN :b_fstbs := DBMS_INMEMORY_ADMIN.GET_FASTSTART_TABLESPACE; END; / PRINT b_fstbs B_FSTBS ----------------------------- NOT ENABLED