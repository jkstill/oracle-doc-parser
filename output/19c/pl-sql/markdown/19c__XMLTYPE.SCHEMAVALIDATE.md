---
id: 19c__XMLTYPE.SCHEMAVALIDATE
name: XMLTYPE.SCHEMAVALIDATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.SCHEMAVALIDATE

This member procedure validates the XML instance against its schema, if it has not already been done.

## Syntax

```sql
MEMBER PROCEDURE schemaValidate(
   self IF OUT NOCOPY XMLType);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | IF | IN | (OUT) |

## Usage Notes

For non-schema based documents an error is raised. If validation fails an error is raised; else, the document's status is changed to validated. MEMBER PROCEDURE schemaValidate( self IF OUT NOCOPY XMLType);