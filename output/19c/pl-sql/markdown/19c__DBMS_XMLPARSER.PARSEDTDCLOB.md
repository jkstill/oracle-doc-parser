---
id: 19c__DBMS_XMLPARSER.PARSEDTDCLOB
name: DBMS_XMLPARSER.PARSEDTDCLOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.PARSEDTDCLOB

PARSEDTDCLOB parses the DTD stored in the given clob.

## Syntax

```sql
PROCEDURE PARSEDTDCLOB(
  p    Parser,
  dtd  CLOB,
  root VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| dtd | CLOB | IN | (IN) |
| root | VARCHAR2) | IN | (IN) |

## Usage Notes

Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails. Syntax PROCEDURE PARSEDTDCLOB( p Parser, dtd CLOB, root VARCHAR2); Parameters Table 207-11 PARSEDTDCLOB Procedure Parameters Parameter IN / OUT Description p (IN) Parser instance. dtd (IN) DTD Clob to parse. root (IN) Name of the root element.