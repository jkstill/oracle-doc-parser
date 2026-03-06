---
id: 19c__DBMS_SQLQ.CREATE_STGTAB_QUARANTINE
name: DBMS_SQLQ.CREATE_STGTAB_QUARANTINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.CREATE_STGTAB_QUARANTINE

This procedure creates a staging table to store the quarantine configurations, so that the staging table can be exported from the current database and imported into another database, thus enabling the quarantine configurations to be used across databases.

## Syntax

```sql
DBMS_SQLQ.CREATE_STGTAB_QUARANTINE (
   staging_table_name   IN VARCHAR2,
   staging_table_owner  IN VARCHAR2 DEFAULT NULL,
   tablespace_name      IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| staging_table_name | VARCHAR2 | IN | Name of the staging table. |
| staging_table_owner | VARCHAR2 | IN | Name of the schema owner of the staging table. Default value is NULL , which means the database user executing this procedure is set as the staging table owner. |
| tablespace_name | VARCHAR2 | IN | Name of the tablespace in which the staging table needs to be created. Default value is NULL , which means the staging table is created in the default tablespace of the database. |

## Usage Notes

Syntax DBMS_SQLQ.CREATE_STGTAB_QUARANTINE ( staging_table_name IN VARCHAR2, staging_table_owner IN VARCHAR2 DEFAULT NULL, tablespace_name IN VARCHAR2 DEFAULT NULL); Parameters Table 167-5 CREATE_STGTAB_QUARANTINE Procedure Parameters Parameter Description staging_table_name Name of the staging table. staging_table_owner Name of the schema owner of the staging table. Default value is NULL , which means the database user executing this procedure is set as the staging table owner. tablespace_name Name of the tablespace in which the staging table needs to be created. Default value is NULL , which means the staging table is created in the default tablespace of the database. Examples The following example creates the staging table TBL_STG_QUARANTINE in the default tablespace of the database and sets its table owner to the database user executing this procedure. BEGIN DBMS_SQLQ.CREATE_STGTAB_QUARANTINE(STAGING_TABLE_NAME => 'TBL_STG_QUARANTINE'); END; /