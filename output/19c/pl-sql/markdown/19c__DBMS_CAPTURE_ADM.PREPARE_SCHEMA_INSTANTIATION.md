---
id: 19c__DBMS_CAPTURE_ADM.PREPARE_SCHEMA_INSTANTIATION
name: DBMS_CAPTURE_ADM.PREPARE_SCHEMA_INSTANTIATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.PREPARE_SCHEMA_INSTANTIATION

This procedure performs the synchronization necessary for instantiating all tables in the schema at another database and can enable supplemental logging for key columns or all columns in these tables.

## Syntax

```sql
DBMS_CAPTURE_ADM.PREPARE_SCHEMA_INSTANTIATION(
   schema_name           IN  VARCHAR2,
   supplemental_logging  IN  VARCHAR2  DEFAULT 'KEYS',
   container             IN  VARCHAR2  DEFAULT 'CURRENT');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema. For example, hr . |
| supplemental_logging | VARCHAR2 | IN | Either NONE , KEYS , or ALL . If NONE is specified, then this procedure does not enable supplemental logging for any columns in the tables in the schema. This procedure does not remove existing supplemental logging specifications for these tables. If KEYS is specified, then this procedure enables supplemental logging for primary key, unique key, bitmap index, and foreign key columns in the tables in the schema and for any table added to this schema in the future. Primary key columns are logged unconditionally. Unique key, bitmap index, and foreign key columns are logged conditionally. Specifying KEYS does not enable supplemental logging of bitmap join index columns. If ALL is specified, then this procedure enables supplemental logging for all columns in the tables in the schema and for any table added to this schema in the future. The columns are logged unconditionally. Supplemental logging is not enabled for columns of the following types: LOB, LONG , LONG RAW , user-defined types, and Oracle-supplied types. |
| container | VARCHAR2 | IN | Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure adds supplemental logging for the current container. If ALL is specified, then this procedure adds supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure adds supplemental logging for the specified PDB ALL and pdb_name are valid only when you invoke the procedure from the root. |

## Usage Notes

This procedure prepares the tables in the schema for instantiation when a capture process will be used to capture changes to the tables in the schema. This procedure records the lowest SCN of each object in the schema for instantiation. SCNs after the lowest SCN for an object can be used for instantiating the object. Running this procedure prepares all current and future objects in the schema for instantiation. Syntax DBMS_CAPTURE_ADM.PREPARE_SCHEMA_INSTANTIATION( schema_name IN VARCHAR2, supplemental_logging IN VARCHAR2 DEFAULT 'KEYS', container IN VARCHAR2 DEFAULT 'CURRENT'); Parameters Table 35-14 PREPARE_SCHEMA_INSTANTIATION Procedure Parameters Parameter Description schema_name The name of the schema. For example, hr . supplemental_logging Either NONE , KEYS , or ALL . If NONE is specified, then this procedure does not enable supplemental logging for any columns in the tables in the schema. This procedure does not remove existing supplemental logging specifications for these tables. If KEYS is specified, then this procedure enables supplemental logging for primary key, unique key, bitmap index, and foreign key columns in the tables in the schema and for any table added to this schema in the future. Primary key columns are logged unconditionally. Unique key, bitmap index, and foreign key columns are logged conditionally. Specifying KEYS does not enable supplemental logging of bitmap join index columns. If ALL is specified, then this procedure enables supplemental logging for all columns in the tables in the schema and for any table added to this schema in the future. The columns are logged unconditionally. Supplemental logging is not enabled for columns of the following types: LOB, LONG , LONG RAW , user-defined types, and Oracle-supplied types. container Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure adds supplemental logging for the current container. If ALL is specified, then this procedure adds supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure adds supplemental logging for the specified PDB ALL and pdb_name are valid only when you invoke the procedure from the root. Usage Notes Run this procedure at the source database. If you use a capture process to capture all of the changes to a schema, then use this procedure to prepare the tables in the schema for instantiation after the capture process has been configured.