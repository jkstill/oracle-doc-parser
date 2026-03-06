---
id: 19c__DBMS_XMLGEN.USEITEMTAGSFORCOLL
name: DBMS_XMLGEN.USEITEMTAGSFORCOLL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.USEITEMTAGSFORCOLL

This procedure overrides the default name of the collection elements. The default name for collection elements is the type name itself.

## Syntax

```sql
DBMS_XMLGEN.USEITEMTAGSFORCOLL (
   ctx  IN ctxHandle);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle) | IN | The context handle. |

## Usage Notes

Syntax DBMS_XMLGEN.USEITEMTAGSFORCOLL ( ctx IN ctxHandle); Parameters Table 205-16 USEITEMTAGSFORCOLL Procedure Parameters Parameter Description ctx The context handle. Usage Notes Using this procedure, you can override the default to use the name of the column with the _ITEM tag appended to it. If there is a collection of NUMBER , the default tag name for the collection elements is NUMBER .