---
id: 19c__XMLTYPE.CREATESCHEMABASEDXML
name: XMLTYPE.CREATESCHEMABASEDXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.CREATESCHEMABASEDXML

This member function creates a schema based XMLType instance from a non-schema based XMLType value.

## Syntax

```sql
MEMBER FUNCTION createSchemaBasedXML(
schema IN varchar2 := NULL)
return XMLType deterministic;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | varchar2 | IN | Optional XMLSchema URL used to convert the value to the specified schema. |

**Returns:** `XMLType`

## Usage Notes

It uses either the supplied SCHEMA URL, or the SCHEMALOCATION attribute of the instance. MEMBER FUNCTION createSchemaBasedXML( schema IN varchar2 := NULL) return XMLType deterministic;