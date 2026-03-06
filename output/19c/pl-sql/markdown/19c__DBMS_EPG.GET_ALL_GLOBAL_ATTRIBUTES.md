---
id: 19c__DBMS_EPG.GET_ALL_GLOBAL_ATTRIBUTES
name: DBMS_EPG.GET_ALL_GLOBAL_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.GET_ALL_GLOBAL_ATTRIBUTES

This procedure retrieves all global attributes and values. The outputs are 2 correlated index-by tables of the name/value pairs.

## Syntax

```sql
DBMS_EPG.GET_ALL_GLOBAL_ATTRIBUTES (
   attr_names     OUT   NOCOPY  VARCHAR2_TABLE,
   attr_values    OUT   NOCOPY  VARCHAR2_TABLE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| attr_name s |  |  | The global attribute names |
| attr_values | NOCOPY | OUT | The values of the global attributes |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.GET_ALL_GLOBAL_ATTRIBUTES ( attr_names OUT NOCOPY VARCHAR2_TABLE, attr_values OUT NOCOPY VARCHAR2_TABLE); Parameters Table 67-13 GET_ALL_GLOBAL_ATTRIBUTES Procedure Parameters Parameter Description attr_name s The global attribute names attr_values The values of the global attributes Usage Notes If the gateway instance has no global attributes set, then attr_names and attr_values will be set to empty arrays.