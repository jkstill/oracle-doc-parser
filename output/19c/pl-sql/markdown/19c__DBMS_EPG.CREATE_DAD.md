---
id: 19c__DBMS_EPG.CREATE_DAD
name: DBMS_EPG.CREATE_DAD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.CREATE_DAD

This procedure creates a new DAD.

## Syntax

```sql
DBMS_EPG.CREATE_DAD (
   dad_name  IN  VARCHAR2,
   path      IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD to create |
| path | VARCHAR2 | IN | The virtual path to which to map the DAD |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.CREATE_DAD ( dad_name IN VARCHAR2, path IN VARCHAR2 DEFAULT NULL); Parameters Table 67-6 CREATE_DAD Procedure Parameters Parameter Description dad_name The name of the DAD to create path The virtual path to which to map the DAD