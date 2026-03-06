---
id: 19c__DBMS_XMLDOM.HASFEATURE
name: DBMS_XMLDOM.HASFEATURE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.HASFEATURE

This function tests if the DOMIMPLEMENTATION implements a specific feature.

## Syntax

```sql
DBMS_XMLDOM.HASFEATURE(
   di       IN     DOMIMPLEMENTATION,
   feature  IN     VARCHAR2,
   version  IN     VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| di | DOMIMPLEMENTATION | IN | DOMIMPLEMENTATION |
| feature | VARCHAR2 | IN | The feature to check for |
| version | VARCHAR2) | IN | The version of the DOM to check in |

**Returns:** `BOOLEAN`

## Usage Notes

See Also: DOMImplementation Subprograms See Also: DOMImplementation Subprograms Syntax DBMS_XMLDOM.HASFEATURE( di IN DOMIMPLEMENTATION, feature IN VARCHAR2, version IN VARCHAR2) RETURN BOOLEAN; Parameters Table 204-90 HASFEATURE Function Parameters Parameter Description di DOMIMPLEMENTATION feature The feature to check for version The version of the DOM to check in