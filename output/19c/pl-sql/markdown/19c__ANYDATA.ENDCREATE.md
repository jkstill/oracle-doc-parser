---
id: 19c__ANYDATA.ENDCREATE
name: ANYDATA.ENDCREATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATA
tags: [anydata]
source_file: ANYDATA-TYPE.html
---

# ANYDATA.ENDCREATE

This procedure ends creation of an ANYDATA . Other creation functions cannot be called after this call.

## Syntax

```sql
MEMBER PROCEDURE EndCreate(
   self         IN OUT NOCOPY ANYDATA);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | An ANYDATA . |

## Usage Notes

Syntax MEMBER PROCEDURE EndCreate( self IN OUT NOCOPY ANYDATA); Parameters Table 280-3 ENDCREATE Procedure Parameter Parameter Description self An ANYDATA .