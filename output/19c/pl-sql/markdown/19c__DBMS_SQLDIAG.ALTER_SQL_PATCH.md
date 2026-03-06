---
id: 19c__DBMS_SQLDIAG.ALTER_SQL_PATCH
name: DBMS_SQLDIAG.ALTER_SQL_PATCH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.ALTER_SQL_PATCH

This procedure alters specific attributes of an existing SQL patch object.

## Syntax

```sql
DBMS_SQLDIAG.ALTER_SQL_PATCH (
   name            IN  VARCHAR2,
   attribute_name  IN  VARCHAR2,
   attribute_value IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of SQL patch to alter. |
| attribute_name | VARCHAR2 | IN | Name of SQL patch to alter. Possible values: STATUS -> can be set to ENABLED or DISABLED NAME -> can be reset to a valid name (must be a valid Oracle identifier and must be unique). DESCRIPTION -> can be set to any string of size no more than 500 CATEGORY -> can be reset to a valid category name (must be valid Oracle identifier and must be unique when combined with normalized SQL text) This parameter is mandatory and is case sensitive. |
| attribute_value | VARCHAR2) | IN | New value of the attribute. See attribute_name for valid attribute values. This parameter is mandatory. |

## Usage Notes

Syntax DBMS_SQLDIAG.ALTER_SQL_PATCH ( name IN VARCHAR2, attribute_name IN VARCHAR2, attribute_value IN VARCHAR2); Parameters Table 165-11 ALTER_SQL_PATCH Procedure Parameters Parameter Description name Name of SQL patch to alter. attribute_name Name of SQL patch to alter. Possible values: STATUS -> can be set to ENABLED or DISABLED NAME -> can be reset to a valid name (must be a valid Oracle identifier and must be unique). DESCRIPTION -> can be set to any string of size no more than 500 CATEGORY -> can be reset to a valid category name (must be valid Oracle identifier and must be unique when combined with normalized SQL text) This parameter is mandatory and is case sensitive. attribute_value New value of the attribute. See attribute_name for valid attribute values. This parameter is mandatory. Usage Notes Requires ALTER ANY SQL PATCH privilege