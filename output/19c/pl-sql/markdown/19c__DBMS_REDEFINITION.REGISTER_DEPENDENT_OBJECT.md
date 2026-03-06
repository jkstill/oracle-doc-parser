---
id: 19c__DBMS_REDEFINITION.REGISTER_DEPENDENT_OBJECT
name: DBMS_REDEFINITION.REGISTER_DEPENDENT_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.REGISTER_DEPENDENT_OBJECT

This procedure registers a dependent object (index, trigger, constraint or materialized view log) on the table being redefined and the corresponding dependent object on the interim table.

## Syntax

```sql
DBMS_REDEFINITION.REGISTER_DEPENDENT_OBJECT(
   uname                  IN    VARCHAR2,
   orig_table             IN    VARCHAR2,
   int_table              IN    VARCHAR2,
   dep_type               IN    PLS_INTEGER,
   dep_owner              IN    VARCHAR2,
   dep_orig_name          IN    VARCHAR2,
   dep_int_name           IN    VARCHAR2);
```

## Usage Notes

This can be used to have the same object on each table but with different attributes. For example: for an index, the storage and tablespace attributes could be different but the columns indexed remain the same Syntax DBMS_REDEFINITION.REGISTER_DEPENDENT_OBJECT( uname IN VARCHAR2, orig_table IN VARCHAR2, int_table IN VARCHAR2, dep_type IN PLS_INTEGER, dep_owner IN VARCHAR2, dep_orig_name IN VARCHAR2, dep_int_name IN VARCHAR2); Parameters Table 138-11 REGISTER_DEPENDENT_OBJECT Procedure Parameters Parameters Description uname Schema name of the tables orig_table Name of the table to be redefined int_table Name of the interim table dep_type Type of the dependent object (see Constants and Operational Notes ) dep_owner Owner of the dependent object dep_orig_name Name of the original dependent object dep_int_name Name of the interim dependent object Usage Notes Attempting to register an already registered object will raise an error. Registering a dependent object will automatically remove that object from DBA_REDEFINITION_ERRORS if an entry exists for that object.