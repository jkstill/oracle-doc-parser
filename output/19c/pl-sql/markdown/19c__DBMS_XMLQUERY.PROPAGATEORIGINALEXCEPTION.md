---
id: 19c__DBMS_XMLQUERY.PROPAGATEORIGINALEXCEPTION
name: DBMS_XMLQUERY.PROPAGATEORIGINALEXCEPTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.PROPAGATEORIGINALEXCEPTION

The PROPAGATEORIGINALEXCEPTION procedure specifies whether to throw every original exception raised or to wrap it in an OracleXMLSQLException .

## Syntax

```sql
PROCEDURE PROPAGATEORIGINALEXCEPTION(
  ctxHdl IN ctxType,
  flag IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN) | IN | (IN) |

## Usage Notes

PROCEDURE PROPAGATEORIGINALEXCEPTION( ctxHdl IN ctxType, flag IN BOOLEAN); Parameters Table 208-10 PROPAGATEORIGINALEXCEPTION Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. flag (IN) TRUE if want to propagate original exception, FALSE to wrap in OracleXMLException.