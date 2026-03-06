---
id: 19c__DBMS_XMLSAVE.SETSQLTOXMLNAMEESCAPING
name: DBMS_XMLSAVE.SETSQLTOXMLNAMEESCAPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETSQLTOXMLNAMEESCAPING

SETSQLTOXMLNAMEESCAPING turns on or off escaping of XML tags in the case that the SQL object name, which is mapped to a XML identifier, is not a valid XML identifier.

## Syntax

```sql
PROCEDURE setSQLToXMLNameEscaping(
   ctxHdl IN ctxType,
   flag IN BOOLEAN := true);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN | IN | (IN) |

## Usage Notes

Syntax PROCEDURE setSQLToXMLNameEscaping( ctxHdl IN ctxType, flag IN BOOLEAN := true); Parameters Table 209-21 SETSQLTOXMLNAMEESCAPING Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. flag (IN) Turn on escaping?