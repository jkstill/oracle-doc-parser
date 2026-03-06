---
id: 19c__DATABASE.URIFACTORY
name: DATABASE.URIFACTORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DATABASE
tags: [database]
source_file: Database-URI-TYPEs.html
---

# DATABASE.URIFACTORY

This procedure unregisters a URL handler. This only unregisters user registered handler prefixes and not predefined system prefixes such as http:// .

## Syntax

```sql
PROCEDURE unregisterUrlHandler(
   prefix IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| prefix | VARCHAR2) | IN | (IN) |

## Usage Notes

PROCEDURE unregisterUrlHandler( prefix IN VARCHAR2);