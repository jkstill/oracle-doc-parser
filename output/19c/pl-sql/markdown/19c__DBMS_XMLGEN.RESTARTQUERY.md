---
id: 19c__DBMS_XMLGEN.RESTARTQUERY
name: DBMS_XMLGEN.RESTARTQUERY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.RESTARTQUERY

This procedure restarts the query and generates the XML from the first row.

## Syntax

```sql
DBMS_XMLGEN.RESTARTQUERY (
ctx  IN ctxHandle);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle) | IN | The context handle corresponding to the current query. |

## Usage Notes

It can be used to start executing the query again, without having to create a new context. Syntax DBMS_XMLGEN.RESTARTQUERY ( ctx IN ctxHandle); Parameters Table 205-9 RESTARTQUERY Procedure Parameters Parameter Description ctx The context handle corresponding to the current query.