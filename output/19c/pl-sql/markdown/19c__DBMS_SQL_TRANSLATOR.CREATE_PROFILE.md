---
id: 19c__DBMS_SQL_TRANSLATOR.CREATE_PROFILE
name: DBMS_SQL_TRANSLATOR.CREATE_PROFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.CREATE_PROFILE

This procedure creates a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.CREATE_PROFILE (
   profile_name    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2) | IN | Name of profile |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.CREATE_PROFILE ( profile_name IN VARCHAR2); Parameters Table 164-4 CREATE_PROFILE Procedure Parameters Parameter Description profile_name Name of profile Exceptions Table 164-5 CREATE_PROFILE Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist PROFILE_EXISTS Profile already exists Usage Notes A SQL translation profile is a database schema object that resides in SQL translation profile namespace. Its name follows the naming rules for database objects of the form [schema.]name . When the schema and profile names are used in the DBMS_SQL_TRANSLATOR package, they are uppercased unless surrounded by double quotation marks. For example, the translation profile profile_name => 'tsql_application' is the same as profile_name => 'Tsql_Application' and profile_name => 'TSQL_APPLICATION' , but not the same as profile_name => '"tsql_application"' . A SQL translation profile is an editionable object type. A SQL translation profile cannot be created as a common object in a multitenant container database (CDB). To destroy a SQL translation profile, use the DROP_PROFILE Procedure . Examples BEGIN DBMS_SQL_TRANSLATOR.CREATE_PROFILE(profile_name => 'tsql_application'); END;