---
id: 19c__DBMS_EPG.DELETE_DAD_ATTRIBUTE
name: DBMS_EPG.DELETE_DAD_ATTRIBUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.DELETE_DAD_ATTRIBUTE

This procedure deletes a DAD attribute.

## Syntax

```sql
DBMS_EPG.DELETE_DAD_ATTRIBUTE (
   dad_name      IN  VARCHAR2,
   attr_name     IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD for which to delete a DAD attribute |
| attr_name | VARCHAR2) | IN | The name of the DAD attribute to delete |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.DELETE_DAD_ATTRIBUTE ( dad_name IN VARCHAR2, attr_name IN VARCHAR2); Parameters Table 67-8 DELETE_DAD_ATTRIBUTE Procedure Parameters Parameter Description dad_name The name of the DAD for which to delete a DAD attribute attr_name The name of the DAD attribute to delete Exceptions Raises an error if DAD does not exist