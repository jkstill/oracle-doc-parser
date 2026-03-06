---
id: 19c__DBMS_APPLY_ADM.COMPARE_OLD_VALUES
name: DBMS_APPLY_ADM.COMPARE_OLD_VALUES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.COMPARE_OLD_VALUES

This procedure specifies whether to compare the old values of one or more columns in a row logical change record (row LCR) with the current values of the corresponding columns at the destination site during apply.

## Syntax

```sql
DBMS_APPLY_ADM.COMPARE_OLD_VALUES(
   object_name         IN VARCHAR2,
   column_list         IN VARCHAR2,
   operation           IN VARCHAR2 DEFAULT 'UPDATE',
   compare             IN BOOLEAN  DEFAULT TRUE,
   apply_database_link IN VARCHAR2 DEFAULT NULL);

DBMS_APPLY_ADM.COMPARE_OLD_VALUES(
   object_name         IN VARCHAR2,
   column_table        IN DBMS_UTILITY.LNAME_ARRAY,
   operation           IN VARCHAR2 DEFAULT 'UPDATE',
   compare             IN BOOLEAN  DEFAULT TRUE,
   apply_database_link IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name | VARCHAR2 | IN | The name of the source table specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| column_list | VARCHAR2 | IN | A comma-delimited list of column names in the table. There must be no spaces between entries. Specify * to include all nonkey columns. |
| column_table | DBMS_UTILITY.LNAME_ARRAY | IN | A PL/SQL associative array of type DBMS_UTILITY.LNAME_ARRAY that contains names of columns in the table. The first column name should be at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. |
| operation | VARCHAR2 | IN | The name of the operation, which can be specified as: UPDATE for UPDATE operations DELETE for DELETE operations * for both UPDATE and DELETE operations |
| compare | BOOLEAN | IN | If compare is TRUE , the old values of the specified columns are compared during apply. If compare is FALSE , the old values of the specified columns are not compared during apply. |
| apply_database_link | VARCHAR2 | IN | The name of the database link to a non-Oracle database. This parameter should be set only when the destination database is a non-Oracle database. |

## Usage Notes

This procedure is relevant only for UPDATE and DELETE operations because only these operations result in old column values in row LCRs. The default is to compare old values for all columns. This procedure is overloaded. The column_list and column_table parameters are mutually exclusive. Syntax DBMS_APPLY_ADM.COMPARE_OLD_VALUES( object_name IN VARCHAR2, column_list IN VARCHAR2, operation IN VARCHAR2 DEFAULT 'UPDATE', compare IN BOOLEAN DEFAULT TRUE, apply_database_link IN VARCHAR2 DEFAULT NULL); DBMS_APPLY_ADM.COMPARE_OLD_VALUES( object_name IN VARCHAR2, column_table IN DBMS_UTILITY.LNAME_ARRAY, operation IN VARCHAR2 DEFAULT 'UPDATE', compare IN BOOLEAN DEFAULT TRUE, apply_database_link IN VARCHAR2 DEFAULT NULL); Parameters Table 21-4 COMPARE_OLD_VALUES Procedure Parameters Parameter Description object_name The name of the source table specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. column_list A comma-delimited list of column names in the table. There must be no spaces between entries. Specify * to include all nonkey columns. column_table A PL/SQL associative array of type DBMS_UTILITY.LNAME_ARRAY that contains names of columns in the table. The first column name should be at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. operation The name of the operation, which can be specified as: UPDATE for UPDATE operations DELETE for DELETE operations * for both UPDATE and DELETE operations compare If compare is TRUE , the old values of the specified columns are compared during apply. If compare is FALSE , the old values of the specified columns are not compared during apply. apply_database_link The name of the database link to a non-Oracle database. This parameter should be set only when the destination database is a non-Oracle database. Usage Notes The following usage notes apply to this procedure: Conflict Detection The COMPARE_OLD_VALUES Procedure and XStream Outbound Servers The COMPARE_OLD_VALUES Procedure and XStream Inbound Servers Conflict Detection By default, an apply component uses the old column values in a row LCR to detect conflicts. You can choose not to compare old column values to avoid conflict detection for specific tables. For example, if you do not want to compare the old values for a set of columns during apply, then, using the COMPARE_OLD_VALUES procedure, specify the set of columns in the column_list or column_table parameter, and set the compare parameter to FALSE . In addition, when the compare_key_only apply component parameter is set to Y , automatic conflict detection is disabled, and the apply component only uses primary key and unique key columns to identify the table row for a row LCR. When the compare_key_only apply component parameter is set to N , automatic conflict detection is enabled, and the apply component uses all of the old values in a row LCR to identify the table row for a row LCR. Note: An apply component compares old values for non-key columns when they are present in a row LCR and when the apply component parameter compare_key_only is set to N . This procedure raises an error if a key column is specified in column_list or column_table and the compare parameter is set to FALSE . See Also: SET_PARAMETER Procedure for more information about the compare_key_only apply component parameter The COMPARE_OLD_VALUES Procedure and XStream Outbound Servers This procedure has no effect on XStream outbound servers. The COMPARE_OLD_VALUES Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers. Note: An apply component compares old values for non-key columns when they are present in a row LCR and when the apply component parameter compare_key_only is set to N . This procedure raises an error if a key column is specified in column_list or column_table and the compare parameter is set to FALSE .