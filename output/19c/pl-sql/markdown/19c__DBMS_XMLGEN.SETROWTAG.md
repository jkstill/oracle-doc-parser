---
id: 19c__DBMS_XMLGEN.SETROWTAG
name: DBMS_XMLGEN.SETROWTAG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.SETROWTAG

This procedure sets the name of the element separating all the rows. The default name is ROW.

## Syntax

```sql
DBMS_XMLGEN.SETROWTAG (
ctx         IN ctxHandle,
rowTagName  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle | IN | The context handle obtained from the NEWCONTEXT Functions call. |
| rowTagName | VARCHAR2) | IN | The name of the ROW element. Passing NULL indicates that you do not want the ROW element present. |

## Usage Notes

Syntax DBMS_XMLGEN.SETROWTAG ( ctx IN ctxHandle, rowTagName IN VARCHAR2); Parameters Table 205-14 SETROWTAG Procedure Parameters Parameter Description ctx The context handle obtained from the NEWCONTEXT Functions call. rowTagName The name of the ROW element. Passing NULL indicates that you do not want the ROW element present. Usage Notes The user can set the name of the element to NULL to suppress the ROW element itself. However, an error is produced if both the row and the rowset are NULL and there is more than one column or row in the output. This is because the generated XML would not have a top-level enclosing tag, and so would be invalid.