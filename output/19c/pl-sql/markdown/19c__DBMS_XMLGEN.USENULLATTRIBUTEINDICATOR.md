---
id: 19c__DBMS_XMLGEN.USENULLATTRIBUTEINDICATOR
name: DBMS_XMLGEN.USENULLATTRIBUTEINDICATOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.USENULLATTRIBUTEINDICATOR

This procedure specifies whether to use an XML attribute to indicate NULL , or to do it by omitting the inclusion of the particular entity in the XML document.

## Syntax

```sql
DBMS_XMLGEN.USENULLATTRIBUTEINDICATOR(
ctx       IN   ctxType,
attrind   IN   BOOLEAN := TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxType | IN | Context handle. |
| attrind | BOOLEAN | IN | Use attribute to indicate NULL ? |

## Usage Notes

It is used as a shortcut for the SETNULLHANDLING Procedure . Syntax DBMS_XMLGEN.USENULLATTRIBUTEINDICATOR( ctx IN ctxType, attrind IN BOOLEAN := TRUE); Parameters Table 205-17 USENULLATTRIBUTEINDICATOR Procedure Parameters Parameter Description ctx Context handle. attrind Use attribute to indicate NULL ?