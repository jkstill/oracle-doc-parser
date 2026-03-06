---
id: 19c__DBMS_EPG.GET_DAD_ATTRIBUTE
name: DBMS_EPG.GET_DAD_ATTRIBUTE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.GET_DAD_ATTRIBUTE

This procedure retrieves the value of a DAD attribute.

## Syntax

```sql
DBMS_EPG.GET_DAD_ATTRIBUTE (
   dad_name     IN  VARCHAR2,
   attr_name    IN  VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD for which to delete an attribute |
| attr_name | VARCHAR2) | IN | The name of the attribute to delete |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.GET_DAD_ATTRIBUTE ( dad_name IN VARCHAR2, attr_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 67-14 GET_DAD_ATTRIBUTE Function Parameters Parameter Description dad_name The name of the DAD for which to delete an attribute attr_name The name of the attribute to delete Return values Returns the DAD attribute value. Returns NULL if attribute is unknown or has not been set.