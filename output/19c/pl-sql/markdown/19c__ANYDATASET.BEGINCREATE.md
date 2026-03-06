---
id: 19c__ANYDATASET.BEGINCREATE
name: ANYDATASET.BEGINCREATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.BEGINCREATE

This procedure creates a new ANYDATASET which can be used to create a set of data values of the given ANYTYPE.

## Syntax

```sql
STATIC PROCEDURE BeginCreate(
   typecode     IN PLS_INTEGER,
   rtype        IN OUT NOCOPY AnyType,
   aset         OUT NOCOPY ANYDATASET);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| typecode | PLS_INTEGER | IN | The typecode for the type of the ANYDATASET . |
| dtype |  |  | The type of the data values. This parameter is a must for user-defined types like TYPECODE_OBJECT , Collection typecodes, and similar others. |
| aset | NOCOPY | OUT | The ANYDATASET being constructed. |

## Usage Notes

Syntax STATIC PROCEDURE BeginCreate( typecode IN PLS_INTEGER, rtype IN OUT NOCOPY AnyType, aset OUT NOCOPY ANYDATASET); Parameters Table 281-3 BEGINCREATE Procedure Parameter Parameter Description typecode The typecode for the type of the ANYDATASET . dtype The type of the data values. This parameter is a must for user-defined types like TYPECODE_OBJECT , Collection typecodes, and similar others. aset The ANYDATASET being constructed. Exceptions DBMS_TYPES.invalid_parameters: dtype is invalid (not fully constructed, and like errors.)