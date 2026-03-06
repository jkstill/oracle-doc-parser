---
id: 19c__XMLTYPE.ISSCHEMAVALID
name: XMLTYPE.ISSCHEMAVALID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.ISSCHEMAVALID

This member function checks if the input instance conforms to a specified schema. I does not change the validation status of the XML instance.

## Syntax

```sql
member function isSchemaValid(
schurl IN VARCHAR2 := NULL,
elem IN VARCHAR2 := NULL)
return NUMBER deterministic;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schurl | VARCHAR2 | IN | (IN) |
| elem | VARCHAR2 | IN | (IN) |

**Returns:** `NUMBER`

## Usage Notes

If an XML Schema URL is not specified and the xml document is schema based, the conformance is checked against the XMLType instance's own schema. member function isSchemaValid( schurl IN VARCHAR2 := NULL, elem IN VARCHAR2 := NULL) return NUMBER deterministic;