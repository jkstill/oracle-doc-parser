---
id: 19c__DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS
name: DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS

This procedure clones the dependent objects of the table being redefined onto the interim table and registers the dependent objects. This procedure does not clone the already registered dependent objects.

## Syntax

```sql
DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS(
   uname                    IN  VARCHAR2,
   orig_table               IN  VARCHAR2,
   int_table                IN  VARCHAR2,
   copy_indexes             IN  PLS_INTEGER := 1,
   copy_triggers            IN  BOOLEAN     := TRUE,
   copy_constraints         IN  BOOLEAN     := TRUE,
   copy_privileges          IN  BOOLEAN     := TRUE,
   ignore_errors            IN  BOOLEAN     := FALSE,
   num_errors               OUT PLS_INTEGER,
   copy_statistics          IN  BOOLEAN     := FALSE, 
   copy_mvlog               IN  BOOLEAN     := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uname | VARCHAR2 | IN | Schema name of the tables |
| orig_table | VARCHAR2 | IN | Name of the table being redefined |
| int_table | VARCHAR2 | IN | Name of the interim table |
| copy_indexes | PLS_INTEGER | IN | Flag indicating whether to copy the indexes 0 - do not copy any index dbms_redefinition . cons_orig_params – copy the indexes using the physical parameters of the source indexes |
| copy_triggers | BOOLEAN | IN | TRUE = clone triggers, FALSE = do nothing |
| copy_constraints | BOOLEAN | IN | TRUE = clone constraints, FALSE = do nothing. If compatibility setting is 10.2 or higher, then clone CHECK and NOT NULL constraints |
| copy_privileges | BOOLEAN | IN | TRUE = clone privileges, FALSE = do nothing |
| ignore_errors | BOOLEAN | IN | TRUE = if an error occurs while cloning a particular dependent object, then skip that object and continue cloning other dependent objects. FALSE = that the cloning process should stop upon encountering an error. |
| num_errors | PLS_INTEGER | OUT | Number of errors that occurred while cloning dependent objects |
| copy_statistics | BOOLEAN | IN | TRUE = copy statistics, FALSE = do nothing |
| copy_mvlog | BOOLEAN | IN | TRUE = copy materialized view log, FALSE = do nothing |

## Usage Notes

This subprogram is used to clone the dependent objects like grants, triggers, constraints and privileges from the table being redefined to the interim table (which represents the post-redefinition table). Syntax DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS( uname IN VARCHAR2, orig_table IN VARCHAR2, int_table IN VARCHAR2, copy_indexes IN PLS_INTEGER := 1, copy_triggers IN BOOLEAN := TRUE, copy_constraints IN BOOLEAN := TRUE, copy_privileges IN BOOLEAN := TRUE, ignore_errors IN BOOLEAN := FALSE, num_errors OUT PLS_INTEGER, copy_statistics IN BOOLEAN := FALSE, copy_mvlog IN BOOLEAN := FALSE); Parameters Table 138-7 COPY_TABLE_DEPENDENTS Procedure Parameters Parameter Description uname Schema name of the tables orig_table Name of the table being redefined int_table Name of the interim table copy_indexes Flag indicating whether to copy the indexes 0 - do not copy any index dbms_redefinition . cons_orig_params – copy the indexes using the physical parameters of the source indexes copy_triggers TRUE = clone triggers, FALSE = do nothing copy_constraints TRUE = clone constraints, FALSE = do nothing. If compatibility setting is 10.2 or higher, then clone CHECK and NOT NULL constraints copy_privileges TRUE = clone privileges, FALSE = do nothing ignore_errors TRUE = if an error occurs while cloning a particular dependent object, then skip that object and continue cloning other dependent objects. FALSE = that the cloning process should stop upon encountering an error. num_errors Number of errors that occurred while cloning dependent objects copy_statistics TRUE = copy statistics, FALSE = do nothing copy_mvlog TRUE = copy materialized view log, FALSE = do nothing Usage Notes The user must check the column num_errors before proceeding to ensure that no errors occurred during the cloning of the objects. In case of an error, the user should fix the cause of the error and call the COPY_TABLE_DEPENDENTS Procedure again to clone the dependent object. Alternatively the user can manually clone the dependent object and then register the manually cloned dependent object using the REGISTER_DEPENDENT_OBJECT Procedure . All cloned referential constraints involving the interim tables will be created disabled (they will be automatically enabled after the redefinition) and all triggers on interim tables will not fire till the redefinition is completed. After the redefinition is complete, the cloned objects will be renamed to the corresponding pre-redefinition names of the objects (from which they were cloned from). It is the user's responsibility that the cloned dependent objects are unaffected by the redefinition. All the triggers will be cloned and it is the user's responsibility that the cloned triggers are unaffected by the redefinition.