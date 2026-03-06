---
id: 19c__DBMS_EPG.MAP_DAD
name: DBMS_EPG.MAP_DAD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.MAP_DAD

This procedure maps a DAD to the specified virtual path. If the virtual path exists already, the old virtual-path mapping will be overridden.

## Syntax

```sql
DBMS_EPG.MAP_DAD (
   dad_name  IN  VARCHAR2,
   path      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD to map |
| path | VARCHAR2) | IN | The virtual path to map |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.MAP_DAD ( dad_name IN VARCHAR2, path IN VARCHAR2); Parameters Table 67-17 MAP_DAD Procedure Parameters Parameter Description dad_name The name of the DAD to map path The virtual path to map Exceptions Raises and error if the DAD does not exist.