---
id: 19c__DBMS_XMLDOM.GETELEMENTSBYTAGNAME
name: DBMS_XMLDOM.GETELEMENTSBYTAGNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETELEMENTSBYTAGNAME

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETELEMENTSBYTAGNAME(
   doc         IN      DOMDOCUMENT,
   tagname     IN      VARCHAR2)
 RETURN DOMNODELIST;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| tagname | VARCHAR2) | IN | Name of the tag to match on |
| elem |  |  | The DOMELEMENT |
| name |  |  | Tag name; using a wildcard(*) would match any tag |
| ns |  |  | Namespace |

**Returns:** `DOMNODELIST`

## Usage Notes

Syntax Returns a DOMNODELIST of all the elements with a specified tagname (See Also: DOMDocument Subprograms ): DBMS_XMLDOM.GETELEMENTSBYTAGNAME( doc IN DOMDOCUMENT, tagname IN VARCHAR2) RETURN DOMNODELIST; Returns the element children of the DOMELEMENT given the tag name (See Also: DOMElement Subprograms ): DBMS_XMLDOM.GETELEMENTSBYTAGNAME( elem IN DOMELEMENT, name IN VARCHAR2) RETURN DOMNODELIST; Returns the element children of the DOMELEMENT given the tag name and namespace (See Also: DOMElement Subprograms ): DBMS_XMLDOM.GETELEMENTSBYTAGNAME( elem IN DOMELEMENT, name IN VARCHAR2, ns IN VARCHAR2) RETURN DOMNODELIST; Parameters Table 204-52 GETELEMENTSBYTAGNAME Function Parameters Parameter Description doc DOMDOCUMENT tagname Name of the tag to match on elem The DOMELEMENT name Tag name; using a wildcard(*) would match any tag ns Namespace