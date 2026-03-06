---
id: 19c__XMLTYPE.GETBLOBVAL
name: XMLTYPE.GETBLOBVAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.GETBLOBVAL

This member function returns a BLOB containing the serialized XML representation. If the BLOB returned is temporary, it must be freed after use.

## Syntax

```sql
MEMBER FUNCTION getBlobVal(
   csid   IN   NUMBER)
 RETURN BLOB DETERMINISTIC;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| csid | NUMBER) | IN | The desired character set ID of output BLOB |

**Returns:** `BLOB`

## Usage Notes

MEMBER FUNCTION getBlobVal( csid IN NUMBER) RETURN BLOB DETERMINISTIC;