---
id: 19c__DBMS_CAPTURE_ADM.PREPARE_SYNC_INSTANTIATION
name: DBMS_CAPTURE_ADM.PREPARE_SYNC_INSTANTIATION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.PREPARE_SYNC_INSTANTIATION

This function performs the synchronization necessary for instantiating one or more tables at another database. This function returns the prepare system change number (SCN) for the table or tables being prepared for instantiation.

## Syntax

```sql
DBMS_CAPTURE_ADM.PREPARE_SYNC_INSTANTIATION(
   table_names  IN  VARCHAR2)
RETURN NUMBER;

DBMS_CAPTURE_ADM.PREPARE_SYNC_INSTANTIATION(
   table_names  IN  DBMS_UTILITY.UNCL_ARRAY)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_names | VARCHAR2) | IN | When the table_names parameter is VARCHAR2 datatype, a comma-delimited list of the tables to prepare for instantiation. There must be no spaces between entries. When the table_names parameter is DBMS_UTILITY.UNCL_ARRAY datatype, specify a PL/SQL associative array of this type that contains the names of the tables to prepare for instantiation. The first table name is at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. In either version of the function, specify the name of each table in the form [ schema_name .] table_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |

**Returns:** `NUMBER`

## Usage Notes

This function prepares one or more tables for instantiation when a synchronous capture will be used to capture changes to the tables. This function records the lowest SCN of each table for instantiation (prepare SCN). SCNs after the lowest SCN for an object can be used for instantiating the object. This function is overloaded. The table_names parameter is VARCHAR2 datatype in one version and DBMS_UTILITY.UNCL_ARRAY datatype in the other version. Syntax DBMS_CAPTURE_ADM.PREPARE_SYNC_INSTANTIATION( table_names IN VARCHAR2) RETURN NUMBER; DBMS_CAPTURE_ADM.PREPARE_SYNC_INSTANTIATION( table_names IN DBMS_UTILITY.UNCL_ARRAY) RETURN NUMBER; Parameters Table 35-15 PREPARE_SYNC_INSTANTIATION Function Parameter Parameter Description table_names When the table_names parameter is VARCHAR2 datatype, a comma-delimited list of the tables to prepare for instantiation. There must be no spaces between entries. When the table_names parameter is DBMS_UTILITY.UNCL_ARRAY datatype, specify a PL/SQL associative array of this type that contains the names of the tables to prepare for instantiation. The first table name is at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. In either version of the function, specify the name of each table in the form [ schema_name .] table_name . For example, hr.employees . If the schema is not specified, then the current user is the default.