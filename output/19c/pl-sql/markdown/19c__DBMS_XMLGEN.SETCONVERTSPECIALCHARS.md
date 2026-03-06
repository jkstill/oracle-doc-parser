---
id: 19c__DBMS_XMLGEN.SETCONVERTSPECIALCHARS
name: DBMS_XMLGEN.SETCONVERTSPECIALCHARS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.SETCONVERTSPECIALCHARS

This procedure sets whether or not special characters in the XML data must be converted into their escaped XML equivalent. For example, the < sign is converted to &lt; .

## Syntax

```sql
DBMS_XMLGEN.SETCONVERTSPECIALCHARS (
ctx   IN ctxHandle,
conv  IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle | IN | The context handle obtained from one of the NEWCONTEXT Functions call. |
| conv | BOOLEAN) | IN | TRUE indicates that conversion is needed. |

## Usage Notes

The default is to perform conversions. This function improves performance of XML processing when the input data cannot contain any special characters such as < , > , ",' , which must be escaped. It is expensive to scan the character data to replace the special characters, particularly if it involves a lot of data. Syntax DBMS_XMLGEN.SETCONVERTSPECIALCHARS ( ctx IN ctxHandle, conv IN BOOLEAN); Parameters Table 205-10 SETCONVERTSPECIALCHARS Procedure Parameters Parameter Description ctx The context handle obtained from one of the NEWCONTEXT Functions call. conv TRUE indicates that conversion is needed.