---
id: 19c__DBMS_SQLDIAG.GET_SQL
name: DBMS_SQLDIAG.GET_SQL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.GET_SQL

This function loads a sql_setrow from the trace file associated to an the given incident ID.

## Syntax

```sql
DBMS_SQLDIAG.GET_SQL (
    incident_id  IN     VARCHAR2)
  RETURN SQLSET_ROW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| incident_id | VARCHAR2) | IN | Identifier of the incident |

**Returns:** `SQLSET_ROW`

## Usage Notes

Syntax DBMS_SQLDIAG.GET_SQL ( incident_id IN VARCHAR2) RETURN SQLSET_ROW; Parameters Table 165-24 GET_SQL Function Parameters Parameter Description incident_id Identifier of the incident