---
id: 19c__DBMS_XMLGEN.SETSKIPROWS
name: DBMS_XMLGEN.SETSKIPROWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.SETSKIPROWS

This procedure skips a given number of rows before generating the XML output for every call to the GETXML Functions. It is used when generating paginated results for stateless Web pages using this utility.

## Syntax

```sql
DBMS_XMLGEN.SETSKIPROWS (
ctx       IN ctxHandle,
skipRows  IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle | IN | The context handle corresponding to the query executed. |
| skipRows | NUMBER) | IN | The number of rows to skip for each call to getXML. |

## Usage Notes

For example, when generating the first page of XML or HTML data, set skiprows to zero. For the next set, set the skiprows to the number of rows obtained in the first case. See GETNUMROWSPROCESSED Function . Syntax DBMS_XMLGEN.SETSKIPROWS ( ctx IN ctxHandle, skipRows IN NUMBER); Parameters Table 205-15 SETSKIPROWS Procedure Parameters Parameter Description ctx The context handle corresponding to the query executed. skipRows The number of rows to skip for each call to getXML.