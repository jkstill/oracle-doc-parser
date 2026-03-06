---
id: 19c__DBMS_CAPTURE_ADM.ABORT_SYNC_INSTANTIATION
name: DBMS_CAPTURE_ADM.ABORT_SYNC_INSTANTIATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.ABORT_SYNC_INSTANTIATION

This procedure reverses the effects of running the PREPARE_SYNC_INSTANTIATION procedure. Specifically, this procedure removes data dictionary information related to the table instantiation.

## Syntax

```sql
DBMS_CAPTURE_ADM.ABORT_SYNC_INSTANTIATION(
   table_names IN  VARCHAR2);

DBMS_CAPTURE_ADM.ABORT_SYNC_INSTANTIATION(
   table_names IN  DBMS_UTILITY.UNCL_ARRAY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_names | VARCHAR2) | IN | When the table_names parameter is VARCHAR2 datatype, a comma-delimited list of the tables for which to abort the effects of preparing instantiation. There must be no spaces between entries. When the table_names parameter is DBMS_UTILITY.UNCL_ARRAY datatype, specify a PL/SQL associative array of this type that contains the names of the tables for which to abort the effects of preparing instantiation. The first table name is at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. In either version of the procedure, specify the name of each table in the form [ schema_name .] table_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |

## Usage Notes

This procedure is overloaded. The table_names parameter is VARCHAR2 datatype in one version and DBMS_UTILITY.UNCL_ARRAY datatype in the other version. Syntax DBMS_CAPTURE_ADM.ABORT_SYNC_INSTANTIATION( table_names IN VARCHAR2); DBMS_CAPTURE_ADM.ABORT_SYNC_INSTANTIATION( table_names IN DBMS_UTILITY.UNCL_ARRAY); Parameters Table 35-4 ABORT_SYNC_INSTANTIATION Procedure Parameter Parameter Description table_names When the table_names parameter is VARCHAR2 datatype, a comma-delimited list of the tables for which to abort the effects of preparing instantiation. There must be no spaces between entries. When the table_names parameter is DBMS_UTILITY.UNCL_ARRAY datatype, specify a PL/SQL associative array of this type that contains the names of the tables for which to abort the effects of preparing instantiation. The first table name is at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. In either version of the procedure, specify the name of each table in the form [ schema_name .] table_name . For example, hr.employees . If the schema is not specified, then the current user is the default.