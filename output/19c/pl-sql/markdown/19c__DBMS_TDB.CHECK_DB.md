---
id: 19c__DBMS_TDB.CHECK_DB
name: DBMS_TDB.CHECK_DB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TDB
tags: [dbms_tdb]
source_file: DBMS_TDB.html
---

# DBMS_TDB.CHECK_DB

This function checks whether a database can be transported to a target platform. It tests whether transport is supported at all for a given source and destination platform, and whether the database is currently in the correct state for transport.

## Syntax

```sql
DBMS_TDB.CHECK_DB (
     target_platform_name   IN VARCHAR2, 
     skip_option            IN  NUMBER)
   RETURN BOOLEAN;

DBMS_TDB.CHECK_DB (
     target_platform_name   IN VARCHAR2)
   RETURN BOOLEAN;

DBMS_TDB.CHECK_DB 
   RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| target_platform_name | VARCHAR2 | IN | The name of the destination platform, as it appears in V$DB_TRANSPORTABLE_PLATFORM . |
| skip_option | NUMBER) | IN | Specifies which, if any, parts of the database to skip when checking whether the database can be transported. Supported values are listed in Table 175-1 . |

**Returns:** `BOOLEAN`

## Usage Notes

You can specify whether to skip checking parts of the database that are read-only or offline, if you do not plan to transport them. The function is overloaded. The different functionality of each form of syntax is presented along with the definition. Syntax DBMS_TDB.CHECK_DB ( target_platform_name IN VARCHAR2, skip_option IN NUMBER) RETURN BOOLEAN; DBMS_TDB.CHECK_DB ( target_platform_name IN VARCHAR2) RETURN BOOLEAN; DBMS_TDB.CHECK_DB RETURN BOOLEAN; Parameters Table 175-3 CHECK_DB Function Parameters Parameter Description target_platform_name The name of the destination platform, as it appears in V$DB_TRANSPORTABLE_PLATFORM . skip_option Specifies which, if any, parts of the database to skip when checking whether the database can be transported. Supported values are listed in Table 175-1 . Return Values If the database cannot be transported to the target platform or is not ready to be transported, returns FALSE . If the database is ready for transport, returns TRUE . Usage Notes If SERVEROUTPUT is ON , then the output will contain the reasons why the database cannot be transported and how to fix the problems. For details on possible reasons and fixes, see Table 175-4 . Table 175-4 Reasons for CHECK_DB Function to Return FALSE Cause Action Unrecognized target platform name. Check V$DB_TRANSPORTABLE_PLATFORM for recognized platform names. Target platform has a different endian format. Conversion is not supported. Database is not open read-only. Open database read-only and retry. There are active or in-doubt transactions in the database. Open the database read-write. After the active transactions are rolled back, open the database read-only and retry the operation. This situation can occur if users flash back the database and open it read only. The active transactions will be rolled back when the database is opened read-write. Deferred transaction rollback needs to be done. Open the database read-write and bring online the necessary tablespaces. Once the deferred transaction rollback is complete, open the database read-only and retry the operation. Database compatibility version is below 10.0.0. Change the COMPATIBLE initialization parameter to 10.0.0 or higher, open the database read-only, and retry the operation. Some tablespaces have not been open read-write with compatibility version is 10.0.0 or higher. Change the COMPATIBLE initialization parameter to 10.0.0 or higher, then open the affected tablespaces read-write. Shut down the database, open it read-only, and retry the operation.