---
id: 19c__DBMS_XMLINDEX.DROPPARAMETER
name: DBMS_XMLINDEX.DROPPARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLINDEX
tags: [dbms_xmlindex]
source_file: DBMS_XMLINDEX.html
---

# DBMS_XMLINDEX.DROPPARAMETER

This procedure drops the XMLIndex parameter string that is associated with a given parameter identifier.

## Syntax

```sql
DBMS_XMLINDEX.DROPPARAMETER (
   name        IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | Identifier for parameter string |

## Usage Notes

Syntax DBMS_XMLINDEX.DROPPARAMETER ( name IN VARCHAR2); Parameters Table 206-4 DROPPARAMETER Procedure Parameters Parameter Description name Identifier for parameter string Examples DBMS_XMLINDEX.DROPPARAMETER ( 'myIndexParam');