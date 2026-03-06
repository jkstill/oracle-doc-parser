---
id: 19c__DBMS_SQL_TRANSLATOR.DROP_PROFILE
name: DBMS_SQL_TRANSLATOR.DROP_PROFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.DROP_PROFILE

This procedure drops a SQL translation profile and its contents.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.DROP_PROFILE (
   profile_name     IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2) | IN | Name of profile |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.DROP_PROFILE ( profile_name IN VARCHAR2); Parameters Table 164-10 DROP_PROFILE Procedure Parameters Parameter Description profile_name Name of profile Exceptions Table 164-11 DROP_PROFILE Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Examples BEGIN DBMS_SQL_TRANSLATOR.DROP_PROFILE( profile_name => 'tsql_application'); END;