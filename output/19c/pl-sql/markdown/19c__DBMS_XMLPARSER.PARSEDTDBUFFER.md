---
id: 19c__DBMS_XMLPARSER.PARSEDTDBUFFER
name: DBMS_XMLPARSER.PARSEDTDBUFFER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.PARSEDTDBUFFER

PARSEDTDBUFFER parses the DTD stored in the given buffer.

## Syntax

```sql
PROCEDURE PARSEDTDBUFFER(
  p    Parser,
  dtd  VARCHAR2,
  root VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| dtd | VARCHAR2 | IN | (IN) |
| root | VARCHAR2) | IN | (IN) |

## Usage Notes

Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails. Syntax PROCEDURE PARSEDTDBUFFER( p Parser, dtd VARCHAR2, root VARCHAR2);