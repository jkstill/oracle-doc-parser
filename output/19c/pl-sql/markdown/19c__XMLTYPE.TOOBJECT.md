---
id: 19c__XMLTYPE.TOOBJECT
name: XMLTYPE.TOOBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.TOOBJECT

This member procedure converts the XML value to an object type using the XMLSCHEMA mapping, if available. If a SCHEMA is not supplied or the input is a non-schema based XML, the procedure uses cannonical mapping between elements and object type attributes.

## Syntax

```sql
MEMBER PROCEDURE toObject(
SELF in XMLType,
object OUT "<ADT_1>",
schema in varchar2 := NULL,
element in varchar2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| SELF | XMLType | in | (IN) |
| object | OUT | IN | (IN) |
| schema | varchar2 | in | (IN) |
| element | varchar2 | in | (IN) |

## Usage Notes

MEMBER PROCEDURE toObject( SELF in XMLType, object OUT "<ADT_1>", schema in varchar2 := NULL, element in varchar2 := NULL);