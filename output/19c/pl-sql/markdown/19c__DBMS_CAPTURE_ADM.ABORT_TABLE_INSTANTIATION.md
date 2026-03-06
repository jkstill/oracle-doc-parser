---
id: 19c__DBMS_CAPTURE_ADM.ABORT_TABLE_INSTANTIATION
name: DBMS_CAPTURE_ADM.ABORT_TABLE_INSTANTIATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CAPTURE_ADM
tags: [dbms_capture_adm]
source_file: DBMS_CAPTURE_ADM.html
---

# DBMS_CAPTURE_ADM.ABORT_TABLE_INSTANTIATION

This procedure reverses the effects of running the PREPARE_TABLE_INSTANTIATION procedure.

## Syntax

```sql
DBMS_CAPTURE_ADM.ABORT_TABLE_INSTANTIATION(
   table_name  IN  VARCHAR2);
   container   IN  VARCHAR2  DEFAULT 'CURRENT');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2) | IN | The name of the table for which to abort the effects of preparing instantiation, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| container | VARCHAR2 | IN | Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure removes supplemental logging for the current container. If ALL is specified, then this procedure removes supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure removes supplemental logging for the specified PDB. ALL and pdb_name are valid only when you invoke the procedure from the root. |

## Usage Notes

Specifically, this procedure performs the following actions: Removes data dictionary information related to the table instantiation Removes any supplemental logging enabled by the PREPARE_TABLE_INSTANTIATION procedure Syntax DBMS_CAPTURE_ADM.ABORT_TABLE_INSTANTIATION( table_name IN VARCHAR2); container IN VARCHAR2 DEFAULT 'CURRENT'); Parameter Table 35-5 ABORT_TABLE_INSTANTIATION Procedure Parameter Parameter Description table_name The name of the table for which to abort the effects of preparing instantiation, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. container Either CURRENT , ALL , or pdb_name . If CURRENT is specified, then this procedure removes supplemental logging for the current container. If ALL is specified, then this procedure removes supplemental logging for all of the containers in the current CDB. If pdb_name is specified, then this procedure removes supplemental logging for the specified PDB. ALL and pdb_name are valid only when you invoke the procedure from the root.