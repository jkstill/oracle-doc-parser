---
id: 19c__DBMS_SQL_TRANSLATOR.IMPORT_PROFILE
name: DBMS_SQL_TRANSLATOR.IMPORT_PROFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.IMPORT_PROFILE

This procedure imports the content of a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.IMPORT_PROFILE (
   profile_name       IN   VARCHAR2,
   content            IN   CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| content | CLOB) | IN | Content of profile |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.IMPORT_PROFILE ( profile_name IN VARCHAR2, content IN CLOB); Parameters Table 164-18 IMPORT_PROFILE Procedure Parameters Parameter Description profile_name Name of profile content Content of profile Exceptions Table 164-19 IMPORT_PROFILE Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist Usage Notes The content of the SQL translation profile must be in XML format as used by the EXPORT_PROFILE Procedure . All elements and attributes are optional. If the profile does not exist, it is created. If it exists, the content overrides any existing attribute, translator package, SQL or error translation registration. To export the content to a SQL translation profile, use the EXPORT_PROFILE Procedure . Examples DECLARE content CLOB; BEGIN DBMS_SQL_TRANSLATOR.IMPORT_PROFILE( profile_name => 'tsql_application', content => content); END;