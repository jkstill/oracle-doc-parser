---
id: 19c__DBMS_EPG.GET_ALL_DAD_MAPPINGS
name: DBMS_EPG.GET_ALL_DAD_MAPPINGS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.GET_ALL_DAD_MAPPINGS

This procedure retrieves all the virtual paths to which the specified DAD is mapped.

## Syntax

```sql
DBMS_EPG.GET_ALL_DAD_MAPPINGS (
   dad_name      IN          VARCHAR2,
   paths         OUT NOCOPY  VARCHAR2_TABLE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name s |  |  | The name of the DAD |
| paths | NOCOPY | OUT | The virtual paths to which h the DAD is mapped |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.GET_ALL_DAD_MAPPINGS ( dad_name IN VARCHAR2, paths OUT NOCOPY VARCHAR2_TABLE); Parameters Table 67-12 GET_ALL_DAD_MAPPINGS Procedure Parameters Parameter Description dad_name s The name of the DAD paths The virtual paths to which h the DAD is mapped Exceptions Raises an error if DAD does not exist.