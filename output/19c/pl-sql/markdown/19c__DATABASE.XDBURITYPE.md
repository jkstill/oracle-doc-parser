---
id: 19c__DATABASE.XDBURITYPE
name: DATABASE.XDBURITYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DATABASE
tags: [database]
source_file: Database-URI-TYPEs.html
---

# DATABASE.XDBURITYPE

This constructs a XDBURITYPE instance.

## Syntax

```sql
CONSTRUCTOR FUNCTION XDBURITYPE(
   url     IN   VARCHAR2,
   flags   IN   RAW := NULL)
 RETURN self AS RESULT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| url | VARCHAR2 | IN | (IN) |
| flags | RAW | IN | (IN) |

**Returns:** `self`

## Usage Notes

CONSTRUCTOR FUNCTION XDBURITYPE( url IN VARCHAR2, flags IN RAW := NULL) RETURN self AS RESULT;