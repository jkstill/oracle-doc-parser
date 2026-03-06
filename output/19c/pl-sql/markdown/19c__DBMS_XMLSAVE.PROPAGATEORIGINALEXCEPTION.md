---
id: 19c__DBMS_XMLSAVE.PROPAGATEORIGINALEXCEPTION
name: DBMS_XMLSAVE.PROPAGATEORIGINALEXCEPTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.PROPAGATEORIGINALEXCEPTION

The PROPAGATEORIGINALEXCEPTION procedure tells the XSU that if an exception is raised, and is being thrown, the XSU should throw the very exception raised; rather then, wrapping it with an OracleXMLSQLException .

## Syntax

```sql
PROCEDURE propagateOriginalException(
   ctxHdl IN ctxType,
   flag IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN) | IN | (IN) |

## Usage Notes

Syntax PROCEDURE propagateOriginalException( ctxHdl IN ctxType, flag IN BOOLEAN); Parameters Table 209-12 PROPAGATEORIGINALEXCEPTION Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. flag (IN) Propagate the original exception? 0= FALSE , 1= TRUE .