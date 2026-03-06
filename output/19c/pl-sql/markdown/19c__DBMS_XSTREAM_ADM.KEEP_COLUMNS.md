---
id: 19c__DBMS_XSTREAM_ADM.KEEP_COLUMNS
name: DBMS_XSTREAM_ADM.KEEP_COLUMNS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.KEEP_COLUMNS

This procedure either adds or removes a declarative rule-based transformation which keeps a list of columns in a row logical change record (LCR) that satisfies the specified rule. The transformation deletes columns that are not in the list from the row LCR.

## Syntax

```sql
DBMS_XSTREAM_ADM.KEEP_COLUMNS(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_list   IN  VARCHAR2,
   value_type    IN  VARCHAR2 DEFAULT '*',
   step_number   IN  NUMBER DEFAULT 0,
   operation     IN  VARCHAR2 DEFAULT 'ADD');

DBMS_XSTREAM_ADM.KEEP_COLUMNS(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_table  IN  DBMS_UTILITY.LNAME_ARRAY,
   value_type    IN  VARCHAR2 DEFAULT '*',
   step_number   IN  NUMBER DEFAULT 0,
   operation     IN  VARCHAR2 DEFAULT 'ADD');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. |
| table_name | VARCHAR2 | IN | The name of the table for which the columns are kept in the row LCR, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| column_list | VARCHAR2 | IN | The names of the columns kept for each row LCR that satisfies the rule. Specify a comma-delimited list of type VARCHAR2 . The transformation removes columns that are not in the list from the row LCR. If this parameter is set to NULL , and the column_table parameter is also set to NULL , then the procedure raises an error. |
| column_table | DBMS_UTILITY.LNAME_ARRAY | IN | The names of the columns kept for each row LCR that satisfies the rule. Specify a PL/SQL associative array of type DBMS_UTILITY.LNAME_ARRAY , where each element is the name of a column. The first schema should be in position 1. The last position must be NULL . The transformation removes columns that are not in the table from the row LCR. If this parameter is set to NULL , and the column_list parameter is also set to NULL , then the procedure raises an error. |
| value_type | VARCHAR2 | IN | Specify 'NEW' to keep the columns in the new values in the row LCR. Specify 'OLD' to keep the columns in the old values in the row LCR. Specify '*' to keep the columns in both the old and new values in the row LCR. |
| step_number | NUMBER | IN | The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering |
| operation | VARCHAR2 | IN | Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule. |

## Usage Notes

For the transformation to be performed when the specified rule evaluates to TRUE , the rule must be in the positive rule set of an XStream client. XStream clients include capture processes, propagations, and apply processes. This procedure is overloaded. The column_list parameter is type VARCHAR2 and the column_table parameter is type DBMS_UTILITY.LNAME_ARRAY . These parameters enable you to enter the list of columns in different ways and are mutually exclusive. Note: The KEEP_COLUMNS procedure supports the same data types supported by Oracle Replication capture processes. The KEEP_COLUMNS procedure is useful when you want to keep a relatively small number of columns in a row LCR. To keep most of the columns in a row LCR and delete a relatively small number of columns, consider using the DELETE_COLUMN procedure in this package. Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations and about the data types supported by Oracle Replication capture processes DELETE_COLUMN Procedure Note: The KEEP_COLUMNS procedure supports the same data types supported by Oracle Replication capture processes. The KEEP_COLUMNS procedure is useful when you want to keep a relatively small number of columns in a row LCR. To keep most of the columns in a row LCR and delete a relatively small number of columns, consider using the DELETE_COLUMN procedure in this package. Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations and about the data types supported by Oracle Replication capture processes DELETE_COLUMN Procedure Syntax DBMS_XSTREAM_ADM.KEEP_COLUMNS( rule_name IN VARCHAR2, table_name IN VARCHAR2, column_list IN VARCHAR2, value_type IN VARCHAR2 DEFAULT '*', step_number IN NUMBER DEFAULT 0, operation IN VARCHAR2 DEFAULT 'ADD'); DBMS_XSTREAM_ADM.KEEP_COLUMNS( rule_name IN VARCHAR2, table_name IN VARCHAR2, column_table IN DBMS_UTILITY.LNAME_ARRAY, value_type IN VARCHAR2 DEFAULT '*', step_number IN NUMBER DEFAULT 0, operation IN VARCHAR2 DEFAULT 'ADD'); Parameters Table 217-21 KEEP_COLUMNS Procedure Parameters Parameter Description rule_name The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. table_name The name of the table for which the columns are kept in the row LCR, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. column_list The names of the columns kept for each row LCR that satisfies the rule. Specify a comma-delimited list of type VARCHAR2 . The transformation removes columns that are not in the list from the row LCR. If this parameter is set to NULL , and the column_table parameter is also set to NULL , then the procedure raises an error. column_table The names of the columns kept for each row LCR that satisfies the rule. Specify a PL/SQL associative array of type DBMS_UTILITY.LNAME_ARRAY , where each element is the name of a column. The first schema should be in position 1. The last position must be NULL . The transformation removes columns that are not in the table from the row LCR. If this parameter is set to NULL , and the column_list parameter is also set to NULL , then the procedure raises an error. value_type Specify 'NEW' to keep the columns in the new values in the row LCR. Specify 'OLD' to keep the columns in the old values in the row LCR. Specify '*' to keep the columns in both the old and new values in the row LCR. step_number The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering operation Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule.