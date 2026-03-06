---
id: 19c__DBMS_SQL_TRANSLATOR
name: DBMS_SQL_TRANSLATOR
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR

This is an example of basic SQL translation using DBMS_SQL_TRANSLATOR .

## Syntax

```sql
BEGIN
  DBMS_SQL_TRANSLATOR.CREATE_PROFILE(
    profile_name     => ' tsql_application');
  DBMS_SQL_TRANSLATOR.SET_ATTRIBUTE(
    profile_name     =>  'tsql_application', 
    attribute_name   =>  DBMS_SQL_TRANSLATOR.ATTR_TRANSLATOR, 
    attribute_value  =>  'migration_repo.sybase_tsql_translator');
END;
```

## Usage Notes

Basic SQL Translation BEGIN DBMS_SQL_TRANSLATOR.CREATE_PROFILE( profile_name => ' tsql_application'); DBMS_SQL_TRANSLATOR.SET_ATTRIBUTE( profile_name => 'tsql_application', attribute_name => DBMS_SQL_TRANSLATOR.ATTR_TRANSLATOR, attribute_value => 'migration_repo.sybase_tsql_translator'); END;