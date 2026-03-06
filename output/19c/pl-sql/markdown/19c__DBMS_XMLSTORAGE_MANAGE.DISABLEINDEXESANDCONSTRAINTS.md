---
id: 19c__DBMS_XMLSTORAGE_MANAGE.DISABLEINDEXESANDCONSTRAINTS
name: DBMS_XMLSTORAGE_MANAGE.DISABLEINDEXESANDCONSTRAINTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.DISABLEINDEXESANDCONSTRAINTS

This procedure disables the indexes and constraints for XMLType tables and XMLType columns.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.DISABLEINDEXESANDCONSTRAINTS (
   owner_name    IN  VARCHAR2 DEFAULT USER, 
   table_name    IN  VARCHAR2, 
   column_name   IN  VARCHAR2 DEFAULT NULL,
   clear         IN  BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name | VARCHAR2 | IN | Owner's name |
| table_name | VARCHAR2 | IN | Name of the XMLType table that the procedure is being performed on |
| column_name | VARCHAR2 | IN | XMLType column name |
| clear | BOOLEAN | IN | Boolean that when set to TRUE clears all stored index and constraint data for the table before the procedure executes. The default is FALSE , which does not clear them. |

## Usage Notes

Syntax DBMS_XMLSTORAGE_MANAGE.DISABLEINDEXESANDCONSTRAINTS ( owner_name IN VARCHAR2 DEFAULT USER, table_name IN VARCHAR2, column_name IN VARCHAR2 DEFAULT NULL, clear IN BOOLEAN DEFAULT FALSE); Parameters Table 213-2 DISABLEINDEXESANDCONSTRAINTS Procedure Parameters Parameter Description owner_name Owner's name table_name Name of the XMLType table that the procedure is being performed on column_name XMLType column name clear Boolean that when set to TRUE clears all stored index and constraint data for the table before the procedure executes. The default is FALSE , which does not clear them. Usage Notes Passing XMLTYPE tables For XMLType tables, you must pass the XMLType table name on which the bulk load operation is to be performed. For XMLType columns, you must pass the relational table name and the corresponding XMLType column name. Using clear to Enable and Disable Indexes and Constraints Note: If the DISABLEINDEXESANDCONTRAINTS procedure is called with clear set to TRUE , it removes any index or constraint information about the XMLTYPE table or column memorized during earlier executions of the procedure. Therefore, you must ensure that all disabled indexes and constraints are re-enabled on the table or column before you call the DISABLEINDEXESANDCONTRAINTS procedure with clear set to TRUE . Ideally, it is recommended that you set clear set to TRUE for the first execution. For any subsequent executions (due to errors while disabling or enabling indexes) clear should be set to FALSE , the default value. Once you have successfully re-enabled all the indexes and constraints following the bulk load operation, you can call this procedure again with clear set to TRUE for the next bulk load operation. Note: If the DISABLEINDEXESANDCONTRAINTS procedure is called with clear set to TRUE , it removes any index or constraint information about the XMLTYPE table or column memorized during earlier executions of the procedure. Example The following example illustrates the use of clear in the DISABLEINDEXESANDCONSTRAINTS procedure and the ENABLEINDEXESANDCONSTRAINTS Procedure . First, add a not- NULL constraint on comment element of the PURCHASEORDER_TAB table: ALTER TABLE PURCHASEORDER_TAB ADD CONSTRAINT c1 check ("XMLDATA"."comment" IS NOT NULL); Then, disable all the indexes and constraints by passing the clear as TRUE , by calling the DISABLEINDEXESANDCONSTRAINTS procedure: BEGIN XDB.DBMS_XMLSTORAGE_MANAGE.DISABLEINDEXESANDCONSTRAINTS ( USER,'PURCHASEORDER_TAB',NULL,TRUE ); END; / Next, perform a bulk load operation (such as datapump import) which violates constraint c1 in the ALTER table statement. This does not raise an error because the constraint is disabled: host impdp orexample/orexample directory=dir dumpfile=dmp.txt tables=OREXAMPLE.PURCHASEORDER_TAB content = DATA_ONLY; NOTE: To view the disabled constraints and indexes use: SELECT constraint_name,table_name,status FROM all_constraints WHERE owner = user; Finally, try to enable the constraint using the ENABLEINDEXESANDCONSTRAINTS procedure. It raises an error because c1 , the not null constraint, is violated by the bulk load operation: BEGIN XDB.DBMS_XMLSTORAGE_MANAGE.ENABLEINDEXESANDCONSTRAINTS ( USER,'PURCHASEORDER_TAB'); END; / To disable all the indexes and constraints, again use DISABLEINDEXESANDCONSTRAINTS , but set clear= FALSE (because the ENABLEINDEXESANDCONSTRAINTS failed to complete successfully). Note: clear = FALSE by default, so we do not need to pass it explicitly in the next call. BEGIN xdb.DBMS_XMLSTORAGE_MANAGE.DISABLEINDEXESANDCONSTRAINTS ( USER,'PURCHASEORDER_TAB'); END; / Then, delete the incorrect rows entered into the table DELETE FROM purchaseorder_tab p WHERE p.xmldata."comment" IS NULL; Re-enable the indexes and constraints using ENABLEINDEXESANDCONSTRAINTS , which completes successfully. BEGIN xdb.DBMS_XMLSTORAGE_MANAGE.ENABLEINDEXESANDCONSTRAINTS ( USER,'PURCHASEORDER_TAB'); END; /