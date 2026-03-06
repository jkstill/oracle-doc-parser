---
id: 19c__DBMS_XMLGEN.SETMAXROWS
name: DBMS_XMLGEN.SETMAXROWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.SETMAXROWS

This procedure sets the maximum number of rows to fetch from the SQL query result for every invocation of the GETXML Functions call.

## Syntax

```sql
DBMS_XMLGEN.SETMAXROWS (
ctx      IN ctxHandle,
maxRows  IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle | IN | The context handle corresponding to the query executed. |
| maxRows | NUMBER) | IN | The maximum number of rows to get for each call to GETXML Functions |

## Usage Notes

It is used when generating paginated results. For example, when generating a page of XML or HTML data, restrict the number of rows converted to XML or HTML by setting the maxrows parameter. Syntax DBMS_XMLGEN.SETMAXROWS ( ctx IN ctxHandle, maxRows IN NUMBER); Parameters Table 205-11 SETMAXROWS Procedure Parameters Parameter Description ctx The context handle corresponding to the query executed. maxRows The maximum number of rows to get for each call to GETXML Functions