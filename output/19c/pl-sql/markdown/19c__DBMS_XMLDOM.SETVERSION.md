---
id: 19c__DBMS_XMLDOM.SETVERSION
name: DBMS_XMLDOM.SETVERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETVERSION

This procedure sets the version of the DOMDOCUMENT .

## Syntax

```sql
DBMS_XMLDOM.SETVERSION(
   doc        IN     DOMDOCUMENT,
   version    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| version | VARCHAR2) | IN | The version of the document |

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.SETVERSION( doc IN DOMDOCUMENT, version IN VARCHAR2); Parameters Table 204-131 SETVERSION Procedure Parameters Parameter Description doc DOMDOCUMENT version The version of the document