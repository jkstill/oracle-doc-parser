---
id: 19c__DBMS_LOGSTDBY.INSTANTIATE_TABLE
name: DBMS_LOGSTDBY.INSTANTIATE_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.INSTANTIATE_TABLE

This procedure creates and populates a table in the standby database from a corresponding table in the primary database.

## Syntax

```sql
DBMS_LOGSTDBY.INSTANTIATE_TABLE (
     schema_name         IN VARCHAR2,
     table_name          IN VARCHAR2,
     dblink              IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of the schema |
| table_name | VARCHAR2 | IN | Name of the table to be created or re-created in the standby database |
| dblink | VARCHAR2) | IN | Name of the database link account that has privileges to read and lock the table in the primary database, as well as the SELECT_CATALOG_ROLE on the primary database |

## Usage Notes

The table requires the name of the database link ( dblink) as an input parameter. If the table already exists in the logical standby database, it will be dropped and re-created based on the table definition at the primary database. This procedure only brings over the data associated with the table, and not the associated indexes and constraints. Use the INSTANTIATE_TABLE procedure to: Add a table to a standby database. Re-create a table in a standby database. In a CDB, the INSTANTIATE_TABLE procedure must be called from within the container in which the table to be instantiated resides. Additionally, the database link that is provided to the primary database must point to the corresponding container on the primary. Syntax DBMS_LOGSTDBY.INSTANTIATE_TABLE ( schema_name IN VARCHAR2, table_name IN VARCHAR2, dblink IN VARCHAR2); Parameters Table 102-6 INSTANTIATE_TABLE Procedure Parameters Parameter Description schema_name Name of the schema table_name Name of the table to be created or re-created in the standby database dblink Name of the database link account that has privileges to read and lock the table in the primary database, as well as the SELECT_CATALOG_ROLE on the primary database Exceptions Table 102-7 INSTANTIATE_TABLE Procedure Exceptions Exception Description ORA-16103 Logical Standby apply must be stopped to allow this operation ORA-16236 Logical Standby metadata operation in progress ORA-16276 Specified database link does not correspond to primary database ORA-16277 Specified table is not supported by logical standby database ORA-16278 Specified table has a multi-object skip rule defined Usage Notes Use this procedure to create and populate a table in a way that keeps the data on the standby database transactionally consistent with the primary database. This table will not be synchronized with the rest of the tables being maintained by SQL Apply and SQL Apply will not start to maintain it until SQL Apply encounters redo that occurred after the table was instantiated from the primary. The SCN at which the table was instantiated from the primary database is available in the DBA_LOGSTDBY_EVENTS view. The specified table must be a table that is supported by logical standby (that is, it does not appear in the DBA_LOGSTDBY_UNSUPPORTED_TABLES view on the primary database). If there are any skip rules that specifically name this table (without any wildcards), those skip rules will be dropped as part of INSTANTIATE_TABLE , so that the table will be properly maintained by SQL Apply in the future. If there are skip rules that indirectly reference this table (match a skip rule with a wildcard in the schema_name or table_name , and have a TABLE, DML, or SCHEMA_DDL statement type), INSTANTIATE_TABLE will fail with an ORA-16278 error. Any multi-object skip rules that pertain to the table must be dropped or changed before re-attempting the INSTANTIATE_TABLE call.