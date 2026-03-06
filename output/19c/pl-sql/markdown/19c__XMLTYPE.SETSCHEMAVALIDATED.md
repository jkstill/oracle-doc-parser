---
id: 19c__XMLTYPE.SETSCHEMAVALIDATED
name: XMLTYPE.SETSCHEMAVALIDATED
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.SETSCHEMAVALIDATED

This member function sets the VALIDATION state of the input XML instance.

## Syntax

```sql
MEMBER PROCEDURE setSchemaValidated(
self IF OUT NOCOPY XMLType,
   flag IN BINARY_INTEGER := 1);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | IF | IN | (OUT) |
| flag | BINARY_INTEGER | IN | (IN) |

## Usage Notes

MEMBER PROCEDURE setSchemaValidated( self IF OUT NOCOPY XMLType, flag IN BINARY_INTEGER := 1);