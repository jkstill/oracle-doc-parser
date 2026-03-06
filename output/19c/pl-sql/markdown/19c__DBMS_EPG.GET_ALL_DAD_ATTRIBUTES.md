---
id: 19c__DBMS_EPG.GET_ALL_DAD_ATTRIBUTES
name: DBMS_EPG.GET_ALL_DAD_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.GET_ALL_DAD_ATTRIBUTES

This procedure retrieves all the attributes of a DAD. The outputs are 2 correlated index-by tables of the name/value pairs.

## Syntax

```sql
DBMS_EPG.GET_ALL_DAD_ATTRIBUTES (
   dad_name      IN          VARCHAR2,
   attr_names    OUT NOCOPY  VARCHAR2_TABLE,                       
   attr_values   OUT NOCOPY  VARCHAR2_TABLE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name s |  |  | The name of the DAD |
| attr_names | NOCOPY | OUT | The attribute names |
| attr_values | NOCOPY | OUT | The attribute values |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.GET_ALL_DAD_ATTRIBUTES ( dad_name IN VARCHAR2, attr_names OUT NOCOPY VARCHAR2_TABLE, attr_values OUT NOCOPY VARCHAR2_TABLE); Parameters Table 67-11 GET_ALL_DAD_ATTRIBUTES Procedure Parameters Parameter Description dad_name s The name of the DAD attr_names The attribute names attr_values The attribute values Exceptions Raises an error if DAD does not exist.