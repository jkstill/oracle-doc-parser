---
id: 19c__DBMS_CAPTURE_ADM.ABORT_GLOBAL_INSTANTIATION
name: DBMS_CAPTURE_ADM.ABORT_GLOBAL_INSTANTIATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.ABORT_GLOBAL_INSTANTIATION

This procedure reverses the effects of running the PREPARE_GLOBAL_INSTANTIATION , PREPARE_SCHEMA_INSTANTIATION , and PREPARE_TABLE_INSTANTIATION procedures.

## Syntax

```sql
DBMS_CAPTURE_ADM.ABORT_GLOBAL_INSTANTIATION(
   container    IN  VARCHAR2  DEFAULT 'CURRENT');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| container | VARCHAR2 | IN | Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure removes supplemental logging for the current container. If ALL is specified, then this procedure removes supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure removes supplemental logging for the specified PDB. ALL and pdb_name are valid only when you invoke the procedure from the root. |

## Usage Notes

Specifically, this procedure performs the following actions: Removes data dictionary information related to the database, schema, and table instantiations Removes any supplemental logging enabled by the PREPARE_GLOBAL_INSTANTIATION , PREPARE_SCHEMA_INSTANTIATION , and PREPARE_TABLE_INSTANTIATION procedures Syntax DBMS_CAPTURE_ADM.ABORT_GLOBAL_INSTANTIATION( container IN VARCHAR2 DEFAULT 'CURRENT'); Parameter Table 35-2 ABORT_GLOBAL_INSTANTIATION Procedure Parameter Parameter Description container Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure removes supplemental logging for the current container. If ALL is specified, then this procedure removes supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure removes supplemental logging for the specified PDB. ALL and pdb_name are valid only when you invoke the procedure from the root.