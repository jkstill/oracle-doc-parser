---
id: 19c__DBMS_CAPTURE_ADM.PREPARE_TABLE_INSTANTIATION
name: DBMS_CAPTURE_ADM.PREPARE_TABLE_INSTANTIATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.PREPARE_TABLE_INSTANTIATION

This procedure performs the synchronization necessary for instantiating the table at another database and can enable supplemental logging for key columns or all columns in the table

## Syntax

```sql
DBMS_CAPTURE_ADM.PREPARE_TABLE_INSTANTIATION(
   table_name            IN  VARCHAR2,
   supplemental_logging  IN  VARCHAR2  DEFAULT 'KEYS',
   container             IN  VARCHAR2  DEFAULT 'CURRENT');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | The name of the table specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| supplemental_logging | VARCHAR2 | IN | Either NONE , KEYS , or ALL . If NONE is specified, then this procedure does not enable supplemental logging for any columns in the table. This procedure does not remove existing supplemental logging specifications for the table. If KEYS is specified, then this procedure enables supplemental logging for primary key, unique key, bitmap index, and foreign key columns in the table. The procedure places the key columns for the table in three separate log groups: the primary key columns in an unconditional log group, the unique key columns and bitmap index columns in a conditional log group, and the foreign key columns in a conditional log group. Specifying KEYS does not enable supplemental logging of bitmap join index columns. If ALL is specified, then this procedure enables supplemental logging for all columns in the table. The procedure places all of the columns for the table in an unconditional log group. Supplemental logging is not enabled for columns of the following types: LOB, LONG , LONG RAW , user-defined types, and Oracle-supplied types. |
| container | VARCHAR2 | IN | Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure adds supplemental logging for the current container. If ALL is specified, then this procedure adds supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure adds supplemental logging for the specified PDB. ALL and pdb_name are valid only when you invoke the procedure from the root. |

## Usage Notes

This procedure prepares the table for instantiation when a capture process will be used to capture changes to the table. This procedure records the lowest SCN of the table for instantiation. SCNs after the lowest SCN for an object can be used for instantiating the object. Syntax DBMS_CAPTURE_ADM.PREPARE_TABLE_INSTANTIATION( table_name IN VARCHAR2, supplemental_logging IN VARCHAR2 DEFAULT 'KEYS', container IN VARCHAR2 DEFAULT 'CURRENT'); Parameters Table 35-16 PREPARE_TABLE_INSTANTIATION Procedure Parameters Parameter Description table_name The name of the table specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. supplemental_logging Either NONE , KEYS , or ALL . If NONE is specified, then this procedure does not enable supplemental logging for any columns in the table. This procedure does not remove existing supplemental logging specifications for the table. If KEYS is specified, then this procedure enables supplemental logging for primary key, unique key, bitmap index, and foreign key columns in the table. The procedure places the key columns for the table in three separate log groups: the primary key columns in an unconditional log group, the unique key columns and bitmap index columns in a conditional log group, and the foreign key columns in a conditional log group. Specifying KEYS does not enable supplemental logging of bitmap join index columns. If ALL is specified, then this procedure enables supplemental logging for all columns in the table. The procedure places all of the columns for the table in an unconditional log group. Supplemental logging is not enabled for columns of the following types: LOB, LONG , LONG RAW , user-defined types, and Oracle-supplied types. container Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure adds supplemental logging for the current container. If ALL is specified, then this procedure adds supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure adds supplemental logging for the specified PDB. ALL and pdb_name are valid only when you invoke the procedure from the root. Usage Notes Run this procedure at the source database. If you use a capture process to capture all of the changes to a table, then use this procedure to prepare the table for instantiation after the capture process has been configured.