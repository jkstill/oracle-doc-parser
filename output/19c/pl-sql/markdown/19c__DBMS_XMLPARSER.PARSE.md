---
id: 19c__DBMS_XMLPARSER.PARSE
name: DBMS_XMLPARSER.PARSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.PARSE

PARSE parses XML stored in the given URL or file. An application error is raised if parsing fails.

## Syntax

```sql
FUNCTION parse(url VARCHAR2)
RETURN DOMDocument;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| url | VARCHAR2) | IN | (IN) |
| p |  |  | (IN) |

**Returns:** `DOMDocument`

## Usage Notes

There are several versions of this method. Syntax Function. Use this when the default parser behavior is acceptable, and only a URL or file needs to be parsed. Returns the built DOM document. FUNCTION parse(url VARCHAR2) RETURN DOMDocument; Procedure. Any changes to the default parser behavior should be effected before calling this procedure. PROCEDURE parse( p Parser, url VARCHAR2); Parameters Table 207-6 PARSE Subprogram Parameters Parameter IN / OUT Description url (IN) Complete path of the url/file to be parsed. p (IN) Parser instance.