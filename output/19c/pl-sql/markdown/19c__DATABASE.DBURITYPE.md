---
id: 19c__DATABASE.DBURITYPE
name: DATABASE.DBURITYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DATABASE
tags: [database]
source_file: Database-URI-TYPEs.html
---

# DATABASE.DBURITYPE

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

The subprograms of the URI Subtype DBPURITYPE member subprogram GETXML are described below. The options are described in the following table. Syntax This function returns the XMLType located at the address specified by the URL. MEMBER FUNCTION getXML() RETURN XMLType; Syntax This function returns the XMLType located at the address specified by the URL and the content type. MEMBER FUNCTION getXML(content OUT VARCHAR2) RETURN XMLType;