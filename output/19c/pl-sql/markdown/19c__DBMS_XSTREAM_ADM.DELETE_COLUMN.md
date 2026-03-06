---
id: 19c__DBMS_XSTREAM_ADM.DELETE_COLUMN
name: DBMS_XSTREAM_ADM.DELETE_COLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.DELETE_COLUMN

This procedure either adds or removes a declarative rule-based transformation which deletes a column from a row logical change record (LCR) that satisfies the specified rule.

## Syntax

```sql
DBMS_XSTREAM_ADM.DELETE_COLUMN(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   value_type    IN  VARCHAR2   DEFAULT '*',
   step_number   IN  NUMBER     DEFAULT 0,
   operation     IN  VARCHAR2   DEFAULT 'ADD');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. |
| table_name | VARCHAR2 | IN | The name of the table from which the column is deleted in the row LCR, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| column_name | VARCHAR2 | IN | The name of the column deleted from each row LCR that satisfies the rule. |
| value_type | VARCHAR2 | IN | Specify 'NEW' to delete the column from the new values in the row LCR. Specify 'OLD' to delete the column from the old values in the row LCR. Specify '*' to delete the column from both the old and new values in the row LCR. |
| step_number | NUMBER | IN | The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering |
| operation | VARCHAR2 | IN | Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule. |

## Usage Notes

For the transformation to be performed when the specified rule evaluates to TRUE , the rule must be in the positive rule set of an XStream client. XStream clients include capture processes, propagations, and apply processes. Note: The DELETE_COLUMN procedure supports the same data types supported by Oracle Replication capture processes. The DELETE_COLUMN procedure is useful when you want to delete a relatively small number of columns in a row LCR. To delete most of the columns in a row LCR and keep a relatively small number of columns, consider using the KEEP_COLUMNS procedure in this package. Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations and about the data types supported by capture processes KEEP_COLUMNS Procedure Note: The DELETE_COLUMN procedure supports the same data types supported by Oracle Replication capture processes. The DELETE_COLUMN procedure is useful when you want to delete a relatively small number of columns in a row LCR. To delete most of the columns in a row LCR and keep a relatively small number of columns, consider using the KEEP_COLUMNS procedure in this package. Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations and about the data types supported by capture processes KEEP_COLUMNS Procedure Syntax DBMS_XSTREAM_ADM.DELETE_COLUMN( rule_name IN VARCHAR2, table_name IN VARCHAR2, column_name IN VARCHAR2, value_type IN VARCHAR2 DEFAULT '*', step_number IN NUMBER DEFAULT 0, operation IN VARCHAR2 DEFAULT 'ADD'); Parameters Table 217-17 DELETE_COLUMN Procedure Parameters Parameter Description rule_name The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. table_name The name of the table from which the column is deleted in the row LCR, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. column_name The name of the column deleted from each row LCR that satisfies the rule. value_type Specify 'NEW' to delete the column from the new values in the row LCR. Specify 'OLD' to delete the column from the old values in the row LCR. Specify '*' to delete the column from both the old and new values in the row LCR. step_number The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering operation Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule.