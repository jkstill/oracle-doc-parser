---
id: 19c__DBMS_REDEFINITION.START_REDEF_TABLE
name: DBMS_REDEFINITION.START_REDEF_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.START_REDEF_TABLE

This procedure starts a table redefinition.

## Syntax

```sql
DBMS_REDEFINITION.START_REDEF_TABLE (
   uname                   IN  VARCHAR2,
   orig_table              IN  VARCHAR2,
   int_table               IN  VARCHAR2,
   col_mapping             IN  VARCHAR2 := NULL,
   options_flag            IN  BINARY_INTEGER := 1,
   orderby_cols            IN  VARCHAR2 := NULL,
   part_name               IN  VARCHAR2 := NULL,
   continue_after_errors   IN  BOOLEAN := FALSE,    
   copy_vpd_opt            IN  BINARY_INTEGER := CONS_VPD_NONE,
   refresh_dep_mviews      IN  VARCHAR2 := 'N',
   enable_rollback         IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uname | VARCHAR2 | IN | Schema name of the tables |
| orig_table | VARCHAR2 | IN | Name of the table to be redefined |
| int_table | VARCHAR2 | IN | Name of the interim table. Can take a comma-delimited list of interim table names. |
| col_mapping | VARCHAR2 | IN | Mapping information from the columns in the original table to the columns in the interim table. (This is similar to the column list on the SELECT clause of a query.) If NULL, all the columns in the original table are selected and have the same name after redefinition. |
| options_flag | BINARY_INTEGER | IN | Indicates the type of redefinition method to use: If dbms_redefinition.cons_use_pk , the redefinition is done using primary keys or pseudo-primary keys (unique keys with all component columns having NOT NULL constraints). The default method of redefinition is using primary keys. If dbms_redefinition.cons_use_rowid , the redefinition is done using rowids. |
| orderby_cols | VARCHAR2 | IN | This optional parameter accepts the list of columns (along with the optional keyword(s) ascending/descending) with which to order by the rows during the initial instantiation of the interim table (the order by is only done for the initial instantiation and not for subsequent synchronizations) |
| part_name | VARCHAR2 | IN | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Can take a comma-delimited list of partition names to be redefined. |
| continue_after_errors | BOOLEAN | IN | When redefining multiple partitions allows operation execution to continue on the next partition (applies only to batched partition redefinition) |
| copy_vpd_opt | BINARY_INTEGER | IN | Specifies how VPD policies are handled in online redefinition |
| refresh_dep_mviews | VARCHAR2 | IN | When set to 'Y' , fast refresh of dependent materialized views is performed when the START_REDEF_TABLE procedure is run, each time the SYNC_INTERIM_TABLE procedure is run, and when the FINISH_REDEF_TABLE procedure is run. |
| enable_rollback | BOOLEAN | IN | When set to TRUE , enables the rollback option. When this parameter is set to true, Oracle Database maintains the interim table created during redefinition after redefinition is complete. You can run the SYNC_INTERIM_TABLE procedure to synchronize the interim table periodically to apply DML changes made to the redefined table to the interim table. An internal materialized view and materialized view log enables maintenance of the interim table. If you decide to roll back the online table redefinition with the ROLLBACK procedure, then the interim table is synchronized, and Oracle Database switches back to it so that the table has its original definition. |

## Usage Notes

Prior to calling this procedure, you must manually create an empty interim table (in the same schema as the table to be redefined) with the desired attributes of the post-redefinition table, and then call this procedure to initiate the redefinition. Syntax DBMS_REDEFINITION.START_REDEF_TABLE ( uname IN VARCHAR2, orig_table IN VARCHAR2, int_table IN VARCHAR2, col_mapping IN VARCHAR2 := NULL, options_flag IN BINARY_INTEGER := 1, orderby_cols IN VARCHAR2 := NULL, part_name IN VARCHAR2 := NULL, continue_after_errors IN BOOLEAN := FALSE, copy_vpd_opt IN BINARY_INTEGER := CONS_VPD_NONE, refresh_dep_mviews IN VARCHAR2 := 'N', enable_rollback IN BOOLEAN := FALSE); Parameters Table 138-14 START_REDEF_TABLE Procedure Parameters Parameter Description uname Schema name of the tables orig_table Name of the table to be redefined int_table Name of the interim table. Can take a comma-delimited list of interim table names. col_mapping Mapping information from the columns in the original table to the columns in the interim table. (This is similar to the column list on the SELECT clause of a query.) If NULL, all the columns in the original table are selected and have the same name after redefinition. options_flag Indicates the type of redefinition method to use: If dbms_redefinition.cons_use_pk , the redefinition is done using primary keys or pseudo-primary keys (unique keys with all component columns having NOT NULL constraints). The default method of redefinition is using primary keys. If dbms_redefinition.cons_use_rowid , the redefinition is done using rowids. orderby_cols This optional parameter accepts the list of columns (along with the optional keyword(s) ascending/descending) with which to order by the rows during the initial instantiation of the interim table (the order by is only done for the initial instantiation and not for subsequent synchronizations) part_name Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Can take a comma-delimited list of partition names to be redefined. continue_after_errors When redefining multiple partitions allows operation execution to continue on the next partition (applies only to batched partition redefinition) copy_vpd_opt Specifies how VPD policies are handled in online redefinition refresh_dep_mviews When set to 'Y' , fast refresh of dependent materialized views is performed when the START_REDEF_TABLE procedure is run, each time the SYNC_INTERIM_TABLE procedure is run, and when the FINISH_REDEF_TABLE procedure is run. enable_rollback When set to TRUE , enables the rollback option. When this parameter is set to true, Oracle Database maintains the interim table created during redefinition after redefinition is complete. You can run the SYNC_INTERIM_TABLE procedure to synchronize the interim table periodically to apply DML changes made to the redefined table to the interim table. An internal materialized view and materialized view log enables maintenance of the interim table. If you decide to roll back the online table redefinition with the ROLLBACK procedure, then the interim table is synchronized, and Oracle Database switches back to it so that the table has its original definition. Examples Start redefinition of three partitions ( sal03q1,sal03q2,sal03q3 ) in table 'STEVE.salestable' using three interim tables of int_salestable1 , int_salestable2 and int_salestable3 , respectively. The operation will continue on sal03q3 even if it fails on sal03q1 . DBMS_REDEFINITION.START_REDEF_TABLE( uname => 'STEVE', orig_table => 'salestable', int_table => 'int_salestable1, int_salestable2, int_salestable3', col_mapping => NULL, options_flag => DBMS_REDEFINITION.CONS_USE_ROWID, part_name => 'sal03q1,sal03q2,sal03q3', continue_after_errors => TRUE); Specify to copy VPD policies automatically: EXECUTE DBMS_REDEFINITION.START_REDEF_TABLE ( uname => 'SCOTT', orig_table => 'T', int_table => 'INT_T', copy_vpd_opt => DBMS_REDEFINITION.CONS_VPD_AUTO);