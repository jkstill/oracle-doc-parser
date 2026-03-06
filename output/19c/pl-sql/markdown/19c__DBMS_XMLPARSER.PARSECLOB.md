---
id: 19c__DBMS_XMLPARSER.PARSECLOB
name: DBMS_XMLPARSER.PARSECLOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.PARSECLOB

PARSECLOB parses XML stored in the given clob.

## Syntax

```sql
PROCEDURE PARSECLOB(
  p   Parser,
doc CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| doc | CLOB) | IN | (IN) |

## Usage Notes

Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails. Syntax PROCEDURE PARSECLOB( p Parser, doc CLOB); Parameters Table 207-8 PARSECLOB Procedure Parameters Parameter IN / OUT Description p (IN) Parser instance. doc (IN) XML document buffer to parse.