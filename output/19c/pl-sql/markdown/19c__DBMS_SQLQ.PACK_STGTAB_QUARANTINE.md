---
id: 19c__DBMS_SQLQ.PACK_STGTAB_QUARANTINE
name: DBMS_SQLQ.PACK_STGTAB_QUARANTINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.PACK_STGTAB_QUARANTINE

This function adds one or more quarantine configurations into a staging table.

## Syntax

```sql
DBMS_SQLQ.PACK_STGTAB_QUARANTINE (
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
| staging_table_name | VARCHAR2 | IN | Name of the staging table in which the quarantine configurations need to be added. |
| staging_table_owner | VARCHAR2 | IN | Name of the schema owner of the staging table. Default value is NULL , which means the database user executing this procedure is set as the staging table owner. |
| name | VARCHAR2 | IN | Name of the quarantine configuration. Its value is case-sensitive and it accepts wildcard characters. |
| sql_text | VARCHAR2 | IN | SQL statement text. Its value is case-sensitive and it accepts wildcard characters. |
| enabled | VARCHAR2 | IN | Flag indicating whether the quarantine configuration should be enabled or disabled. If it is set to YES , then the quarantine configuration is enabled, else it is disabled. Default value is NULL , which means the quarantine configuration is disabled by default. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SQLQ.PACK_STGTAB_QUARANTINE ( staging_table_name IN VARCHAR2, staging_table_owner IN VARCHAR2 DEFAULT NULL, name IN VARCHAR2 DEFAULT '%', sql_text IN VARCHAR2 DEFAULT '%', enabled IN VARCHAR2 DEFAULT NULL) RETURN NUMBER; Parameters Table 167-8 PACK_STGTAB_QUARANTINE Function Parameters Parameter Description staging_table_name Name of the staging table in which the quarantine configurations need to be added. staging_table_owner Name of the schema owner of the staging table. Default value is NULL , which means the database user executing this procedure is set as the staging table owner. name Name of the quarantine configuration. Its value is case-sensitive and it accepts wildcard characters. sql_text SQL statement text. Its value is case-sensitive and it accepts wildcard characters. enabled Flag indicating whether the quarantine configuration should be enabled or disabled. If it is set to YES , then the quarantine configuration is enabled, else it is disabled. Default value is NULL , which means the quarantine configuration is disabled by default. Return Value Number of quarantine configurations added to the staging table. Examples The following example adds all the quarantine configurations having the names starting with SQL_QUARANTINE_ into the staging table TBL_STG_QUARANTINE . DECLARE quarantine_configs NUMBER; BEGIN quarantine_configs := DBMS_SQLQ.PACK_STGTAB_QUARANTINE( STAGING_TABLE_NAME => 'TBL_STG_QUARANTINE', NAME => 'SQL_QUARANTINE_%'); END; /