---
id: 19c__DBMS_SQLQ.UNPACK_STGTAB_QUARANTINE
name: DBMS_SQLQ.UNPACK_STGTAB_QUARANTINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.UNPACK_STGTAB_QUARANTINE

This function creates quarantine configurations in a database from a staging table.

## Syntax

```sql
DBMS_SQLQ.UNPACK_STGTAB_QUARANTINE (
   staging_table_name    IN VARCHAR2,
   staging_table_owner   IN VARCHAR2 DEFAULT NULL,
   name                  IN VARCHAR2 DEFAULT '%',
   sql_text              IN VARCHAR2 DEFAULT '%',
   enabled               IN VARCHAR2 DEFAULT NULL)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| staging_table_name | VARCHAR2 | IN | Name of the staging table from which the quarantine configurations need to be created in the database. |
| staging_table_owner | VARCHAR2 | IN | Name of the schema owner of the staging table. Default value is NULL , which means the database user executing this procedure is set as the staging table owner. |
| name | VARCHAR2 | IN | Name of the quarantine configuration. Its value is case-sensitive and it accepts wildcard characters. |
| sql_text | VARCHAR2 | IN | SQL statement text. Its value is case-sensitive and it accepts wildcard characters. |
| enabled | VARCHAR2 | IN | Flag indicating whether the quarantine configuration should be enabled or disabled. If its value is YES , then the quarantine configuration is enabled, else it is disabled. Default value is NULL , which means the quarantine configuration is disabled by default. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SQLQ.UNPACK_STGTAB_QUARANTINE ( staging_table_name IN VARCHAR2, staging_table_owner IN VARCHAR2 DEFAULT NULL, name IN VARCHAR2 DEFAULT '%', sql_text IN VARCHAR2 DEFAULT '%', enabled IN VARCHAR2 DEFAULT NULL) RETURN NUMBER; Parameters Table 167-9 UNPACK_STGTAB_QUARANTINE Function Parameters Parameter Description staging_table_name Name of the staging table from which the quarantine configurations need to be created in the database. staging_table_owner Name of the schema owner of the staging table. Default value is NULL , which means the database user executing this procedure is set as the staging table owner. name Name of the quarantine configuration. Its value is case-sensitive and it accepts wildcard characters. sql_text SQL statement text. Its value is case-sensitive and it accepts wildcard characters. enabled Flag indicating whether the quarantine configuration should be enabled or disabled. If its value is YES , then the quarantine configuration is enabled, else it is disabled. Default value is NULL , which means the quarantine configuration is disabled by default. Return Value Number of quarantine configurations created in the database from the staging table. Examples The following example creates the quarantine configurations in the database from all the quarantine configurations stored in the staging table TBL_STG_QUARANTINE . DECLARE quarantine_configs NUMBER; BEGIN quarantine_configs := DBMS_SQLQ.UNPACK_STGTAB_QUARANTINE( STAGING_TABLE_NAME => 'TBL_STG_QUARANTINE'); END; /