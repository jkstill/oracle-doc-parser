---
id: 19c__DBMS_SQLTUNE.ALTER_SQL_PROFILE
name: DBMS_SQLTUNE.ALTER_SQL_PROFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.ALTER_SQL_PROFILE

This procedure alters specific attributes of an existing SQL profile object.

## Syntax

```sql
DBMS_SQLTUNE.ALTER_SQL_PROFILE (
   name                 IN  VARCHAR2,
   attribute_name       IN  VARCHAR2,
   value                IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The (mandatory) name of the existing SQL profile to alter |
| attribute_name | VARCHAR2 | IN | The (mandatory) attribute name to alter (case insensitive) using valid attribute names |
| value | VARCHAR2) | IN | The (mandatory) new value of the attribute using valid attribute values |

## Usage Notes

The following attributes can be altered (using these attribute names): STATUS can be set to ENABLED or DISABLED . NAME can be reset to a valid name which must be a valid Oracle identifier and must be unique. DESCRIPTION can be set to any string of size no more than 500 characters. CATEGORY can be reset to a valid category name which must be a valid Oracle identifier and must be unique when combined with normalized SQL text). See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.ALTER_SQL_PROFILE ( name IN VARCHAR2, attribute_name IN VARCHAR2, value IN VARCHAR2); Parameters Table 169-11 ALTER_SQL_PROFILE Procedure Parameters Parameter Description name The (mandatory) name of the existing SQL profile to alter attribute_name The (mandatory) attribute name to alter (case insensitive) using valid attribute names value The (mandatory) new value of the attribute using valid attribute values Usage Notes Requires the ALTER ANY SQL PROFILE privilege.