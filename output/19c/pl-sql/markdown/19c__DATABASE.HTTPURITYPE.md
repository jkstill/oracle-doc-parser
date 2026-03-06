---
id: 19c__DATABASE.HTTPURITYPE
name: DATABASE.HTTPURITYPE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DATABASE
tags: [database]
source_file: Database-URI-TYPEs.html
---

# DATABASE.HTTPURITYPE

This constructs a HTTPURITYPE instance. The HTTPURITYPE instance does not contain the prefix http:// in the stored URL.

## Syntax

```sql
CONSTRUCTOR FUNCTION HTTPURITYPE(
   url IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| url | VARCHAR2) | IN | (IN) |

## Usage Notes

CONSTRUCTOR FUNCTION HTTPURITYPE( url IN VARCHAR2);