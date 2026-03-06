---
id: 19c__DBMS_XMLPARSER.PARSEBUFFER
name: DBMS_XMLPARSER.PARSEBUFFER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.PARSEBUFFER

PARSEBUFFER parses XML stored in the given buffer.

## Syntax

```sql
PROCEDURE PARSEBUFFER(
  p   Parser,
doc VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| doc | VARCHAR2) | IN | (IN) |

## Usage Notes

Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails. Syntax PROCEDURE PARSEBUFFER( p Parser, doc VARCHAR2);