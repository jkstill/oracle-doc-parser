---
id: 19c__DBMS_EPG.GET_GLOBAL_ATTRIBUTE
name: DBMS_EPG.GET_GLOBAL_ATTRIBUTE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.GET_GLOBAL_ATTRIBUTE

This function retrieves the value of a global attribute.

## Syntax

```sql
DBMS_EPG.GET_GLOBAL_ATTRIBUTE (
   attr_name  IN  VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| attr_name | VARCHAR2) | IN | The global attribute to retrieve |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.GET_GLOBAL_ATTRIBUTE ( attr_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 67-16 GET_GLOBAL_ATTRIBUTE Procedure Parameters Parameter Description attr_name The global attribute to retrieve Return Values Returns the global attribute value. Returns NULL if attribute has not been set or is not a valid attribute.