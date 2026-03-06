---
id: 19c__DBMS_XMLDOM.GETCHILDRENBYTAGNAME
name: DBMS_XMLDOM.GETCHILDRENBYTAGNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETCHILDRENBYTAGNAME

This function returns the children of the DOMELEMENT .

## Syntax

```sql
DBMS_XMLDOM.GETCHILDRENBYTAGNAME(
   elem      IN      DOMElement, 
   name      IN      VARCHAR2) 
 RETURN DOMNODELIST;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMElement | IN | DOMELEMENT |
| name | VARCHAR2) | IN | Tag name |
| ns |  |  | Namespace |

**Returns:** `DOMNODELIST`

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax Returns children of the DOMELEMENT given the tag name: DBMS_XMLDOM.GETCHILDRENBYTAGNAME( elem IN DOMElement, name IN VARCHAR2) RETURN DOMNODELIST; Returns children of the DOMELEMENT given the tag name and namespace: DBMS_XMLDOM.GETCHILDRENBYTAGNAME( elem IN DOMElement, name IN VARCHAR2, ns IN VARCHAR2) RETURN DOMNODELIST; Parameters Table 204-48 GETCHILDRENBYTAGNAME Function Parameters Parameter Description elem DOMELEMENT name Tag name ns Namespace