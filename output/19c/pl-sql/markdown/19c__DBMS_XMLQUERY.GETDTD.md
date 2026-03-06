---
id: 19c__DBMS_XMLQUERY.GETDTD
name: DBMS_XMLQUERY.GETDTD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.GETDTD

Generates and returns the DTD based on the SQL query used to initialize the context. The options are described in the following table.

## Syntax

```sql
FUNCTION GETDTD(
  ctxHdl IN ctxType,
  withVer IN BOOLEAN := false)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| withVer | BOOLEAN | IN | (IN) |
| xDoc |  |  | (IN) |

**Returns:** `CLOB`

## Usage Notes

Syntax Function that generates the DTD based on the SQL query that is used to initialize the context. FUNCTION GETDTD( ctxHdl IN ctxType, withVer IN BOOLEAN := false) RETURN CLOB; Procedure that generates the DTD based on the SQL query that is used to initialize the context. Specifies the output CLOB for XML document result. PROCEDURE GETDTD( ctxHdl IN ctxType, xDoc IN CLOB, withVer IN BOOLEAN := false); Parameters Table 208-5 GETDTD Subprogram Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. withVer (IN) Generate the version information? TRUE for yes . xDoc (IN) CLOB into which to write the generated XML document.