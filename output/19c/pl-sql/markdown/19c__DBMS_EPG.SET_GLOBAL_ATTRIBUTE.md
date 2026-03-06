---
id: 19c__DBMS_EPG.SET_GLOBAL_ATTRIBUTE
name: DBMS_EPG.SET_GLOBAL_ATTRIBUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.SET_GLOBAL_ATTRIBUTE

This procedure sets the value of a global attribute.

## Syntax

```sql
DBMS_EPG.SET_GLOBAL_ATTRIBUTE (
   attr_name    IN VARCHAR2,                     
   attr_value   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| attr_name | VARCHAR2 | IN | The global attribute to set |
| attr_value | VARCHAR2) | IN | The attribute value to set |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.SET_GLOBAL_ATTRIBUTE ( attr_name IN VARCHAR2, attr_value IN VARCHAR2); Parameters Table 67-20 SET_GLOBAL_ATTRIBUTE Procedure Parameters Parameter Description attr_name The global attribute to set attr_value The attribute value to set Table 67-21 Mapping Between mod_plsql and Embedded PL/SQL Gateway Global Attributes mod_plsql Global Attribute Embedded PL/SQL Gateway Global Attribute Allows Multiple Occurr-ences Legal Values PlsqlLogLevel log-level No Unsigned integer PlsqlMaxParameters max-parameters No Unsigned integer Usage Notes The attribute name is case sensitive. The value may or may not be case-sensitive depending on the attribute. If attr_name attribute has been set before, then the old value will be overwritten with the new attr_value argument.