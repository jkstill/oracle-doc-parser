---
id: 19c__DBMS_XMLDOM.CREATEENTITYREFERENCE
name: DBMS_XMLDOM.CREATEENTITYREFERENCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATEENTITYREFERENCE

This function creates a DOMENTITYREFERENCE node.

## Syntax

```sql
DBMS_XMLDOM.CREATEENTITYREFERENCE(
   doc        IN     DOMDOCUMENT,
   name       IN     VARCHAR2)
 RETURN DOMENTITYREFERENCE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| name | VARCHAR2) | IN | New entity reference name |

**Returns:** `DOMENTITYREFERENCE`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.CREATEENTITYREFERENCE( doc IN DOMDOCUMENT, name IN VARCHAR2) RETURN DOMENTITYREFERENCE; Parameters Table 204-32 CREATEENTITYREFERENCE Function Parameters Parameter Description doc DOMDOCUMENT name New entity reference name