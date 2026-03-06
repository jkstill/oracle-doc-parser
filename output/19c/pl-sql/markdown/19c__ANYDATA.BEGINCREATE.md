---
id: 19c__ANYDATA.BEGINCREATE
name: ANYDATA.BEGINCREATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATA
tags: [anydata]
source_file: ANYDATA-TYPE.html
---

# ANYDATA.BEGINCREATE

This procedure begins the creation process on a new ANYDATA .

## Syntax

```sql
STATIC PROCEDURE BeginCreate(
   dtype          IN OUT NOCOPY AnyType,
   adata          OUT NOCOPY ANYDATA);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dtype | NOCOPY | IN OUT | The type of the ANYDATA . (Should correspond to OCI_TYPECODE_OBJECT or a Collection typecode.) |
| adata | NOCOPY | OUT | ANYDATA being constructed. |

## Usage Notes

Syntax STATIC PROCEDURE BeginCreate( dtype IN OUT NOCOPY AnyType, adata OUT NOCOPY ANYDATA); Parameters Table 280-2 BEGINCREATE Procedure Parameters Parameter Description dtype The type of the ANYDATA . (Should correspond to OCI_TYPECODE_OBJECT or a Collection typecode.) adata ANYDATA being constructed. Exception DBMS_TYPES.INVALID_PARAMETERS : dtype is invalid (not fully constructed, and similar deficits.) Usage Notes There is no need to call PIECEWISE immediately after this call. The construction process begins in a piece-wise manner automatically.