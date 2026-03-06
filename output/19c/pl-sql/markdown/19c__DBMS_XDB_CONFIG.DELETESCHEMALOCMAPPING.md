---
id: 19c__DBMS_XDB_CONFIG.DELETESCHEMALOCMAPPING
name: DBMS_XDB_CONFIG.DELETESCHEMALOCMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.DELETESCHEMALOCMAPPING

This procedure deletes the schema location mapping for a specified schema URL from the XDB configuration.

## Syntax

```sql
DBMS_XDB_CONFIG.DELETESCHEMALOCMAPPING(
     schemaURL    IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schemaURL | VARCHAR2) | IN | Schema URL |

## Usage Notes

Syntax DBMS_XDB_CONFIG.DELETESCHEMALOCMAPPING( schemaURL IN VARCHAR2); Parameters Table 196-13 DELETESCHEMALOCMAPPING Procedure Parameters Parameter Description schemaURL Schema URL