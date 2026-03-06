---
id: 19c__DATABASE.URITYPE
name: DATABASE.URITYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DATABASE
tags: [database]
source_file: Database-URI-TYPEs.html
---

# DATABASE.URITYPE

This function returns the XMLType located at the address specified by the URL.

## Syntax

```sql
MEMBER FUNCTION getXML()
  RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| content |  |  | (OUT) |

**Returns:** `XMLType`

## Usage Notes

Syntax This function can be overridden in the subtype instances. The options are described below. This function returns the XMLType located at the address specified by the URL. MEMBER FUNCTION getXML() RETURN XMLType; Syntax This function returns the XMLType located at the address specified by the URL and the content type. MEMBER FUNCTION getXML(content OUT VARCHAR2) RETURN XMLType;