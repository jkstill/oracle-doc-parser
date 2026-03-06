---
id: 19c__DBMS_SQLTUNE.DROP_SQL_PROFILE
name: DBMS_SQLTUNE.DROP_SQL_PROFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.DROP_SQL_PROFILE

This procedure drops the named SQL profile from the database.

## Syntax

```sql
DBMS_SQLTUNE.DROP_SQL_PROFILE (
   name          IN  VARCHAR2,
   ignore        IN  BOOLEAN  := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The (mandatory) name of SQL profile to be dropped. The name is case sensitive. |
| ignore | BOOLEAN | IN | Ignores errors due to object not existing |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.DROP_SQL_PROFILE ( name IN VARCHAR2, ignore IN BOOLEAN := FALSE); Parameters Table 169-20 DROP_SQL_PROFILE Procedure Parameters Parameter Description name The (mandatory) name of SQL profile to be dropped. The name is case sensitive. ignore Ignores errors due to object not existing Usage Notes Requires the DROP ANY SQL PROFILE privilege.