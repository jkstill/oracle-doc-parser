---
id: 19c__DBMS_XMLDOM.WRITETOCLOB
name: DBMS_XMLDOM.WRITETOCLOB
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.WRITETOCLOB

WRITETOCLOB is an overloaded procedure that writes an XML node or document to a specified CLOB .

## Syntax

```sql
DBMS_XMLDOM.WRITETOCLOB(
   n       IN      DOMNODE, 
   cl      IN OUT  CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNODE |
| cl | CLOB) | IN OUT | CLOB to which to write |
| doc |  |  | DOMDOCUMENT |

## Usage Notes

The specific forms of functionality are described along with the syntax declarations. Syntax Writes XML node to specified CLOB using the database character set (See Also: DOMNode Subprograms ): DBMS_XMLDOM.WRITETOCLOB( n IN DOMNODE, cl IN OUT CLOB); Writes XML document to a specified CLOB using database character set (See Also: DOMDocument Subprograms ): DBMS_XMLDOM.WRITETOCLOB( doc IN DOMDOCUMENT, cl IN OUT CLOB); Parameters Table 204-136 WRITETOCLOB Procedure Parameters Parameter Description n DOMNODE cl CLOB to which to write doc DOMDOCUMENT