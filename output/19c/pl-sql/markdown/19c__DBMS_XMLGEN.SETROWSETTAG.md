---
id: 19c__DBMS_XMLGEN.SETROWSETTAG
name: DBMS_XMLGEN.SETROWSETTAG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.SETROWSETTAG

This procedure sets the name of the root element of the document. The default name is ROWSET.

## Syntax

```sql
DBMS_XMLGEN.SETROWSETTAG ( 
ctx            IN ctxHandle,  
rowSetTagName  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle | IN | The context handle obtained from the NEWCONTEXT Functions call. |
| rowSetTagName | VARCHAR2) | IN | The name of the document element. Passing NULL indicates that you do not want the ROWSET element present. |

## Usage Notes

Syntax DBMS_XMLGEN.SETROWSETTAG ( ctx IN ctxHandle, rowSetTagName IN VARCHAR2); Parameters Table 205-13 SETROWSETTAG Procedure Parameters Parameter Description ctx The context handle obtained from the NEWCONTEXT Functions call. rowSetTagName The name of the document element. Passing NULL indicates that you do not want the ROWSET element present. Usage Notes The user can set the rowSetTag to NULL to suppress the printing of this element. However, an error is produced if both the row and the rowset are NULL and there is more than one column or row in the output. This is because the generated XML would not have a top-level enclosing tag, and so would be invalid.