---
id: 19c__DBMS_XMLPARSER.SETBASEDIR
name: DBMS_XMLPARSER.SETBASEDIR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.SETBASEDIR

This procedure sets the base directory used to resolve relative URLs. An application error is raised if parsing fails.

## Syntax

```sql
PROCEDURE setBaseDir(
  p   Parser,
  dir VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| dir | VARCHAR2) | IN | (IN) |

## Usage Notes

Syntax PROCEDURE setBaseDir( p Parser, dir VARCHAR2);