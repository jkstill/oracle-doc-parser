---
id: 19c__DBMS_TDB.CHECK_EXTERNAL
name: DBMS_TDB.CHECK_EXTERNAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TDB
tags: [dbms_tdb]
source_file: DBMS_TDB.html
---

# DBMS_TDB.CHECK_EXTERNAL

This function determines whether a database has external tables, directories, or BFILEs.

## Syntax

```sql
DBMS_TDB.CHECK_EXTERNAL 
   RETURN BOOLEAN;
```

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_TDB.CHECK_EXTERNAL RETURN BOOLEAN; Return Values If the database has external tables, directories, or BFILEs, return TRUE . Otherwise, return FALSE . Usage Notes If SERVEROUTPUT is ON , then the function will output the names of the external tables, directories, and BFILEs in the database. The database must be open read-write. Examples This example illustrates the use of CHECK_EXTERNAL with a database that has several external tables, directories, and BFILEs: SQL> SET SERVEROUTPUT ON SQL> DECLARE external BOOLEAN; BEGIN external := DBMS_TDB.CHECK_EXTERNAL; END; / The following external tables exist in the database: SH.SALES_TRANSACTIONS_EXT The following directories exist in the database: SYS.MEDIA_DIR, SYS.DATA_FILE_DIR, SYS.LOG_FILE_DIR, SYS.DATA_PUMP_DIR The following BFILEs exist in the database: PM.PRINT_MEDIA PL/SQL procedure successfully completed.