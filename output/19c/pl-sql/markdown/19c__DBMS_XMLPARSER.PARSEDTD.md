---
id: 19c__DBMS_XMLPARSER.PARSEDTD
name: DBMS_XMLPARSER.PARSEDTD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.PARSEDTD

PARSEDTD parses the DTD stored in the given URL or file.

## Syntax

```sql
PROCEDURE PARSEDTD(
  p     Parser,
  url   VARCHAR2,
  root  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| url | VARCHAR2 | IN | (IN) |
| root | VARCHAR2) | IN | (IN) |

## Usage Notes

Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails. Syntax PROCEDURE PARSEDTD( p Parser, url VARCHAR2, root VARCHAR2); Parameters Table 207-9 PARSEDTD Procedure Parameters Parameter IN / OUT Description p (IN) Parser instance. url (IN) Complete path of the URL or file to be parsed. root (IN) Name of the root element.