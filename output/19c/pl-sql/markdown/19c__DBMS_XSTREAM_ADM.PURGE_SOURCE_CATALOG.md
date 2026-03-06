---
id: 19c__DBMS_XSTREAM_ADM.PURGE_SOURCE_CATALOG
name: DBMS_XSTREAM_ADM.PURGE_SOURCE_CATALOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.PURGE_SOURCE_CATALOG

This procedure removes all Oracle Replication data dictionary information at the local database for the specified object.

## Syntax

```sql
DBMS_XSTREAM_ADM.PURGE_SOURCE_CATALOG(
   source_database     IN  VARCHAR2,
   source_object_name  IN  VARCHAR2,
   source_object_type  IN  VARCHAR2,
   source_root_name    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| source_database | VARCHAR2 | IN | In a non-CDB, specify the global name of the source database containing the database object. In a CDB, specify the global name of the container containing the database object. The container can be the root or a PDB. If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is .NET , then the procedure specifies DBS1.NET automatically. |
| source_object_name | VARCHAR2 | IN | The name of the object specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| source_object_type | VARCHAR2 | IN | Type of the object. Currently, TABLE is the only possible object type. |
| source_root_name | VARCHAR2) | IN | The global name of the source root containing the object in a CDB. The source root is where the changes being captured originated in a CDB. If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is EXAMPLE.COM , then the procedure specifies DBS1.EXAMPLE.COM automatically. If the source_root_name parameter is NULL , then the global name of the local root is the default. Note: This parameter only applies to a CDB. |

## Usage Notes

You can use this procedure to remove Oracle Replication metadata that is not needed currently and will not be needed in the future. Syntax DBMS_XSTREAM_ADM.PURGE_SOURCE_CATALOG( source_database IN VARCHAR2, source_object_name IN VARCHAR2, source_object_type IN VARCHAR2, source_root_name IN VARCHAR2); Parameters Table 217-24 PURGE_SOURCE_CATALOG Procedure Parameters Parameter Description source_database In a non-CDB, specify the global name of the source database containing the database object. In a CDB, specify the global name of the container containing the database object. The container can be the root or a PDB. If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is .NET , then the procedure specifies DBS1.NET automatically. source_object_name The name of the object specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. source_object_type Type of the object. Currently, TABLE is the only possible object type. source_root_name The global name of the source root containing the object in a CDB. The source root is where the changes being captured originated in a CDB. If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify DBS1 and the domain is EXAMPLE.COM , then the procedure specifies DBS1.EXAMPLE.COM automatically. If the source_root_name parameter is NULL , then the global name of the local root is the default. Note: This parameter only applies to a CDB. Usage Notes The global name of the source database containing the object must be specified for the source_database parameter. If the current database is not the source database for the object, then the procedure removes data dictionary information about the object from the current database, not the source database. For example, suppose changes to the hr.employees table at the dbs1.net source database are being applied to the hr.employees table at the dbs2.net destination database. Also, suppose hr.employees at dbs2.net is not a source at all. In this case, specifying dbs2.net as the source_database for this table results in an error. However, specifying dbs1.net as the source_database for this table while running the PURGE_SOURCE_CATALOG procedure at the dbs2.net database removes data dictionary information about the table at dbs2.net . Do not run this procedure at a database if either of the following conditions is true: Logical change records (LCRs) captured by the capture process for the object are or might be applied locally without reinstantiating the object. LCRs captured by the capture process for the object are or might be forwarded by the database without reinstantiating the object. Note: These conditions do not apply to LCRs that were not created by the capture process. That is, these conditions do not apply to user-created LCRs. Note: These conditions do not apply to LCRs that were not created by the capture process. That is, these conditions do not apply to user-created LCRs.