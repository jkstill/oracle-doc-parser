---
id: 19c__DBMS_SQL_TRANSLATOR.SET_ATTRIBUTE
name: DBMS_SQL_TRANSLATOR.SET_ATTRIBUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.SET_ATTRIBUTE

This procedure sets an attribute of a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.SET_ATTRIBUTE (
   profile_name      IN  VARCHAR2,
   attribute_name    IN  VARCHAR2,
   attribute_value   IN  VARCHAR2;)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| attribute_name | VARCHAR2 | IN | Name of attribute |
| attribute_value | VARCHAR2 | IN | Value of attribute |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.SET_ATTRIBUTE ( profile_name IN VARCHAR2, attribute_name IN VARCHAR2, attribute_value IN VARCHAR2;) Parameters Table 164-24 SET_ATTRIBUTE Procedure Parameters Parameter Description profile_name Name of profile attribute_name Name of attribute attribute_value Value of attribute Exceptions Table 164-25 SET_ATTRIBUTE Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Usage Notes See Constants