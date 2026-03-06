---
id: 19c__DBMS_XMLGEN.GETNUMROWSPROCESSED
name: DBMS_XMLGEN.GETNUMROWSPROCESSED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.GETNUMROWSPROCESSED

This function retrieves the number of SQL rows processed when generating the XML using the GETXML Functions call. This count does not include the number of rows skipped before generating the XML.

## Syntax

```sql
DBMS_XMLGEN.GETNUMROWSPROCESSED (
   ctx     IN    ctxHandle)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle) | IN | The context handle obtained from the NEWCONTEXT Functions call. |

**Returns:** `NUMBER`

## Usage Notes

Note that GETXML Functions always generates an XML document, even if there are no rows present. Syntax DBMS_XMLGEN.GETNUMROWSPROCESSED ( ctx IN ctxHandle) RETURN NUMBER; Parameters Table 205-4 GETNUMROWSPROCESSED Function Parameters Parameter Description ctx The context handle obtained from the NEWCONTEXT Functions call. Usage Notes This function is used to determine the terminating condition if calling GETXML Functions in a loop.