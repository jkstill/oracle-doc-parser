---
id: 19c__DBMS_APPLY_ADM.SET_TABLE_INSTANTIATION_SCN
name: DBMS_APPLY_ADM.SET_TABLE_INSTANTIATION_SCN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.SET_TABLE_INSTANTIATION_SCN

This procedure records the specified instantiation SCN for the specified table in the specified source database. This procedure overwrites any existing instantiation SCN for the particular table.

## Syntax

```sql
DBMS_APPLY_ADM.SET_TABLE_INSTANTIATION_SCN(
  source_object_name    IN  VARCHAR2,
  source_database_name  IN  VARCHAR2,
  instantiation_scn     IN  NUMBER,
  apply_database_link   IN  VARCHAR2  DEFAULT NULL,
  source_root_name      IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| source_object_name | VARCHAR2 | IN | The name of the source object specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. When setting an instantiation SCN for a database object, always specify the name of the schema and database object at the source database, even if a rule-based transformation or apply handler is configured to change the schema name or database object name. |
| source_database_name | VARCHAR2 | IN | The global name of the source database. For example, DBS1.NET . If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is NET , then the procedure specifies DBS1.NET automatically. |
| instantiation_scn | NUMBER | IN | The instantiation SCN. Specify NULL to remove the instantiation SCN metadata for the source table from the data dictionary. |
| apply_database_link | VARCHAR2 | IN | The name of the database link to a non-Oracle database. This parameter should be set only when the destination database of a local apply component is a non-Oracle database. Note: This parameter must be NULL when the procedure is invoked from the root of a CDB. |
| source_root_name | VARCHAR2 | IN | The global name of the source root database. In a non-CDB, this parameter must be NULL . In a CDB, both source_database and source_root_name must be specified to identify a specific container. |

## Usage Notes

This procedure gives you precise control over which logical change records (LCRs) for a table are ignored and which LCRs are applied by an apply component. Syntax DBMS_APPLY_ADM.SET_TABLE_INSTANTIATION_SCN( source_object_name IN VARCHAR2, source_database_name IN VARCHAR2, instantiation_scn IN NUMBER, apply_database_link IN VARCHAR2 DEFAULT NULL, source_root_name IN VARCHAR2 DEFAULT NULL); Parameters Table 21-26 SET_TABLE_INSTANTIATION_SCN Procedure Parameters Parameter Description source_object_name The name of the source object specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. When setting an instantiation SCN for a database object, always specify the name of the schema and database object at the source database, even if a rule-based transformation or apply handler is configured to change the schema name or database object name. source_database_name The global name of the source database. For example, DBS1.NET . If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is NET , then the procedure specifies DBS1.NET automatically. instantiation_scn The instantiation SCN. Specify NULL to remove the instantiation SCN metadata for the source table from the data dictionary. apply_database_link The name of the database link to a non-Oracle database. This parameter should be set only when the destination database of a local apply component is a non-Oracle database. Note: This parameter must be NULL when the procedure is invoked from the root of a CDB. source_root_name The global name of the source root database. In a non-CDB, this parameter must be NULL . In a CDB, both source_database and source_root_name must be specified to identify a specific container. Usage Notes The following usage notes apply to this procedure: Instantiation SCNs and LCRs The SET_TABLE_INSTANTIATION_SCN Procedure and XStream Outbound Servers The SET_TABLE_INSTANTIATION_SCN Procedure and XStream Inbound Servers The SET_TABLE_INSTANTIATION_SCN Procedure and CDBs Instantiation SCNs and LCRs If the commit SCN of an LCR for a table from a source database is less than or equal to the instantiation SCN for that table at some destination database, then the apply component at the destination database disregards the LCR. Otherwise, the apply component applies the LCR. The table instantiation SCN specified by this procedure is used on the following types of LCRs: Row LCRs for the table DDL LCRs that have a non- NULL base_table_owner and base_table_name specified, except for DDL LCRs with a command_type of CREATE TABLE For example, the table instantiation SCN set by this procedure is used for DDL LCRs with a command_type of ALTER TABLE or CREATE TRIGGER . Note: The instantiation SCN specified by this procedure is used only for LCRs captured by a capture process. It is not used for user-created LCRs. See Also: SET_GLOBAL_INSTANTIATION_SCN Procedure SET_SCHEMA_INSTANTIATION_SCN Procedure LCR$_ROW_RECORD Type for more information about row LCRs LCR$_DDL_RECORD Type for more information about DDL LCRs The SET_TABLE_INSTANTIATION_SCN Procedure and XStream Outbound Servers Instantiation SCNs are not required for database objects processed by an outbound server. If an instantiation SCN is set for a database object, then the outbound server only sends the LCRs for the database object with SCN values that are greater than the instantiation SCN value. If a database object does not have an instantiation SCN set, then the outbound server skips the instantiation SCN check and sends all LCRs for that database object. In both cases, the outbound server only sends LCRs that satisfy its rule sets. The apply_database_link parameter must be set to NULL or to the local database for this procedure to set an instantiation SCN for an outbound server. See Also: Oracle Database XStream Guide for more information about outbound servers and instantiation SCNs The SET_TABLE_INSTANTIATION_SCN Procedure and XStream Inbound Servers Inbound servers ignore instantiation SCNs. This procedure has no effect on XStream inbound servers. Note: The instantiation SCN specified by this procedure is used only for LCRs captured by a capture process. It is not used for user-created LCRs.