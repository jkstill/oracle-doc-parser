---
id: 19c__DBMS_EPG.GET_DAD_LIST
name: DBMS_EPG.GET_DAD_LIST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.GET_DAD_LIST

This procedure retrieves a list of all DADs for an Embedded Gateway instance.

## Syntax

```sql
DBMS_EPG.GET_DAD_LIST (
   dad_names     OUT NOCOPY  VARCHAR2_TABLE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_names | NOCOPY | OUT | The list of all DADs |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.GET_DAD_LIST ( dad_names OUT NOCOPY VARCHAR2_TABLE); Parameters Table 67-15 GET_DAD_LIST Procedure Parameters Parameter Description dad_names The list of all DADs Usage Notes If no DADs exist then dad_names will be set to an empty array.