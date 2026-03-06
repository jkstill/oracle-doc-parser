---
id: 19c__DBMS_EPG.DROP_DAD
name: DBMS_EPG.DROP_DAD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.DROP_DAD

This procedure drops a DAD. All the virtual-path mappings of the DAD will be dropped also.

## Syntax

```sql
DBMS_EPG.DROP_DAD (
   dadname  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name |  |  | The DAD to drop |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.DROP_DAD ( dadname IN VARCHAR2); Parameters Table 67-10 DROP_DAD Procedure Parameters Parameter Description dad_name The DAD to drop Exceptions Raises an error if the DAD does not exist.