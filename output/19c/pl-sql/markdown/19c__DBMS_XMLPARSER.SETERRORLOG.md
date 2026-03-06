---
id: 19c__DBMS_XMLPARSER.SETERRORLOG
name: DBMS_XMLPARSER.SETERRORLOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.SETERRORLOG

This procedure sets errors to be sent to the specified file.

## Syntax

```sql
PROCEDURE setErrorLog(
  p        Parser,
  fileName VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| fileName | VARCHAR2) | IN | (IN) |

## Usage Notes

Syntax PROCEDURE setErrorLog( p Parser, fileName VARCHAR2);