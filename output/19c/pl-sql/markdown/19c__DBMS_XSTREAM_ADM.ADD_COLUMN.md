---
id: 19c__DBMS_XSTREAM_ADM.ADD_COLUMN
name: DBMS_XSTREAM_ADM.ADD_COLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.ADD_COLUMN

This procedure either adds or removes a declarative rule-based transformation which adds a column to a row logical change record (row LCR) that satisfies the specified rule.

## Syntax

```sql
DBMS_XSTREAM_ADM.ADD_COLUMN(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   column_value  IN  ANYDATA,
   value_type    IN  VARCHAR2     DEFAULT 'NEW',
   step_number   IN  NUMBER       DEFAULT 0,
   operation     IN  VARCHAR2     DEFAULT 'ADD');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. |
| table_name | VARCHAR2 | IN | The name of the table to which the column is added in the row LCR, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| column_name | VARCHAR2 | IN | The name of the column added to each row LCR that satisfies the rule. |
| column_value | ANYDATA | IN | The value of the added column. Specify the appropriate ANYDATA function for the column datatype and the column value. For example, if the datatype of the column being added is NUMBER and the value is NULL , then specify the ANYDATA.ConvertNumber(NULL) function. This parameter cannot be specified if the column_function parameter is specified. |
| column_function |  |  | Either the 'SYSDATE' or the 'SYSTIMESTAMP' SQL function. The 'SYSDATE' SQL function places the current date and time set for the operating system on which the database resides. The datatype of the returned value is DATE , and the format returned depends on the value of the NLS_DATE_FORMAT initialization parameter. The 'SYSTIMESTAMP' SQL function returns the system date, including fractional seconds and time zone, of the system on which the database resides. The return type is TIMESTAMP WITH TIME ZONE . The function executes when the rule evaluates to TRUE . This parameter cannot be specified if the column_value parameter is specified. |
| value_type | VARCHAR2 | IN | Specify 'NEW' to add the column to the new values in the row LCR. Specify 'OLD' to add the column to the old values in the row LCR. |
| step_number | NUMBER | IN | The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering |
| operation | VARCHAR2 | IN | Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule. |

## Usage Notes

For the transformation to be performed when the specified rule evaluates to TRUE , the rule must be in the positive rule set of an XStream client. XStream clients include capture processes, propagations, and apply processes. This procedure is overloaded. The column_value and column_function parameters are mutually exclusive. Note: ADD_COLUMN transformations cannot add columns of the following data types: BLOB , CLOB , NCLOB , BFILE , LONG , LONG RAW , ROWID , user-defined types (including object types, REF s, varrays, nested tables), and Oracle-supplied types (including any types, XML types, spatial types, and media types). Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations Note: ADD_COLUMN transformations cannot add columns of the following data types: BLOB , CLOB , NCLOB , BFILE , LONG , LONG RAW , ROWID , user-defined types (including object types, REF s, varrays, nested tables), and Oracle-supplied types (including any types, XML types, spatial types, and media types). Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations Syntax DBMS_XSTREAM_ADM.ADD_COLUMN( rule_name IN VARCHAR2, table_name IN VARCHAR2, column_name IN VARCHAR2, column_value IN ANYDATA, value_type IN VARCHAR2 DEFAULT 'NEW', step_number IN NUMBER DEFAULT 0, operation IN VARCHAR2 DEFAULT 'ADD'); DBMS_XSTREAM_ADM.ADD_COLUMN( rule_name IN VARCHAR2, table_name IN VARCHAR2, column_name IN VARCHAR2, column_function IN VARCHAR2, value_type IN VARCHAR2 DEFAULT 'NEW', step_number IN NUMBER DEFAULT 0, operation IN VARCHAR2 DEFAULT 'ADD'); Parameters Table 217-2 ADD_COLUMN Procedure Parameters Parameter Description rule_name The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. table_name The name of the table to which the column is added in the row LCR, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. column_name The name of the column added to each row LCR that satisfies the rule. column_value The value of the added column. Specify the appropriate ANYDATA function for the column datatype and the column value. For example, if the datatype of the column being added is NUMBER and the value is NULL , then specify the ANYDATA.ConvertNumber(NULL) function. This parameter cannot be specified if the column_function parameter is specified. column_function Either the 'SYSDATE' or the 'SYSTIMESTAMP' SQL function. The 'SYSDATE' SQL function places the current date and time set for the operating system on which the database resides. The datatype of the returned value is DATE , and the format returned depends on the value of the NLS_DATE_FORMAT initialization parameter. The 'SYSTIMESTAMP' SQL function returns the system date, including fractional seconds and time zone, of the system on which the database resides. The return type is TIMESTAMP WITH TIME ZONE . The function executes when the rule evaluates to TRUE . This parameter cannot be specified if the column_value parameter is specified. value_type Specify 'NEW' to add the column to the new values in the row LCR. Specify 'OLD' to add the column to the old values in the row LCR. step_number The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering operation Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule.