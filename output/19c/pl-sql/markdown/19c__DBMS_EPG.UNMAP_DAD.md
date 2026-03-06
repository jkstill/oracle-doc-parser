---
id: 19c__DBMS_EPG.UNMAP_DAD
name: DBMS_EPG.UNMAP_DAD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.UNMAP_DAD

This procedure unmaps a DAD from the specified virtual path. If path is NULL , the procedure removes all virtual-path mappings for the DAD but keeps the DAD.

## Syntax

```sql
DBMS_EPG.UNMAP_DAD (
   dad_name IN VARCHAR2,
   path     IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD to unmap |
| path | VARCHAR2 | IN | The virtual path to unmap |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.UNMAP_DAD ( dad_name IN VARCHAR2, path IN VARCHAR2 DEFAULT NULL); Parameters Table 67-22 UNMAP_DAD Procedure Parameters Parameter Description dad_name The name of the DAD to unmap path The virtual path to unmap Usage Notes Raises and error if the DAD does not exist.