---
id: 19c__DBMS_XMLSCHEMA.COPYEVOLVE
name: DBMS_XMLSCHEMA.COPYEVOLVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA
tags: [dbms_xmlschema]
source_file: DBMS_XMLSCHEMA.html
---

# DBMS_XMLSCHEMA.COPYEVOLVE

This procedure evolves registered schemas so that existing XML instances remain valid.

## Syntax

```sql
DBMS_XMLSCHEMA.COPYEVOLVE(
   schemaurls       IN  XDB$STRUBG_LIST_T,
   newschemas       IN  XMLSequenceType,
   transforms       IN  XMLSequenceType :=NULL,
   preserveolddocs  IN  BOOLEAN :=FALSE,
   maptablename     IN  VARCHAR2 :=NULL,
   generatetables   IN  BOOLEAN :=TRUE,
   force            IN  BOOLEAN :=FALSE,
   schemaowners     IN  XDB$STRING_LIST_T :=NULL
   parallelDegree   IN  PLS_INTEGER := 0,
   options          IN  PLS_INTEGER := 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schemaurls | XDB$STRUBG_LIST_T | IN | VARRAY of URLs of all schemas to be evolved. Should include the dependent schemas. Unless the FORCE parameter is TRUE , URLs should be in the order of dependency. |
| newschemas | XMLSequenceType | IN | VARRAY of new schema documents. Should be specified in same order as the corresponding URLs. |
| transforms | XMLSequenceType | IN | VARRAY of transforming XSL documents to be applied to schema-based documents. Should be specified in same order as the corresponding URLs. Optional if no transformations are required. |
| preserveolddocs | BOOLEAN | IN | Default is FALSE , and temporary tables with old data are dropped. If TRUE , these table are still available after schema evolution is complete. |
| maptabname |  |  | Specifies the name of the table mapping permanent to temporary tables during the evolution process. Valid columns are: SCHEMA_URL - VARCHAR2(700) - URL of schema to which this table conforms SCHEMA_OWNER - VARCHAR2(30) - Owner of the schema ELEMENT_NAME - VARCHAR2(256) - Element to which this table conforms TAB_NAME - VARCHAR2(65) - Qualified table name: <owner_name>.<table_name> COL_NAME - VARCHAR2(4000) - Name of the column ( NULL for XMLType tables) TEMP_TABNAME - VARCHAR2(30) - Name of temporary tables which holds data for this table. |
| generatetables | BOOLEAN | IN | Default is TRUE , and new tables will be generated. If FALSE : new tables will not be generated after registration of new schemas preserveolddocs must be TRUE maptablename must be non- NULL |
| force | BOOLEAN | IN | Default is FALSE . If TRUE , ignores errors generated during schema evolution. Used when there are circular dependencies among schemas to ensure that all schemas are stored despite possible errors in registration. |
| schemaowners | XDB$STRING_LIST_T | IN | VARRAY of names of schema owners. Should be specified in same order as the corresponding URLs. Default is NULL, assuming that all schemas are owned by the current user. |
| paralleldegree | PLS_INTEGER | IN | Specifies the degree of parallelism to be used in a PARALLEL hint during the data copy stage of the evolution. If this is 0 (default), the PARALLEL hint will not be given in the data copy statements. |
| options | PLS_INTEGER | IN | Currently, the only supported option is COPYEVOLVE_BINARY_XML which lets you register the new schemas for binary XML and create the new tables/columns with binary XML as the storage type. |

## Usage Notes

This procedure is accomplished in according to the following basic scenario (alternative actions are controlled by the procedure's parameters): copies data in schema based XMLType tables to temporary table storage drops old tables deletes old schemas registers new schemas creates new XMLType tables Populates new tables with data in temporary storage; auxiliary structures (constraints, triggers, indexes, and others) are not preserved drops temporary tables See Also: "Schema Evolution" chapter of the Oracle XML DB Developer's Guide for examples on how to evolve existing schemas Oracle Database Error Messages for information on exceptions specific to schema evolution, ORA-30142 through ORA-30946. See Also: "Schema Evolution" chapter of the Oracle XML DB Developer's Guide for examples on how to evolve existing schemas Oracle Database Error Messages for information on exceptions specific to schema evolution, ORA-30142 through ORA-30946. Syntax DBMS_XMLSCHEMA.COPYEVOLVE( schemaurls IN XDB$STRUBG_LIST_T, newschemas IN XMLSequenceType, transforms IN XMLSequenceType :=NULL, preserveolddocs IN BOOLEAN :=FALSE, maptablename IN VARCHAR2 :=NULL, generatetables IN BOOLEAN :=TRUE, force IN BOOLEAN :=FALSE, schemaowners IN XDB$STRING_LIST_T :=NULL parallelDegree IN PLS_INTEGER := 0, options IN PLS_INTEGER := 0); Parameters Table 210-7 COPYEVOLVE Procedure Parameters Parameter Description schemaurls VARRAY of URLs of all schemas to be evolved. Should include the dependent schemas. Unless the FORCE parameter is TRUE , URLs should be in the order of dependency. newschemas VARRAY of new schema documents. Should be specified in same order as the corresponding URLs. transforms VARRAY of transforming XSL documents to be applied to schema-based documents. Should be specified in same order as the corresponding URLs. Optional if no transformations are required. preserveolddocs Default is FALSE , and temporary tables with old data are dropped. If TRUE , these table are still available after schema evolution is complete. maptabname Specifies the name of the table mapping permanent to temporary tables during the evolution process. Valid columns are: SCHEMA_URL - VARCHAR2(700) - URL of schema to which this table conforms SCHEMA_OWNER - VARCHAR2(30) - Owner of the schema ELEMENT_NAME - VARCHAR2(256) - Element to which this table conforms TAB_NAME - VARCHAR2(65) - Qualified table name: <owner_name>.<table_name> COL_NAME - VARCHAR2(4000) - Name of the column ( NULL for XMLType tables) TEMP_TABNAME - VARCHAR2(30) - Name of temporary tables which holds data for this table. generatetables Default is TRUE , and new tables will be generated. If FALSE : new tables will not be generated after registration of new schemas preserveolddocs must be TRUE maptablename must be non- NULL force Default is FALSE . If TRUE , ignores errors generated during schema evolution. Used when there are circular dependencies among schemas to ensure that all schemas are stored despite possible errors in registration. schemaowners VARRAY of names of schema owners. Should be specified in same order as the corresponding URLs. Default is NULL, assuming that all schemas are owned by the current user. paralleldegree Specifies the degree of parallelism to be used in a PARALLEL hint during the data copy stage of the evolution. If this is 0 (default), the PARALLEL hint will not be given in the data copy statements. options Currently, the only supported option is COPYEVOLVE_BINARY_XML which lets you register the new schemas for binary XML and create the new tables/columns with binary XML as the storage type. Usage Notes You should back up all schemas and documents prior to invocation because COPYEVOLVE Procedure deletes all conforming documents prior to implementing the schema evolution.