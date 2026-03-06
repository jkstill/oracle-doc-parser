---
id: 19c__DBMS_XMLGEN.SETNULLHANDLING
name: DBMS_XMLGEN.SETNULLHANDLING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.SETNULLHANDLING

This procedure sets NULL handling options, handled through the flag parameter setting.

## Syntax

```sql
DBMS_XMLGEN.SETNULLHANDLING(
ctx  IN ctx,
flag IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctx | IN | The context handle corresponding to the query executed. |
| flag | NUMBER) | IN | The NULL handling option set. DROP_NULLS CONSTANT NUMBER:= 0; (Default) Leaves out the tag for NULL elements. NULL_ATTR CONSTANT NUMBER:= 1 ; Sets xsi:nil="true" . EMPTY_TAG CONSTANT NUMBER:= 2; Sets, for example, <foo/> . |

## Usage Notes

Syntax DBMS_XMLGEN.SETNULLHANDLING( ctx IN ctx, flag IN NUMBER); Parameters Table 205-12 SETNULLHANDLING Procedure Parameters Parameter Description ctx The context handle corresponding to the query executed. flag The NULL handling option set. DROP_NULLS CONSTANT NUMBER:= 0; (Default) Leaves out the tag for NULL elements. NULL_ATTR CONSTANT NUMBER:= 1 ; Sets xsi:nil="true" . EMPTY_TAG CONSTANT NUMBER:= 2; Sets, for example, <foo/> .